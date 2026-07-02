#!/usr/bin/env python3
"""PostToolUse hook: blocks speculative metrics in pipeline deliverables.

Runs after every Write/Edit. If the written file is a markdown deliverable
under an output directory, scan it against the guardrail patterns and exit 2
(stderr is fed back to the agent for immediate self-correction).
"""

import json
import os
import re
import sys

OUTPUT_DIRS = ("1-problem", "2-solution", "3-delivery")
BROAD_CONTEXT = os.path.join("0-documentation", "broad-context.md")


def main():
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0  # malformed input: never block on hook infrastructure errors

    tool_input = payload.get("tool_input") or {}
    file_path = tool_input.get("file_path") or tool_input.get("path") or ""
    if not file_path.endswith(".md"):
        return 0

    project_dir = payload.get("cwd") or os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
    rel = os.path.relpath(file_path, project_dir)
    if not (rel.startswith(OUTPUT_DIRS) or rel == BROAD_CONTEXT):
        return 0

    patterns_file = os.path.join(project_dir, "scripts", "validation-patterns.json")
    if not os.path.isfile(patterns_file):
        return 0
    with open(patterns_file, "r", encoding="utf-8") as f:
        scan_patterns = json.load(f)["validation_checks"]["scan_patterns"]

    try:
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
    except OSError:
        return 0

    violations = []
    for pat in scan_patterns:
        violations.extend(re.findall(pat, content))

    if violations:
        examples = ", ".join(repr(v) for v in violations[:5])
        print(
            f"GUARDRAIL VIOLATION in {rel}: speculative financial/percentage claims "
            f"are not allowed in deliverables ({examples}). Replace with conservative "
            "qualitative language citing the source interview/file, then rewrite the file.",
            file=sys.stderr,
        )
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
