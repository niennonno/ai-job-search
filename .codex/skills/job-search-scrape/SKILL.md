---
name: job-search-scrape
description: Search for jobs from this local ai-job-search workspace using configured portal skills and search state. Use when the user asks to find jobs, scrape jobs, search roles, rank new postings, list matches, update seen_jobs.json, or run the equivalent of /scrape.
---

# Job Search Scrape

Use this skill to find and triage job postings.

## Workflow

1. Read `AGENTS.md` and `.claude/skills/job-scraper/SKILL.md`.
2. Load state:
   - `job_scraper/seen_jobs.json`
   - `job_search_tracker.csv`
   - `.claude/skills/job-scraper/search-queries.md`, if present.
3. Use Australia-first sources by default: SEEK, LinkedIn Australia, Workforce Australia, APS Jobs, and company ATS pages such as Greenhouse, Lever, Workday, SmartRecruiters, and Ashby.
4. Use `.agents/skills/linkedin-search` when a CLI-based search is useful. Treat the Danish portal skills as legacy examples unless the user explicitly asks for Denmark.
5. For each portal skill used, read its `SKILL.md` and run its CLI according to that file.
6. Deduplicate against both `seen_jobs.json` and `job_search_tracker.csv`.
7. Present only open, real postings with title, company, location, URL, deadline if available, and quick fit.
8. Update `seen_jobs.json` with all fetched postings.
9. If the user selects a job for a detailed evaluation, switch to `job-search-apply`.

## Rules

- Respect each job board's access rules and terms.
- Keep volume low for personal-use sources.
- Do not fabricate or infer postings that were not actually found.
- Do not submit applications.
- Flag Australian logistics early: work rights, baseline salary/superannuation, hybrid cadence, interstate time zone, FIFO roster, or relocation.
