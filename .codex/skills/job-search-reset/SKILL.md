---
name: job-search-reset
description: Reset local profile, documents, generated applications, or search state. Use only for explicit reset/wipe/clear requests or /reset.
---

# Job Search Reset

Use this skill only for explicit reset requests.

## Workflow

1. Read `AGENTS.md` and `.claude/commands/reset.md`.
2. Confirm the requested reset scope:
   - profile
   - documents
   - generated applications
   - scraper/search state
   - all
3. Preview the files or folders that would be changed or removed.
4. Ask for explicit confirmation before destructive changes.
5. Prefer moving files to a timestamped backup folder over permanent deletion unless the user requests deletion.

## Rules

- Never reset anything from an ambiguous request.
- Never delete source documents or profile data without explicit confirmation.
- Do not touch unrelated repositories or parent folders.
