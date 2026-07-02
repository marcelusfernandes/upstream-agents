---
name: phase-3-delivery
description: Run Phase 3 (Delivery Preparation) of the product discovery pipeline — import-ready Confluence and Jira structures, ending at gate G3.
disable-model-invocation: true
argument-hint: "[step-id to resume from, optional]"
---

# Phase 3 — Delivery Preparation

Execute Phase 3 of the pipeline defined in `pipeline.yaml` (read its `phases[id="3"]` block now; the manifest is canonical).

## Preconditions

1. Run `python3 scripts/validate-gate.py can-start 3`. If gate G2 is not approved, stop and tell the user what is missing. Do not proceed past an unapproved gate.
2. Run `python3 scripts/validate-gate.py status` and show the user where the pipeline stands.

## Execution

For each step of phase 3 **in manifest order** (skip steps whose outputs already exist, unless the user passed a step-id to redo — `$ARGUMENTS`):

1. Launch the subagent named in the step's `role` field (`.claude/agents/`), with a short task prompt: step id, input paths, output contract from the manifest.
2. Verify the output contract when the subagent returns; re-run with the gap named if broken.
3. Both structures must include their import guide. This phase only *prepares* import-ready files — it never pushes to live Confluence/Jira instances.

## Gate G3

When all steps are done:

1. Run `python3 scripts/validate-gate.py check 3`.
2. Fix any guardrail violations via the owning subagent, then re-check.
3. When checks pass, summarize the delivery package (Confluence hierarchy, Jira Initiative/Epics/Stories, import guides) and instruct the user to review and run `python3 scripts/validate-gate.py approve 3`. **Never run `approve` yourself.**
