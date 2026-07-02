# Product Discovery Pipeline — Claude Code Agent Team

An AI-powered product discovery system that turns customer interviews into delivery-ready implementation structures — problem analysis, solution design, and Confluence/Jira packages — in hours instead of weeks, with human validation at every phase gate.

Built natively for **Claude Code**: 15 role-named subagents, 4 skills, machine-verifiable gates, and a write-time guardrail hook. The pipeline definition lives in a single manifest: **`pipeline.yaml`**.

---

## How it works

```
0-documentation/  (business context + raw interviews)
        │
┌───────▼──────── PHASE 1 · Problem Discovery ─────────────────────────┐
│ context-setup → interview-analysis → painpoint-granularization       │
│   → painpoint-clustering → asis-journey-mapping                      │
│   → journey-consolidation → strategic-report → visual-journey-spec   │
└───────┬───────────────────────────────────────────────────────────────┘
   ═ GATE G1 ═  outputs exist + guardrail scan + human approval
┌───────▼──────── PHASE 2 · Solution Development ──────────────────────┐
│ solution-ideation → experience-design → solution-concepts            │
│   → mvp-prioritization → product-communication                       │
└───────┬───────────────────────────────────────────────────────────────┘
   ═ GATE G2 ═  outputs exist + guardrail scan + human approval
┌───────▼──────── PHASE 3 · Delivery Preparation ──────────────────────┐
│ confluence-structure → jira-structure                                 │
└───────┬───────────────────────────────────────────────────────────────┘
   ═ GATE G3 ═  import-ready Confluence + Jira packages
```

Each step is executed by a dedicated subagent with an explicit file contract (inputs → outputs). A phase is only complete when its gate passes machine checks **and** a human approves. The next phase refuses to start without the approved gate.

## Quick start (Claude Code)

1. **Provide inputs:**
   - `0-documentation/0a-projectdocs/context.md` — business context and objectives
   - `0-documentation/0b-Interviews/` — raw interview files
2. **Run each phase** (user-invoked skills; the model never auto-advances past a gate):
   ```
   /phase-1-problem
   /phase-2-solution
   /phase-3-delivery
   ```
3. **Approve each gate** after reviewing the deliverables:
   ```bash
   python3 scripts/validate-gate.py check 1     # machine checks (read-only)
   python3 scripts/validate-gate.py approve 1   # record your approval
   ```
4. **Check progress anytime:** `/pipeline-status` or `python3 scripts/validate-gate.py status`

## The agent team

All subagents live in `.claude/agents/` (lean, ≤120-line prompts; templates loaded just-in-time from `_output-structure/`).

| Phase | Subagent | Produces |
|---|---|---|
| 1 | `product-context-specialist` | `0-documentation/broad-context.md` + directory scaffold |
| 1 | `qualitative-researcher` | one structured analysis per interview (`1a-interview-analysis/`) |
| 1 | `painpoint-decomposer` | 30–50 atomic pain points (`1b0-granular/`) |
| 1 | `painpoint-synthesizer` | 4–6 thematic clusters + consolidated mapping (`1b-painpoints/`) |
| 1 | `journey-mapper` | per-stage As-Is journey maps (`1c2-asis-breakdown/`) |
| 1 | `journey-consolidator` | unified As-Is journey (`asis-journey.md`) |
| 1 | `strategic-reporter` | executive pain + problem reports (`1d-problem-output/`) |
| 1 | `visual-journey-designer` | Figma-Make-ready visual spec (`journey-output.md`) |
| 2 | `opportunity-strategist` | prioritized opportunities, RICE matrix, roadmap (`2a-opportunities/`) |
| 2 | `experience-designer` | To-Be journey + experience improvements (`2b-tobe_journey/`) |
| 2 | `concept-specialist` | solution concepts + feasibility (conceptual only) (`2c-priotization/`) |
| 2 | `mvp-scoper` | MVP scope, feature prioritization, validation plan (`2d-roadmap/`) |
| 2 | `product-communicator` | product brief, roadmap, stakeholder comms (`2e-solution-output/`) |
| 3 | `confluence-publisher` | import-ready Confluence hierarchy (`3-delivery/confluence/`) |
| 3 | `jira-publisher` | import-ready Jira Initiative/Epics/Stories (`3-delivery/jira/`) |

## Quality enforcement (code first, prose never)

- **Write-time hook** (`.claude/hooks/guardrail-check.py`, wired via `.claude/settings.json`): every Write/Edit to a deliverable is scanned for invented financial/percentage claims; violations block with exit 2 and the agent self-corrects immediately.
- **Phase gates** (`scripts/validate-gate.py`): read-only verification that every output contract in `pipeline.yaml` is satisfied plus a full guardrail re-scan; human approval is recorded in `.gates/` (commit it for the audit trail) and required before the next phase.
- **Judgment guardrails** (invented quotes, source attribution, tone) are explicitly the human reviewer's checklist at each gate — not pretend-enforcement prose.
- **Optional auto-fix**: `python3 scripts/validate-guardrails.py <dir>` rewrites speculative metrics into conservative language (never run by gates; on demand only).

## Repository layout

```
├── CLAUDE.md                 # project memory (facts + hard rules)
├── pipeline.yaml             # ★ canonical pipeline definition
├── .claude/
│   ├── agents/               # 15 subagents (one per step)
│   ├── skills/               # /phase-1-problem, /phase-2-solution, /phase-3-delivery, /pipeline-status
│   ├── hooks/                # write-time guardrail check
│   └── settings.json         # hook wiring + permissions
├── scripts/                  # validate-gate.py, validate-guardrails.py, validation-patterns.json
├── _output-structure/        # deliverable templates (problem/solution/delivery)
├── 0-documentation/          # your inputs
├── 1-problem/ 2-solution/ 3-delivery/   # generated at runtime
└── _archive/                 # superseded v1/v2 systems (Cursor rules, numbered agents)
```

## Optional: parallelism with agent teams

With the experimental agent-teams feature enabled (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`), independent work inside a phase can run as parallel teammates — e.g., one `qualitative-researcher` per interview, or `confluence-publisher` and `jira-publisher` side by side. Contracts and gates are unchanged: teams parallelize *within* a phase, never across gates.

## Docs

- `CLAUDE.md` — project rules Claude Code loads every session
- `WORKFLOW-OTIMIZADO.md` — design rationale, execution guide, migration history
- `AVALIACAO.md` — the system evaluation that motivated this architecture
- `_archive/README.md` — what was retired and why
