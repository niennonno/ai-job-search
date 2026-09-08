---
name: job-search-add-portal
description: Create a market-specific job portal search CLI skill. Use for /add-portal, adding SEEK or other job boards, portal CLI scaffolding, and custom job search integrations.
---

# Job Search Add Portal

Use this skill to create a new job-board search skill under `.agents/skills/`.

## Workflow

1. Read `AGENTS.md`.
2. Read `.claude/commands/add-portal.md`; it is the canonical workflow for portal research, scaffolding, CLI contract, tests, and registration.
3. Use `.agents/skills/linkedin-search/` or `.agents/skills/freehire-search/` as the active reference implementation.
4. Treat `.agents/archive/skills/*` as historical examples only; copy from them only when the user explicitly wants that market and after reviewing them.
5. Test-run a live query before registering a generated portal skill.

## Rules

- Respect robots.txt, public access limits, and portal terms.
- Never hardcode credentials; use environment variables when a credential is required.
- Keep generated portal skills scoped to the user's fork unless the user asks for upstream preparation.
