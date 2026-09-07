---
name: job-search-scrape
description: Search and rank Australian jobs. Use for finding roles, scraping, lists, dedupe, seen_jobs updates, or /scrape.
---

# Job Search Scrape

Use this skill to find and triage Australian job postings.

## Token-Efficient Workflow

1. Read `AGENTS.md` and `.codex/context/job-application-brief.md`.
2. Load only the needed state files:
   - `job_scraper/seen_jobs.json`
   - `job_search_tracker.csv`
   - `job_search_comprehensive_*.md` only when the user asks to consolidate or show the full list.
3. Search Australia-first sources: SEEK, LinkedIn Australia, Workforce Australia, APS Jobs, and target-company ATS pages such as Greenhouse, Lever, Workday, SmartRecruiters, Ashby, and Teamtailor.
4. Use `.agents/skills/linkedin-search/SKILL.md` or `.agents/skills/freehire-search/SKILL.md` only when those CLI searches are actually needed. Do not read archived Danish portal examples unless the user asks for Denmark.
5. Deduplicate against `seen_jobs.json`, `job_search_tracker.csv`, user skip decisions, and known closed roles.
6. Present a compact ranked table: status, platform, role, company, location, fit, strength, gap, link.
7. Update `seen_jobs.json` after fetching postings. Switch to `job-search-apply` for a selected role.

## Rules

- Respect each job board's access rules and keep volume low.
- Do not fabricate or infer postings that were not actually found.
- Do not submit applications from this skill.
- Flag salary/superannuation, hybrid cadence, sponsorship, security checks, travel, FIFO, and relocation early.
