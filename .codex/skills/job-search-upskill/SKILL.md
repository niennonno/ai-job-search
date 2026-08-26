---
name: job-search-upskill
description: Analyse job-market skill gaps and learning plans. Use for upskilling, gap analysis, heatmaps, training priorities, or /upskill.
---

# Job Search Upskill

Use this skill to compare the candidate profile with one posting or the tracked job market.

## Token-Efficient Workflow

1. Read `AGENTS.md`, `.codex/context/job-application-brief.md`, and relevant rows from `.codex/context/evidence-bank.csv`.
2. If the user provided a posting, parse that posting. Otherwise use `job_search_tracker.csv` and the compact rows from `job_search_comprehensive_*.md`.
3. Identify recurring requirements, genuine gaps, adjacent strengths, and high-leverage learning areas.
4. Produce a prioritised learning plan with effort, practical exercises, and interview/portfolio evidence.
5. Read `.claude/skills/upskill/SKILL.md` only for a durable report or deeper market-gap analysis.

## Rules

- Do not mark a skill as present unless it is supported by profile facts.
- Distinguish hard requirements from nice-to-haves.
- Prefer learning actions that produce portfolio evidence or interview stories.
