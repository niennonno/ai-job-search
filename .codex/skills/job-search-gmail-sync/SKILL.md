---
name: job-search-gmail-sync
description: Propose application status updates from Gmail. Use for /gmail-sync, job application email scanning, interview invite detection, rejection email classification, and Gmail-based tracker updates.
---

# Job Search Gmail Sync

Use this skill when the user wants to classify job-search emails and update local application history from Gmail signals.

## Workflow

1. Read `AGENTS.md`.
2. Read `.claude/commands/gmail-sync.md`; it is the canonical workflow for Gmail search, classification, proposal format, approval, and writes.
3. Use Gmail connector tools only when they are available in the current session. If not available, explain that Gmail must be connected and stop.
4. Present proposed updates as a batch with source email citations before editing `job_search_tracker.csv` or any `outcome.md`.

## Rules

- Never write email-derived status changes before user approval.
- Do not use Bash, IMAP, browser scraping, or exported mailbox files as a substitute for the Gmail connector.
- Never infer `hired` or `offer_declined` from an email; that decision belongs to the user.
- Keep emails and application history local unless the user explicitly asks otherwise.
