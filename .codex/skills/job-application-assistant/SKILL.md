---
name: job-application-assistant
description: Core Australian job application workflow. Use for job postings, fit checks, CV/resume tailoring, cover letters, interview prep, application forms, and career positioning.
---

# Job Application Assistant

Use this skill when the user brings a specific job posting, asks for an application asset, wants interview preparation, or asks for career positioning based on the candidate profile.

## Codex Workflow

1. Read `AGENTS.md`, `.codex/context/job-application-brief.md`, and only the relevant rows from `.codex/context/evidence-bank.csv`.
2. For a full application run, unresolved template/layout issue, application forms, company research, or interview prep, read the active detailed workflow files under `.claude/skills/job-application-assistant/`.
3. Treat `.claude/skills/job-application-assistant/SKILL.md` as the canonical long-form workflow. The old copy under `.agents/archive/skills/job-application-assistant/` is historical only.
4. If the user provides a posting, evaluate fit before drafting. Continue to CV/cover letter work only when the user has asked for it or approves proceeding.
5. Derive `<company>_<role>` once using the subfolder naming rule in `documents/README.md`; use it consistently for `cv/main_<company>_<role>.tex`, `cover_letters/cover_<company>_<role>.tex`, and the application archive.
6. Ground every factual claim in `CODEX.md`, `.claude/skills/job-application-assistant/01-candidate-profile.md`, `cv/Aditya_Godawat_PM.tex`, `.codex/context/evidence-bank.csv`, or user-confirmed chat facts.

## Detailed References

- `.claude/commands/apply.md` for the full drafter-reviewer workflow, tracker row, and archive write.
- `.claude/skills/job-application-assistant/01-candidate-profile.md` for structured profile facts.
- `.claude/skills/job-application-assistant/02-behavioral-profile.md` for voice, working style, and interview positioning.
- `.claude/skills/job-application-assistant/03-writing-style.md` for tone.
- `.claude/skills/job-application-assistant/04-job-evaluation.md` for scoring, deal-breakers, and company research.
- `.claude/skills/job-application-assistant/05-cv-templates.md` for CV structure and PDF rules.
- `.claude/skills/job-application-assistant/06-cover-letter-templates.md` for cover letter structure.
- `.claude/skills/job-application-assistant/07-interview-prep.md` for STAR answers and mock interview protocol.
- `.claude/skills/job-application-assistant/08-application-forms.md` for portal free-text responses.
- `.claude/skills/job-application-assistant/09-web-research.md` for posting/company fetch fallback and claim verification.

## Rules

- Never fabricate skills, dates, achievements, credentials, tools, payment depth, domain depth, or company facts.
- Verify company-specific claims independently before using them in application materials.
- Do not auto-submit applications or upload personal files without action-time confirmation.
- Compile and visually inspect generated PDFs before delivery.
- Keep personal data local unless the user explicitly asks to publish, commit, or sync it.
