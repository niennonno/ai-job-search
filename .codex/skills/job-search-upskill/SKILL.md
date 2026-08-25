---
name: job-search-upskill
description: Analyze skill gaps between the candidate profile and target jobs in the local ai-job-search repo. Use when the user asks for upskilling, learning plans, gap analysis, skill heatmaps, training priorities, or the equivalent of /upskill.
---

# Job Search Upskill

Use this skill to compare the candidate profile with one posting or the tracked job market.

## Workflow

1. Read `AGENTS.md` and `.claude/skills/upskill/SKILL.md`.
2. Read profile and evaluation sources from `.claude/skills/job-application-assistant/`.
3. If the user provided a posting, parse that posting. Otherwise use tracked jobs and recent scrape results.
4. Identify recurring requirements, genuine gaps, adjacent strengths, and high-leverage learning areas.
5. Produce a prioritized learning plan with estimated effort, practical exercises, and resources.
6. Save reports under `upskill/` when the user wants a durable artifact.

## Rules

- Do not mark a skill as present unless it is supported by the profile.
- Distinguish hard requirements from nice-to-haves.
- Prefer learning actions that produce portfolio evidence or interview stories.

