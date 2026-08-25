---
name: job-search-setup
description: Build or update the local Australian AI job-search candidate profile in this repo. Use when the user asks to set up the job search workspace, import a CV or resume, read the documents folder, update search preferences, fill profile files, or run the equivalent of /setup.
---

# Job Search Setup

Use this skill inside the `ai-job-search` workspace to populate or update the candidate profile.

## Workflow

1. Read `AGENTS.md`, `CLAUDE.md`, and `.claude/commands/setup.md`.
2. Follow `.claude/commands/setup.md` as the canonical procedure, translating Claude-specific tool names into Codex equivalents:
   - `Glob` -> file listing/search.
   - `Read` -> file read.
   - `Edit`/`Write` -> targeted file edits.
   - `AskUserQuestion` -> concise user question.
3. Read existing profile files before extracting new material:
   - `.claude/skills/job-application-assistant/01-candidate-profile.md`
   - `.claude/skills/job-application-assistant/02-behavioral-profile.md`
   - `.claude/skills/job-application-assistant/03-writing-style.md`
   - `.claude/skills/job-application-assistant/04-job-evaluation.md`
   - `.claude/skills/job-application-assistant/05-cv-templates.md`
   - `.claude/skills/job-application-assistant/06-cover-letter-templates.md`
   - `.claude/skills/job-application-assistant/07-interview-prep.md`
4. Prefer additive, source-labeled updates. Present conflicts to the user before editing.
5. During search setup, default to Australian sources: SEEK, LinkedIn Australia, Workforce Australia, APS Jobs, and target-company career pages. Ask which industries, cities, states, remote constraints, and specialist boards matter.
6. Capture Australian logistics: work rights, visa constraints if any, salary expectations, superannuation expectations, hybrid cadence, travel, FIFO/rostered work, security clearance, and relocation boundaries.
7. Preserve framework rules and templates. Only change personal profile content or search preferences unless the user asks for framework changes.

## Safety

- Do not invent profile facts.
- Do not commit or publish generated profile files.
- Keep extracted personal data inside this workspace.
