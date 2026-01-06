#!/usr/bin/env python3
"""
Automated Guardrail Validation and Fix System
Integrates with Agent Workflow Orchestrator
"""

import re
import json
import os
import glob
from typing import Dict, List, Tuple

class GuardrailValidator:
    def __init__(self, patterns_file: str = "validation-patterns.json"):
        """Initialize validator with pattern definitions"""
        with open(patterns_file, 'r') as f:
            self.patterns = json.load(f)
    
    def scan_violations(self, content: str) -> Dict[str, List[str]]:
        """Scan content for guardrail violations"""
        violations = {}
        
        for check_pattern in self.patterns['validation_checks']['scan_patterns']:
            matches = re.findall(check_pattern, content)
            if matches:
                violations[check_pattern] = matches
        
        return violations
    
    def apply_fixes(self, content: str) -> Tuple[str, List[Dict]]:
        """Apply auto-fixes to content and return fixed content + log"""
        fixes_applied = []
        fixed_content = content
        
        # Process all violation categories
        for category, patterns in self.patterns['guardrail_patterns'].items():
            for violation_type, fix_config in patterns.items():
                pattern = fix_config['pattern']
                replacement = fix_config['replacement']
                description = fix_config['description']
                
                # Count matches before fixing
                matches = re.findall(pattern, fixed_content)
                if matches:
                    # Apply fix
                    fixed_content = re.sub(pattern, replacement, fixed_content)
                    
                    fixes_applied.append({
                        'type': violation_type,
                        'category': category,
                        'description': description,
                        'matches_fixed': len(matches),
                        'examples': matches[:3]  # Show first 3 examples
                    })
        
        return fixed_content, fixes_applied
    
    def validate_file(self, file_path: str) -> Dict:
        """Validate and fix a single file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            # Scan for violations
            violations = self.scan_violations(original_content)
            
            if not violations:
                return {
                    'file': file_path,
                    'status': 'compliant',
                    'violations_found': 0,
                    'fixes_applied': []
                }
            
            # Apply fixes
            fixed_content, fixes_applied = self.apply_fixes(original_content)
            
            # Write fixed content back to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            
            # Check if all violations were fixed
            remaining_violations = self.scan_violations(fixed_content)
            
            return {
                'file': file_path,
                'status': 'fixed' if not remaining_violations else 'partial',
                'violations_found': sum(len(v) for v in violations.values()),
                'fixes_applied': fixes_applied,
                'remaining_violations': remaining_violations
            }
            
        except Exception as e:
            return {
                'file': file_path,
                'status': 'error',
                'error': str(e)
            }
    
    def validate_directory(self, directory: str) -> Dict:
        """Validate all markdown files in directory"""
        md_files = glob.glob(os.path.join(directory, "*.md"))
        
        results = {
            'directory': directory,
            'files_processed': 0,
            'files_compliant': 0,
            'files_fixed': 0,
            'files_with_remaining_violations': 0,
            'total_violations_found': 0,
            'total_fixes_applied': 0,
            'file_results': [],
            'summary': {}
        }
        
        for file_path in md_files:
            file_result = self.validate_file(file_path)
            results['file_results'].append(file_result)
            results['files_processed'] += 1
            
            if file_result['status'] == 'compliant':
                results['files_compliant'] += 1
            elif file_result['status'] == 'fixed':
                results['files_fixed'] += 1
                results['total_violations_found'] += file_result['violations_found']
                results['total_fixes_applied'] += len(file_result['fixes_applied'])
            elif file_result['status'] == 'partial':
                results['files_with_remaining_violations'] += 1
                results['total_violations_found'] += file_result['violations_found']
                results['total_fixes_applied'] += len(file_result['fixes_applied'])
        
        # Generate summary
        if results['files_with_remaining_violations'] == 0:
            results['summary']['status'] = 'COMPLIANT'
            results['summary']['message'] = 'All files pass guardrail validation'
        else:
            results['summary']['status'] = 'VIOLATIONS_REMAIN'
            results['summary']['message'] = f"{results['files_with_remaining_violations']} files have remaining violations"
        
        return results

def format_validation_report(results: Dict) -> str:
    """Format validation results for orchestrator display"""
    
    if results['files_processed'] == 0:
        return "🛡️ **Guardrail Validation** - No files found to validate"
    
    report = f"🛡️ **Guardrail Validation - {results['directory']}**\n\n"
    
    # Summary stats
    report += f"📊 **Violations Detected & Fixed:**\n"
    report += f"- Files processed: {results['files_processed']}\n"
    report += f"- Violations found: {results['total_violations_found']}\n"
    report += f"- Auto-fixes applied: {results['total_fixes_applied']}\n"
    report += f"- Files requiring manual review: {results['files_with_remaining_violations']}\n\n"
    
    # Show examples of fixes
    if results['total_fixes_applied'] > 0:
        report += "✅ **Auto-Fix Examples:**\n"
        for file_result in results['file_results']:
            if file_result.get('fixes_applied'):
                for fix in file_result['fixes_applied'][:2]:  # Show first 2 fixes
                    examples = ', '.join(fix['examples'][:2])
                    report += f"- {fix['description']}: {examples}\n"
        report += "\n"
    
    # Final status
    status_icon = "✅" if results['summary']['status'] == 'COMPLIANT' else "❌"
    report += f"🎯 **Final Status:** {status_icon} {results['summary']['status']}\n"
    report += f"{results['summary']['message']}\n"
    
    return report

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python validate-guardrails.py <directory>")
        sys.exit(1)
    
    directory = sys.argv[1]
    
    if not os.path.exists(directory):
        print(f"Error: Directory {directory} does not exist")
        sys.exit(1)
    
    # Initialize validator
    patterns_file = os.path.join(os.path.dirname(__file__), "validation-patterns.json")
    validator = GuardrailValidator(patterns_file)
    
    # Run validation
    results = validator.validate_directory(directory)
    
    # Print formatted report
    report = format_validation_report(results)
    print(report)
    
    # Exit with appropriate code
    sys.exit(0 if results['summary']['status'] == 'COMPLIANT' else 1)
