# Archive

This directory contains files that were **superseded** by newer versions of the agent system. They are kept for historical reference only and are **not consumed by any agent or workflow**.

## `legacy/`

| File | Why it was archived |
|------|---------------------|
| `agent-8-communication-specialist.md` | Legacy v1 solution-space agent. Its responsibilities were absorbed by **Agent 10 (Product Communication Specialist)**; the current Agent 8 is the **Solution Concept Specialist**. It also references non-existent paths and templates (e.g., `change-management-template.md`). |
| `agent-8-communication-specialist.mdc` | `.cursor/rules/` mirror of the legacy agent above. |
| `agent-2-painpoint-analysis-specialist.md.backup` | Pre-split version of Agent 2. Replaced by **Agent 2A (Pain Point Granularization)** and **Agent 2B (Pain Point Clustering)**. |
| `agent-2-painpoint-analysis-specialist.mdc.backup` | `.cursor/rules/` mirror of the pre-split Agent 2 backup above. |
| `template-quality-assessment.md` | One-time meta-review of the template library (2025-10-16). Not a template and not referenced by any agent. |

## `agents-v2/` (archived 2026-07-02, migration to native Claude Code)

The entire v2 prompt library: the numbered agent instruction files (`problem-space/`, `solution-space/`, `delivery-space/`, 150–850 lines each) and the prose guardrail system (`GUARDRAILS-ENFORCEMENT.md`, `guardrails-police.md`, `guardrail-validator.md`, `validation-readme.md`).

Superseded by:
- **`.claude/agents/`** — 15 role-named subagents distilled from these files (methodology preserved, boilerplate and embedded templates removed)
- **`.claude/hooks/guardrail-check.py` + `scripts/validate-gate.py`** — the enforceable replacement for the guardrail prose
- **`CLAUDE.md`** — the surviving always-true rules

## `cursor-v2/` (archived 2026-07-02)

The full `.cursor/` tree (`rules/` with the `.mdc` agent mirror and orchestrator, `commands/`). It was a hand-maintained, diverged copy of `_agents/` and is replaced by the native `.claude/` configuration (skills replace the orchestrator trigger and commands). The old files remain readable as plain markdown if ever needed in Cursor.

Do not add new dependencies on anything in this directory.
