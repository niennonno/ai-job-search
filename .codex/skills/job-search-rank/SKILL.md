---
name: job-search-rank
description: Rank scraped job postings into a shortlist. Use for /rank, ranking new jobs, scoring seen_jobs entries, shortlists, and batch triage before applying.
---

# Job Search Rank

Use this skill to score scraped jobs before deciding which applications deserve full `/apply` effort.

## Workflow

1. Read `AGENTS.md` and `.codex/context/job-application-brief.md`.
2. Read `.claude/commands/rank.md`; it is the canonical workflow for candidate selection, status updates, scoring dimensions, expiry handling, and output format.
3. Use `tools/rank_state.py` for selecting candidates and writing rank results. Do not load the full `job_scraper/seen_jobs.json` into context unless debugging a specific row.
4. Treat rankings as triage only. A later application run must still perform the deeper fit evaluation and company research.

## Rules

- Score only from fetched posting content and grounded profile facts.
- Mark a posting expired only after following the fetch fallback rules in `.claude/skills/job-application-assistant/09-web-research.md`.
- Do not apply, draft documents, or update application history from this skill.
