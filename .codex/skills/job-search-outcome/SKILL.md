---
name: job-search-outcome
description: Record application outcomes and follow-ups. Use for /outcome, interview updates, offers, rejections, no response, stale sweeps, and application follow-up drafts.
---

# Job Search Outcome

Use this skill when the user wants to record what happened after an application, draft a follow-up, or sweep stale open applications.

## Workflow

1. Read `AGENTS.md`.
2. Read `.claude/commands/outcome.md`; it is the canonical workflow for tracker status vocabulary, archive format, follow-up limits, stale sweeps, and write rules.
3. Load only the needed rows from `job_search_tracker.csv` and the matching `documents/applications/<company>_<role>/outcome.md` archive.
4. Update the tracker and archive only after the target application and outcome are clear.

## Rules

- Never invent an outcome or impose `no_response` without the user's decision.
- Preserve submitted files in the archive by copying, not moving.
- Follow-up drafts are drafts only; do not send messages.
- Keep application history local unless the user explicitly asks to sync it elsewhere.
