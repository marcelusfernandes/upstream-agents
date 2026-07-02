#!/usr/bin/env python3
"""
validate-gate.py — Gates de validação verificáveis por máquina para o pipeline.

Lê o manifesto `pipeline.yaml` (fonte única de verdade) e valida os contratos
de saída de cada passo/fase. Diferente de `scripts/validate-guardrails.py`,
este script NUNCA modifica arquivos: gates são read-only por definição.

Uso:
    python3 scripts/validate-gate.py status              # estado de todo o pipeline
    python3 scripts/validate-gate.py check <fase>        # checagens de máquina do gate
    python3 scripts/validate-gate.py approve <fase>      # registra aprovação humana
    python3 scripts/validate-gate.py can-start <fase>    # verifica pré-requisitos da fase

Exit codes: 0 = ok, 1 = falha de validação, 2 = erro de uso/configuração.
"""

import glob as globmod
import json
import os
import re
import sys
from datetime import datetime, timezone

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(REPO_ROOT, "pipeline.yaml")
GATES_DIR = os.path.join(REPO_ROOT, ".gates")


def load_manifest():
    try:
        import yaml
    except ImportError:
        print("Erro: PyYAML não instalado. Rode: pip install pyyaml", file=sys.stderr)
        sys.exit(2)
    with open(MANIFEST, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def resolve_glob(pattern):
    """Expande um padrão relativo à raiz do repo, ignorando lixo de SO."""
    matches = globmod.glob(os.path.join(REPO_ROOT, pattern), recursive=True)
    return [m for m in matches if os.path.basename(m) != ".DS_Store"]


def check_paths(specs, kind):
    """Valida uma lista de specs {path, min_files?}. Retorna lista de erros."""
    errors = []
    for spec in specs or []:
        path = spec["path"] if isinstance(spec, dict) else spec
        min_files = spec.get("min_files", 1) if isinstance(spec, dict) else 1
        if any(ch in path for ch in "*?["):
            found = resolve_glob(path)
            if len(found) < min_files:
                errors.append(
                    f"{kind} '{path}': esperado >= {min_files} arquivo(s), encontrado {len(found)}"
                )
        else:
            full = os.path.join(REPO_ROOT, path)
            if not os.path.isfile(full):
                errors.append(f"{kind} '{path}': arquivo não existe")
            elif os.path.getsize(full) == 0:
                errors.append(f"{kind} '{path}': arquivo existe mas está vazio")
    return errors


def step_status(step, phase_steps):
    """'done' se todos os outputs existem, 'ready' se inputs/requires ok, senão 'blocked'."""
    if not check_paths(step.get("outputs"), "output"):
        return "done"
    if check_paths(step.get("inputs"), "input"):
        return "blocked"
    by_id = {s["id"]: s for s in phase_steps}
    for req in step.get("requires", []):
        dep = by_id.get(req)
        if dep and check_paths(dep.get("outputs"), "output"):
            return "blocked"
    return "ready"


def scan_guardrails(manifest, scan_dirs):
    """Scan READ-ONLY dos padrões de guardrail em todos os .md dos diretórios."""
    patterns_file = os.path.join(REPO_ROOT, manifest["guardrails"]["patterns"])
    with open(patterns_file, "r", encoding="utf-8") as f:
        patterns = json.load(f)
    scan_patterns = patterns["validation_checks"]["scan_patterns"]

    violations = []
    for d in scan_dirs:
        for md in resolve_glob(os.path.join(d, "**", "*.md")):
            with open(md, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
            for pat in scan_patterns:
                for match in re.findall(pat, content):
                    rel = os.path.relpath(md, REPO_ROOT)
                    violations.append(f"{rel}: '{match}' (padrão: {pat})")
    return violations


def find_phase(manifest, phase_id):
    for phase in manifest["phases"]:
        if str(phase["id"]) == str(phase_id):
            return phase
    print(f"Erro: fase '{phase_id}' não existe no pipeline.yaml", file=sys.stderr)
    sys.exit(2)


def gate_marker(gate_id):
    return os.path.join(GATES_DIR, f"{gate_id}.approved")


def cmd_check(manifest, phase_id, quiet=False):
    phase = find_phase(manifest, phase_id)
    errors = []
    for step in phase["steps"]:
        errs = check_paths(step.get("outputs"), "output")
        if errs:
            errors.extend(f"[{step['id']}] {e}" for e in errs)

    gate = phase.get("gate", {})
    if "guardrails_scan" in gate.get("checks", []):
        violations = scan_guardrails(manifest, gate.get("scan_dirs", []))
        errors.extend(f"[guardrails] {v}" for v in violations)

    if errors:
        if not quiet:
            print(f"❌ Gate {gate.get('id', phase_id)} REPROVADO — {len(errors)} problema(s):")
            for e in errors:
                print(f"   - {e}")
            print("\nCorrija os problemas acima. Para auto-fix de métricas especulativas:")
            print(f"   python3 {manifest['guardrails']['scanner']} <diretório>")
        return 1
    if not quiet:
        print(f"✅ Gate {gate.get('id', phase_id)}: todas as checagens de máquina passaram.")
        if gate.get("human_approval"):
            approved = os.path.isfile(gate_marker(gate["id"]))
            if approved:
                print(f"✅ Aprovação humana registrada ({gate_marker(gate['id'])}).")
            else:
                print("⏳ Falta aprovação humana. Revise os outputs e rode:")
                print(f"   python3 scripts/validate-gate.py approve {phase_id}")
    return 0


def cmd_approve(manifest, phase_id):
    phase = find_phase(manifest, phase_id)
    if cmd_check(manifest, phase_id, quiet=True) != 0:
        print("❌ Não é possível aprovar: as checagens de máquina falharam.")
        print(f"   Rode: python3 scripts/validate-gate.py check {phase_id}")
        return 1
    gate = phase["gate"]
    os.makedirs(GATES_DIR, exist_ok=True)
    marker = gate_marker(gate["id"])
    with open(marker, "w", encoding="utf-8") as f:
        f.write(
            f"gate: {gate['id']}\nphase: {phase_id}\n"
            f"approved_at: {datetime.now(timezone.utc).isoformat()}\n"
            f"approved_by: {os.environ.get('USER', 'unknown')}\n"
        )
    print(f"✅ Gate {gate['id']} aprovado. Registro: {os.path.relpath(marker, REPO_ROOT)}")
    print("   Faça commit do marcador para manter a trilha de auditoria.")
    return 0


def cmd_can_start(manifest, phase_id):
    phase = find_phase(manifest, phase_id)
    required = phase.get("requires_gate")
    if required and not os.path.isfile(gate_marker(required)):
        print(f"❌ Fase {phase_id} bloqueada: gate {required} ainda não foi aprovado.")
        return 1
    print(f"✅ Fase {phase_id} pode iniciar.")
    return 0


def cmd_status(manifest):
    print(f"Pipeline v{manifest['version']} — status\n")
    for phase in manifest["phases"]:
        gate = phase.get("gate", {})
        approved = os.path.isfile(gate_marker(gate.get("id", "")))
        gate_state = "aprovado ✅" if approved else "pendente ⏳"
        print(f"Fase {phase['id']} — {phase['name']} (gate {gate.get('id')}: {gate_state})")
        for step in phase["steps"]:
            icon = {"done": "✅", "ready": "▶️ ", "blocked": "⛔"}[step_status(step, phase["steps"])]
            print(f"  {icon} {step['id']}  ({step['role']})")
        print()
    return 0


def main():
    manifest = load_manifest()
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    cmd = args[0]
    if cmd == "status":
        return cmd_status(manifest)
    if cmd in ("check", "approve", "can-start"):
        if len(args) != 2:
            print(f"Uso: validate-gate.py {cmd} <fase>", file=sys.stderr)
            return 2
        return {"check": cmd_check, "approve": cmd_approve, "can-start": cmd_can_start}[cmd](
            manifest, args[1]
        )
    print(f"Comando desconhecido: {cmd}", file=sys.stderr)
    print(__doc__)
    return 2


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:
        sys.exit(0)
