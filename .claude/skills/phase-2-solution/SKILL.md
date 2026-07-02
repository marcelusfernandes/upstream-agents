---
name: phase-2-solution
description: Run Phase 2 (Solution Development) of the product discovery pipeline — opportunities through product communications, ending at gate G2.
disable-model-invocation: true
argument-hint: "[step-id to resume from, optional]"
---

# Phase 2 — Solution Development

Execute Phase 2 of the pipeline defined in `pipeline.yaml` (read its `phases[id="2"]` block now; the manifest is canonical).

## Preconditions

1. Run `python3 scripts/validate-gate.py can-start 2`. If gate G1 is not approved, stop and tell the user what is missing (`check 1` output helps). Do not proceed past an unapproved gate.
2. Run `python3 scripts/validate-gate.py status` and show the user where the pipeline stands.

## Execution

For each step of phase 2 **in manifest order** (skip steps whose outputs already exist, unless the user passed a step-id to redo — `$ARGUMENTS`):

1. Launch the subagent named in the step's `role` field (`.claude/agents/`), with a short task prompt: step id, input paths, output contract from the manifest.
2. When the subagent returns, verify the output contract (files exist, non-empty). Re-run with the specific gap named if not. Never advance on a broken contract.
3. Solution deliverables stay **conceptual** — if a subagent produced technical specs or user stories, that is a contract violation (they belong to Phase 3).

## Gate G2

When all steps are done:

1. Run `python3 scripts/validate-gate.py check 2`.
2. Fix any guardrail violations via the owning subagent, then re-check.
3. When checks pass, summarize the deliverables and instruct the user to review and run `python3 scripts/validate-gate.py approve 2`. **Never run `approve` yourself.**
