---
name: job-search-setup
description: Build or update the candidate profile. Use for setup, CV/resume import, document reads, preferences, profile files, or /setup.
---

# Job Search Setup

Use this skill to populate or update the candidate profile.

## Token-Efficient Workflow

1. Read `AGENTS.md`, `CODEX.md`, `.codex/context/job-application-brief.md`, and `.codex/context/evidence-bank.csv`.
2. Inspect only newly supplied documents or the specific profile sections the user wants changed.
3. Update `CODEX.md`, `.claude/skills/job-application-assistant/01-candidate-profile.md`, `.codex/context/job-application-brief.md`, and `.codex/context/evidence-bank.csv` when candidate facts, proof points, or preferences change.
4. Read `.claude/commands/setup.md` only for a full re-import, conflict resolution, or when rebuilding every profile file from source documents.
5. Capture source labels for new facts. Ask before overwriting conflicting facts.

## Safety

- Do not invent profile facts.
- Keep personal data inside this workspace.
- Do not publish, commit, or sync generated profile files unless explicitly requested.
