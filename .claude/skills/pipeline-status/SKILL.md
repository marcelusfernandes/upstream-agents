---
name: pipeline-status
description: Report the product discovery pipeline's progress — completed steps, pending gates, and what to run next. Use when the user asks where the pipeline stands.
allowed-tools: Bash(python3 scripts/validate-gate.py *), Read
---

# Pipeline Status

1. Run `python3 scripts/validate-gate.py status`.
2. Summarize for the user: which steps are done (✅), which are ready (▶️), which are blocked (⛔), and each gate's approval state.
3. Tell them the single next action: the phase skill to run (`/phase-1-problem`, `/phase-2-solution`, `/phase-3-delivery`), the gate to approve (`python3 scripts/validate-gate.py approve <N>` after review), or the inputs to provide (`0-documentation/`).
