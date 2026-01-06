# Context-Driven Product Discovery - Agent Workflow System

## Project Overview

An AI-powered research analysis system that transforms weeks of strategic analysis into hours, while maintaining human oversight and validation. This system uses specialized AI agents to analyze customer interviews and user research data, automatically identifying key problems, opportunities, and strategic insights.

**What it does:**
• Takes customer interviews and user research data as input
• Automatically identifies key problems, opportunities, and strategic insights  
• Generates complete analysis from pain points to solution recommendations
• Produces executive-ready reports and implementation roadmaps
• Requires human validation at each step to ensure accuracy and relevance

**Benefits for Product & Design Teams:**
• **Speed:** Complete strategic analysis in hours instead of weeks
• **Quality:** Captures insights and patterns humans typically miss under time pressure
• **Completeness:** Full package from problem identification to actionable solutions
• **Sprint-compatible:** Deep analysis that fits within 2-week sprint cycles
• **Stakeholder-ready:** Professional deliverables for leadership presentations

---

## Directory Structure

The project follows a systematic problem → solution → delivery progression with specialized agent orchestration:

```
├── 0-documentation/          # Project context and source materials
│   ├── 0a-projectdocs/       # Project documentation and context
│   │   └── context.md        # Business context and objectives
│   └── 0b-Interviews/        # Source interview files
├── 1-problem/               # Problem analysis phase (Agents 0-6)
│   ├── 1a-interview-analysis/  # Individual interview breakdowns (Agent 1)
│   ├── 1b-painpoints/         # Pain point analysis (Agents 2A & 2B)
│   │   ├── 1b0-granular/      # Atomic pain point decomposition (Agent 2A)
│   │   ├── 1b1-painpoints-breakdown/  # Clustered pain analyses (Agent 2B)
│   │   └── painpoint-mapping.md       # Final consolidated mapping (Agent 2B)
│   ├── 1c-asis-journey/       # Current state journey mapping (Agents 3 & 4)
│   │   └── 1c2-asis-breakdown/  # Individual journey stage analyses
│   └── 1d-problem-output/     # Final problem reports (Agent 5) + visual specs (Agent 6)
├── 2-solution/              # Solution ideation phase (Agents 6-10)
│   ├── 2a-opportunities/      # Strategic opportunities (Agent 6)
│   │   └── 2a1-opportunities-breakdown/  # Individual opportunity analyses
│   ├── 2b-tobe_journey/       # Future experience journey (Agent 7)
│   │   └── 2b1-journey-breakdown/  # Individual future stage analyses
│   ├── 2c-priotization/       # Solution concepts & feasibility (Agent 8)
│   │   └── 2c1-concept-breakdown/  # Individual concept details
│   ├── 2d-roadmap/            # MVP scope & feature prioritization (Agent 9)
│   │   ├── 2d1-mvp/           # Core MVP features
│   │   └── 2d2-stage2/        # Post-MVP features
│   └── 2e-solution-output/    # Product communications (Agent 10)
│       └── stakeholder-communications/  # Audience-specific materials
├── 3-delivery/              # Delivery preparation phase (Agents 11-12)
│   ├── confluence/           # Confluence documentation structure (Agent 11)
│   └── jira/                 # Jira project structure (Agent 12)
├── _agents/                 # Agent instruction files
│   ├── problem-space/       # Agents 0-6 (problem analysis)
│   ├── solution-space/      # Agents 6-10 (solution development)
│   ├── delivery-space/      # Agents 11-12 (delivery preparation)
│   ├── guardrail-validator.md  # Quality validation agent
│   ├── GUARDRAILS-ENFORCEMENT.md  # Data integrity rules
│   ├── guardrails-police.md    # Quality enforcement agent
│   ├── validate-guardrails.py # Python validation automation
│   ├── validation-patterns.json # Validation rule definitions
│   └── validation-readme.md    # Validation system docs
└── _output-structure/       # Templates and formatting guides
    ├── problem-space/       # Problem analysis templates (7 templates)
    ├── solution-space/      # Solution development templates (19 templates)
    ├── delivery-space/      # Delivery preparation templates (5 templates)
    └── workflow-rules.md    # Process and progression rules
```

---

## Agent Workflow System

### Phase 1: Problem Analysis (Agents 0-6)
**Trigger:** Manual execution or "start workflow"
**Duration:** 2-4 hours for complete problem analysis
**Output:** Comprehensive problem understanding with strategic context and visual specifications

**🔍 Problem Space Agents:**

**Agent 0: Product & Service Specialist**
- Creates project structure and broad context
- Establishes business objectives and scope
- **Output:** `0-documentation/0a-projectdocs/context.md`, directory scaffolding

**Agent 1: Qualitative Research Specialist** 
- Analyzes individual interview files
- Extracts insights, pain points, and opportunities
- **Output:** Structured interview analyses in `1a-interview-analysis/`

**Agent 2A: Pain Point Granularization Specialist** ⚡
- **DECOMPOSES** pain points into atomic, specific problems (30-50 pain points)
- Applies atomicity tests to ensure maximum granularity
- Classifies by TYPE (UX/Ops/Business/Tech)
- **Philosophy:** Divergent analysis - break everything into smallest parts
- **Output:** `1b-painpoints/1b0-granular/all-painpoints-granular.md`

**Agent 2B: Pain Point Clustering Specialist** ⚡
- **GROUPS** atomic pain points by relational patterns (4-6 clusters)
- Identifies causal, contextual, and thematic relationships
- Creates meaningful thematic clusters
- **Philosophy:** Convergent analysis - find meaningful patterns
- **Output:** Cluster files in `1b1-painpoints-breakdown/` + `painpoint-mapping.md`

**Agent 3: As-Is Journey Mapper**
- Creates detailed current-state journey maps
- Documents tools, processes, and pain points per stage
- **Output:** Journey mapping files in `1c-asis-journey/` + `1c2-asis-breakdown/`

**Agent 4: Journey Consolidation Specialist**
- Consolidates multiple journeys into unified flow
- Creates comprehensive current-state overview
- **Output:** Consolidated journey in `1c-asis-journey/asis-journey.md`

**Agent 5: Strategic Report Generator**
- Generates executive-ready problem reports
- Creates strategic problem statements with recommendations
- **Output:** Final reports in `1d-problem-output/`

**Agent 6: Visual Journey Designer** (Problem Space)
- Creates Figma Make-ready visual journey specifications
- Transforms journey maps into visual design specifications
- Prepares AI-powered design tool inputs
- **Output:** Visual journey specs in `1d-problem-output/`

### Phase 2: Solution Development (Agents 6-10)
**Trigger:** "start workflow" after Phase 1 completion
**Duration:** 2-3 hours for complete solution package
**Output:** Implementation-ready product/service concepts with strategic roadmaps
**Focus:** Digital products, services, and experience improvements (not process automation)

**💡 Solution Space Agents:**

**Agent 6: Solution Ideation Specialist** (Solution Space)
- Transforms pain points into product/service/experience opportunities
- Creates prioritization matrices using RICE + User Impact framework
- Designs strategic roadmap with quick wins
- **Output:** Opportunities, prioritization matrix, and roadmap in `2a-opportunities/` + `2a1-opportunities-breakdown/`

**Agent 7: Experience Design Specialist**
- Designs consolidated future journey (To-Be state)
- Maps experience improvements to journey stages
- Defines value moments and UX quality targets
- Documents transformation (As-Is → To-Be)
- **Output:** Future journey and improvements in `2b-tobe_journey/` + `2b1-journey-breakdown/`

**Agent 8: Solution Concept Specialist**
- Details solution concepts (features, capabilities, benefits)
- Assesses feasibility (technical, business, desirability)
- Creates concept-level specifications (NOT technical specs)
- Provides recommendations based on feasibility
- **Output:** Solution concepts and feasibility in `2c-priotization/` + `2c1-concept-breakdown/`

**Agent 9: Product Prioritization Specialist**
- Defines ruthlessly prioritized MVP scope (core value proposition)
- Prioritizes features using Impact vs Effort Matrix
- Creates validation plan with hypotheses and metrics
- Plans post-MVP roadmap (Stage 2)
- **Output:** MVP scope, feature prioritization, validation plan in `2d-roadmap/` + `2d1-mvp/` + `2d2-stage2/`

**Agent 10: Product Communication Specialist**
- Creates comprehensive product brief and visual roadmap
- Documents experience evolution
- Develops stakeholder communication plans
- Prepares executive presentation materials
- **Output:** Product communications and executive materials in `2e-solution-output/` + `stakeholder-communications/`

### Phase 3: Delivery Preparation (Agents 11-12)
**Trigger:** "start workflow" after Phase 2 completion, or manual execution
**Duration:** 1-2 hours for complete delivery structure
**Output:** Ready-to-import documentation and project structures for Confluence and Jira
**Purpose:** Transform strategic analysis into executable implementation structures

**📦 Delivery Space Agents:**

**Agent 11: Confluence Documentation Specialist**
- Structures and formats all project documentation for Confluence
- Creates navigable page hierarchy and subpages
- Converts markdown to Confluence format (tables, macros, panels)
- Establishes internal page links and breadcrumbs
- **Output:** Complete Confluence structure in `3-delivery/confluence/`

**Agent 12: Jira Project Setup Specialist**
- Creates Initiative, Epics, and Stories in Jira format
- Populates all fields with strategic context
- Defines relationships and dependencies
- Establishes prioritization and sprint allocation
- **Output:** Complete Jira structure in `3-delivery/jira/` with import guide

---

## Key Deliverables

### Problem Analysis Package (Phase 1)
- **Granular Pain Point Catalog** (Agent 2A) - 30-50 atomic, specific problems
- **Clustered Pain Point Analysis** (Agent 2B) - 4-6 thematic clusters with relationships
- **Pain Point Mapping** (Agent 2B) - Consolidated mapping of all pain points
- **Current State Journey** (Agents 3 & 4) - Detailed As-Is process mapping with bottlenecks
- **Strategic Problem Report** (Agent 5) - Comprehensive analysis ready for stakeholder review
- **Visual Journey Specifications** (Agent 6) - Figma Make-ready design specs

### Solution Development Package (Phase 2)  
- **Strategic Opportunities** (Agent 6) - Product/service/experience opportunities with prioritization matrix
- **Implementation Roadmap** (Agent 6) - Phased approach with quick wins and success metrics
- **Future Journey Design** (Agent 7) - To-Be experience with improvements mapped to stages
- **Solution Concepts** (Agent 8) - Detailed concepts with feasibility assessment
- **MVP Scope** (Agent 9) - Ruthlessly prioritized core features with validation plan
- **Product Brief** (Agent 10) - Comprehensive product documentation
- **Executive Presentation** (Agent 10) - Leadership-ready materials for decision making
- **Stakeholder Communications** (Agent 10) - Audience-specific messaging and communication plans

### Delivery Preparation Package (Phase 3)
- **Confluence Documentation Structure** (Agent 11) - Complete, navigable page hierarchy ready for import
- **Jira Project Structure** (Agent 12) - Initiative, Epics, and Stories with description populated and relationships defined
- **Import Guides** (Agents 11 & 12) - Step-by-step instructions for importing into Confluence and Jira

---

## How to Use the System

### Getting Started
1. **Prepare Source Materials:**
   - Place interview files in `0-documentation/0b-Interviews/`
   - Create/update `0-documentation/0a-projectdocs/context.md` with business objectives
   - Ensure interviews contain: process steps, pain points, needs, opportunities

### Phase 1: Problem Analysis (Agents 0-6)
2. **Trigger the Workflow:**
   ```
   "start workflow"
   ```
   - System automatically progresses through Agents 0-6
   - Agent 2 now split into 2A (granularization) and 2B (clustering)
   - Each agent builds on previous outputs
   - Validates completion before proceeding

3. **Review Problem Analysis:**
   - Check granular pain points in `1b-painpoints/1b0-granular/`
   - Review clustered analyses in `1b-painpoints/1b1-painpoints-breakdown/`
   - Validate pain point mapping in `1b-painpoints/painpoint-mapping.md`
   - Confirm current state journey in `1c-asis-journey/`
   - Review problem reports in `1d-problem-output/`

### Phase 2: Solution Development (Agents 6-10)
4. **Continue to Solution Phase:**
   ```
   "start workflow" (continues automatically after Phase 1)
   ```
   - Agents 6-10 transform problems into product/service concepts
   - Creates comprehensive solution package with MVP definition
   - Generates stakeholder-ready presentations and communications

5. **Review Solution Package:**
   - Strategic opportunities in `2a-opportunities/`
   - Future journey design in `2b-tobe_journey/`
   - Solution concepts in `2c-priotization/`
   - MVP scope and prioritization in `2d-roadmap/`
   - Product communications in `2e-solution-output/`

### Phase 3: Delivery Preparation (Agents 11-12)
6. **Prepare for Implementation:**
   ```
   "start workflow" (continues automatically after Phase 2)
   ```
   or manually trigger:
   ```
   "Run Agent 11 to create Confluence documentation structure"
   "Run Agent 12 to create Jira project structure"
   ```
   - Agent 11 creates Confluence-ready documentation
   - Agent 12 creates Jira-ready project structure
   - Both outputs ready for direct import

7. **Review Delivery Package:**
   - Confluence structure in `3-delivery/confluence/`
   - Jira structure in `3-delivery/jira/`
   - Follow import guides for each platform

### Quality Assurance
8. **Validation Checkpoints:**
   - Each agent includes completion criteria
   - Cross-references maintained across all phases
   - Conservative estimates with source attribution
   - No invented metrics or unsupported claims
   - Automated guardrail validation throughout

---

## Agent Dependencies and Templates

### Problem Space Templates (7 templates)
- **Interview Analysis Template** - Standardized insight extraction (Agent 1)
- **Granular Pain Point Template** - Atomic pain point decomposition (Agent 2A)
- **Pain Point Analysis Template** - Clustered analysis and process mapping (Agent 2B)
- **Journey Mapping Template** - Current state documentation (Agents 3 & 4)
- **Journey Visualization Template** - Visual journey specifications (Agent 6)
- **Report Template** - Strategic reports and executive summaries (Agent 5)
- **Model Structure** - Core directory structure reference

### Solution Space Templates (19 templates)
- **Opportunity Identification Template** - Strategic opportunity analysis (Agent 6)
- **Opportunity Breakdown Template** - Individual opportunity details (Agent 6)
- **Prioritization Matrix Template** - Impact vs feasibility scoring (Agent 6)
- **Strategic Roadmap Template** - Phased implementation planning (Agent 6)
- **Future Journey Template** - To-Be journey design (Agent 7)
- **Future Journey Breakdown Template** - Individual stage details (Agent 7)
- **Experience Improvements Template** - Experience transformation mapping (Agent 7)
- **Experience Evolution Template** - As-Is to To-Be transformation (Agent 7)
- **Solution Concept Template** - Concept documentation (Agent 8)
- **Concept Breakdown Template** - Individual concept details (Agent 8)
- **Feasibility Assessment Template** - Feasibility analysis (Agent 8)
- **MVP Scope Template** - Core MVP definition (Agent 9)
- **Feature Prioritization Template** - Feature impact/effort matrix (Agent 9)
- **Validation Plan Template** - Hypothesis and metrics (Agent 9)
- **Product Brief Template** - Comprehensive product documentation (Agent 10)
- **Product Roadmap Template** - Visual product roadmap (Agent 10)
- **Executive Presentation Template** - Leadership decision materials (Agent 10)
- **Stakeholder Communication Template** - Audience-specific messaging (Agent 10)
- **Conservative Estimation Guide** - Financial projection guidelines
- **Guardrail Validation Checklist** - Quality validation framework

### Delivery Space Templates (5 templates)
- **Confluence Page Template** - Confluence documentation structure (Agent 11)
- **Jira Initiative Template** - Strategic initiative setup (Agent 12)
- **Jira Epic Template** - Epic structure and fields (Agent 12)
- **Jira Story Template** - User story format (Agent 12)
- **Import Guide Template** - Platform import instructions (Agents 11 & 12)

---

## Important: Agent 6 Exists in TWO Places

**⚠️ Understanding the Two Agent 6s:**

The system has **two distinct Agent 6s** that serve different purposes in different phases:

### Agent 6 (Problem Space) - Visual Journey Designer
- **Phase:** Problem Analysis (Phase 1)
- **Purpose:** Create visual journey specifications for design tools
- **Input:** Agent 5's strategic reports and journey maps
- **Output:** Figma Make-ready specifications in `1d-problem-output/`
- **Focus:** Translating analysis into visual design specifications

### Agent 6 (Solution Space) - Solution Ideation Specialist
- **Phase:** Solution Development (Phase 2)
- **Purpose:** Transform problems into product opportunities
- **Input:** Phase 1 outputs (pain reports, journey, problem statement)
- **Output:** Opportunities, prioritization, roadmap in `2a-opportunities/`
- **Focus:** Strategic opportunity identification and prioritization

**Why Two Agent 6s?**
- They operate in different phases (Problem vs Solution)
- They have completely different inputs and outputs
- They serve distinct strategic purposes
- No risk of confusion during sequential workflow execution

**Sequential Workflow:**
```
Phase 1: Agents 0 → 1 → 2A → 2B → 3 → 4 → 5 → 6 (Visual)
Phase 2: Agents 6 (Ideation) → 7 → 8 → 9 → 10
Phase 3: Agents 11 → 12
```

---

## Quality Control & Validation

### Automated Quality Assurance
The system includes comprehensive quality control mechanisms to ensure analysis accuracy and output reliability:

**🔍 Guardrail Validator**
- **Purpose:** Automated quality checking and validation
- **Function:** Validates agent outputs against quality standards
- **Location:** `_agents/guardrail-validator.md`

**🐍 Validation Scripts**
- **Python Automation:** `_agents/validate-guardrails.py`
- **Pattern Definitions:** `_agents/validation-patterns.json`
- **Documentation:** `_agents/validation-readme.md`

**📋 Quality Standards**
- **Conservative Estimates:** No speculative metrics or invented data
- **Source Attribution:** All insights traceable to original interviews
- **Evidence-Based Analysis:** Conclusions supported by research data
- **Template Compliance:** Consistent formatting and structure adherence

### Continuous Improvement
- **Improvement Tracking:** `_agents/improvements.md` - System enhancement documentation
- **Template Refinement:** Regular updates based on usage patterns
- **Agent Optimization:** Enhanced instructions based on output quality
- **Process Evolution:** Adaptation for new research methodologies

---

## Success Metrics

### Process Efficiency
- **Time Reduction:** Complete strategic analysis in 5-8 hours vs 2-3 weeks
- **Quality Improvement:** Systematic insight capture with 30-50 granular pain points vs ad-hoc analysis
- **Completeness:** End-to-end problem → solution → delivery package (3 complete phases)
- **Stakeholder Readiness:** Professional deliverables requiring minimal editing
- **Implementation Readiness:** Confluence and Jira structures ready for direct import

### Business Impact
- **Decision Acceleration:** Executive-ready materials for immediate review across all phases
- **Strategic Alignment:** Clear traceability from atomic pain points through solutions to delivery
- **Implementation Focus:** Actionable MVP scope with validation plans and success metrics
- **Risk Mitigation:** Conservative estimates with transparent assumptions and source attribution
- **Team Productivity:** Delivery-ready structures eliminate weeks of manual documentation work

---

## Advanced Usage

### Workflow Customization
- **Agent Instructions:** Modify agent files in `_agents/` for specific domains
- **Template Customization:** Update templates in `_output-structure/` for brand/format requirements
- **Process Adaptation:** Adjust workflow rules for different analysis types

### Integration Options
- **LLM Integration:** Compatible with GPT-4, Claude, or custom models
- **Automation:** Orchestrate via API for continuous analysis workflows
- **Export Formats:** Templates designed for Figma, presentation tools, and strategic planning systems

### Quality Control
- **Automated Validation:** Guardrail validator and Python scripts ensure output quality
- **Source Attribution:** All insights traceable to original interviews
- **Conservative Estimates:** No speculative metrics or invented data  
- **Validation Gates:** Each agent includes completion and quality criteria
- **Pattern Recognition:** JSON-defined validation patterns for consistency
- **Change Tracking:** Version control for iterative analysis refinement

---

## Maintenance and Updates

### Regular Updates
- **Template Refinement:** Improve based on usage patterns and feedback
- **Agent Optimization:** Enhance instructions based on output quality
- **Process Evolution:** Adapt workflow for new research methodologies

### Troubleshooting  
- **Incomplete Analysis:** Verify source material quality and completeness
- **Quality Issues:** Run validation scripts and check guardrail compliance
- **Process Breaks:** Validate sequential execution and input requirements
- **Validation Failures:** Review `validation-patterns.json` and agent dependencies
- **Template Inconsistencies:** Use guardrail validator for compliance checking

### Support
- **Documentation:** All agents and templates include detailed instructions
- **Agent-Specific Guides:** 
  - Problem Space: `_agents/problem-space/README.md`
  - Solution Space: `_agents/solution-space/README.md`
  - Delivery Space: `_agents/delivery-space/README.md`
- **Examples:** Sample outputs demonstrate expected quality and format
- **Iteration:** System designed for continuous improvement and refinement

---

## Complete Agent Overview

### 📊 All Agents at a Glance

**Phase 0: Documentation Setup**
- **Agent 0:** Product & Service Specialist

**Phase 1: Problem Analysis (7 agents)**
- **Agent 1:** Qualitative Research Specialist
- **Agent 2A:** Pain Point Granularization Specialist ⚡
- **Agent 2B:** Pain Point Clustering Specialist ⚡
- **Agent 3:** As-Is Journey Mapper
- **Agent 4:** Journey Consolidation Specialist
- **Agent 5:** Strategic Report Generator
- **Agent 6:** Visual Journey Designer (Problem Space)

**Phase 2: Solution Development (5 agents)**
- **Agent 6:** Solution Ideation Specialist (Solution Space)
- **Agent 7:** Experience Design Specialist
- **Agent 8:** Solution Concept Specialist
- **Agent 9:** Product Prioritization Specialist
- **Agent 10:** Product Communication Specialist

**Phase 3: Delivery Preparation (2 agents)**
- **Agent 11:** Confluence Documentation Specialist
- **Agent 12:** Jira Project Setup Specialist

**Total:** 15 specialized agents across 3 phases

---

**This system enables product teams to think strategically without sacrificing speed, providing the thorough analysis that drives successful product decisions within modern development cycles. From initial research through strategic analysis to delivery-ready implementation structures, the system delivers comprehensive, validated, and actionable insights in hours instead of weeks. Enhanced with automated quality validation, 2-phase pain point analysis (granularization + clustering), and direct integration with Confluence and Jira, it ensures reliable, consistent, and immediately implementable results every time.**