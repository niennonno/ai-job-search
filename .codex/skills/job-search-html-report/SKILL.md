---
name: job-search-html-report
description: Generate an offline job-search dashboard. Use for /html-report, application tracker reports, charts, funnel summaries, and self-contained HTML dashboards.
---

# Job Search HTML Report

Use this skill to generate a local HTML dashboard from the tracker and application archives.

## Workflow

1. Read `AGENTS.md`.
2. Read `.claude/commands/html-report.md`; it is the canonical workflow for arguments, status buckets, funnel math, escaping, layout, and output path.
3. Parse `job_search_tracker.csv` and `documents/applications/*/outcome.md` with structured parsers.
4. Write the report to `reports/application-dashboard.html` by default, or to the user-provided path.

## Rules

- Generate a single self-contained HTML file with inline CSS, inline JS, and no external dependencies.
- HTML-escape every value from CSV or archive files before interpolation.
- This skill reads and renders; it does not update the tracker or application history.
