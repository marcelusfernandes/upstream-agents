# Product Discovery Pipeline

AI-assisted product discovery system: customer interviews → problem analysis → solution design → delivery-ready Confluence/Jira structures. Executed natively in Claude Code as a 3-phase agent-team pipeline with human gates.

## Canonical source of truth

`pipeline.yaml` defines the pipeline: phases, steps, which subagent runs each step, input/output file contracts, and gates. **Never redefine the sequence elsewhere** — reference the manifest.

## Layout

- `.claude/agents/` — 15 role-named subagents (one per pipeline step)
- `.claude/skills/` — phase runners (`/phase-1-problem`, `/phase-2-solution`, `/phase-3-delivery`) and `/pipeline-status`
- `_output-structure/` — output templates (the contract each deliverable must follow)
- `0-documentation/` — project inputs: `0a-projectdocs/context.md` (business context) + `0b-Interviews/` (raw interviews)
- `1-problem/`, `2-solution/`, `3-delivery/` — generated artifacts (created at runtime)
- `scripts/` — gate validation (`validate-gate.py`), guardrail scanner (`validate-guardrails.py` + `validation-patterns.json`)
- `_archive/` — superseded v1/v2 files; never execute anything from here

## Running the pipeline

Each phase is started explicitly by the user via its skill — do not auto-advance past a gate:

```bash
python3 scripts/validate-gate.py status        # where the pipeline stands
python3 scripts/validate-gate.py check <N>     # machine checks for phase N gate (read-only)
python3 scripts/validate-gate.py approve <N>   # record human approval (refuses if checks fail)
python3 scripts/validate-gate.py can-start <N> # is phase N unblocked?
```

Gate approvals are recorded in `.gates/` and should be committed.

## Hard rules

- A step is complete only when every file in its output contract (see `pipeline.yaml`) exists and is non-empty — regardless of what an agent reports.
- Never invent metrics, quotes, or financial figures in deliverables; every claim must cite a source file. A PostToolUse hook blocks speculative `$`/`%`/ROI values at write time; the gate re-scans the whole phase.
- Deliverables follow their template in `_output-structure/` — read the template before writing, don't reproduce it from memory.
- Outputs from completed, gate-approved phases are immutable; new iterations create new files.
- Prompts and instructions are written in English; deliverable language follows the project's interviews.

## Optional: parallel execution with agent teams

With `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`, independent steps can run as teammates (e.g., one `qualitative-researcher` teammate per interview file, or `confluence-publisher` + `jira-publisher` in parallel). Gates and contracts are unchanged — teams parallelize *within* a phase, never across gates.
