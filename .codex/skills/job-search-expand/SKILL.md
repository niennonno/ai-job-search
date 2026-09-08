---
name: job-search-expand
description: Enrich the candidate profile from documents and public linked sources. Use for /expand, competency discovery, GitHub/profile enrichment, course skills, and profile evidence expansion.
---

# Job Search Expand

Use this skill to add missing competencies from source documents and public profile links.

## Workflow

1. Read `AGENTS.md`, `CODEX.md`, `.codex/context/job-application-brief.md`, and `.codex/context/evidence-bank.csv`.
2. Read `.claude/commands/expand.md`; it is the canonical workflow for source order, enrichment, deduplication, and profile update rules.
3. Scan only the relevant local source folders or public profile links needed for the requested enrichment.
4. Propose additions before writing when a discovered fact could conflict with existing profile facts.
5. When approved, update `CODEX.md`, `.claude/skills/job-application-assistant/01-candidate-profile.md`, `.codex/context/job-application-brief.md`, and `.codex/context/evidence-bank.csv` as needed.

## Rules

- Additive only unless the user explicitly asks to correct existing facts.
- Capture source labels for new facts.
- Do not invent competencies from vague affiliations or empty repositories.
- Keep personal profile data local unless the user explicitly asks to commit or sync it.
