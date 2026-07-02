---
name: phase-1-problem
description: Run Phase 1 (Problem Discovery) of the product discovery pipeline — interview analysis through strategic reports, ending at gate G1.
disable-model-invocation: true
argument-hint: "[step-id to resume from, optional]"
---

# Phase 1 — Problem Discovery

Execute Phase 1 of the pipeline defined in `pipeline.yaml` (the canonical source — read its `phases[id="1"]` block now; do not rely on a memorized step list).

## Preconditions

1. Run `python3 scripts/validate-gate.py status` and show the user where the pipeline stands.
2. Verify inputs exist: `0-documentation/0a-projectdocs/context.md` is non-empty and `0-documentation/0b-Interviews/` has at least one interview. If not, stop and ask the user to provide them.

## Execution

For each step of phase 1 **in manifest order** (skip steps whose outputs already exist, unless the user passed a step-id to redo — `$ARGUMENTS`):

1. Launch the subagent named in the step's `role` field (they live in `.claude/agents/`), with a short task prompt: the step id, its input paths, and its output contract from the manifest. One step at a time — each step consumes the previous step's files.
2. When the subagent returns, verify its output contract is satisfied (files exist, non-empty). If not, re-run the subagent with the specific gap named. Do not proceed to the next step on a broken contract.
3. Steps with independent inputs (e.g., one analysis per interview inside `interview-analysis`) may be parallelized across multiple subagent invocations; steps themselves are sequential.

## Gate G1

When all steps are done:

1. Run `python3 scripts/validate-gate.py check 1`.
2. If guardrail violations are reported, have the owning subagent rewrite the flagged file (cite sources, qualitative language) and re-check.
3. When checks pass, summarize the deliverables for the user and instruct them to review and run `python3 scripts/validate-gate.py approve 1`. **Never run `approve` yourself — the approval is the human's.**
