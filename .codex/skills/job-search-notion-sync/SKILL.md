---
name: job-search-notion-sync
description: Publish a one-way job-search pipeline view to Notion. Use for /notion-sync, Notion job pipeline dashboards, ranked job syncing, and application status views.
---

# Job Search Notion Sync

Use this skill to publish a one-way view of ranked jobs and tracked applications into Notion.

## Workflow

1. Read `AGENTS.md`.
2. Read `.claude/commands/notion-sync.md`; it is the canonical workflow for preflight, schema, sync set, upserts, and privacy rules.
3. Use Notion connector tools only when they are available in the current session. If not available, explain that Notion must be connected and stop.
4. Build the sync set from local `job_scraper/seen_jobs.json` and `job_search_tracker.csv`; the tracker wins for application status.

## Rules

- Notion is a presentation layer only; repo files remain the system of record.
- Sync filenames only for CVs and cover letters, never document contents.
- Do not delete or archive Notion pages from this workflow.
- Do not initiate OAuth or external setup flows from the workflow; tell the user what is missing and stop cleanly.
