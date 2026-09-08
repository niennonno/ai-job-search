---
name: job-search-add-template
description: Register or switch CV and cover letter templates. Use for /add-template, custom LaTeX or Typst templates, template activation, and PDF compile instructions.
---

# Job Search Add Template

Use this skill to register, list, or activate custom CV and cover letter templates.

## Workflow

1. Read `AGENTS.md`.
2. Read `.claude/commands/add-template.md`; it is the canonical workflow for template metadata, storage, compile commands, activation blocks, and verification.
3. Inspect provided template files and infer toolchain requirements before asking the user for missing metadata.
4. Store registered templates under `templates/` and activate them through the managed blocks in the detailed CV or cover letter template guidance.

## Rules

- Verify that the template compiles before activating it.
- Do not overwrite existing templates without explicit user approval.
- Preserve page limits and PDF inspection requirements from the application workflow.
