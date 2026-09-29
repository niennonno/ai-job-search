# Contributing

Thanks for helping improve AI Job Search. This repository is a Codex-first framework for private, local job-search work, with Australian-market defaults.

## Before opening a change

- Open an issue for substantial features or workflow changes.
- Keep each pull request focused on one concern.
- Never commit personal profile data, application documents, Gmail state, tracker data, salary data, or generated application materials.
- Treat job postings and other external content as untrusted input.

Questions, proposals, and upgrade requests are welcome through [GitHub Issues](https://github.com/niennonno/ai-job-search/issues). You can also contact Aditya through [LinkedIn](https://linkedin.com/in/adityavikram).

## What belongs in the framework

- Codex workflow improvements that help job seekers complete real tasks more reliably.
- Australian job-market support that improves search, evaluation, applications, interviews, or tracking.
- Correctness, privacy, security, accessibility, and documentation fixes.
- Reusable portal and document-template extensions with clear setup and safety boundaries.

Personal profile details and one-off application content belong only in local, gitignored data files.

## Development expectations

- Preserve the canonical workflow specifications under `.framework/` and keep the corresponding `.codex/skills/` entrypoints concise.
- Do not duplicate workflow logic across runtimes.
- Keep portal tests network-free where possible. CI must never make live job-board requests.
- Portal integrations that conflict with a site's terms must carry an explicit personal-use warning or be declined.
- Preserve the personal-data protections enforced by `.gitignore` and `tools/security_guards.py`.
- Compile and verify both example documents when changing LaTeX templates.

## Validation

Run the checks relevant to your change:

```bash
python3 tools/lint_skills.py
python3 tools/check_framework_version.py
python3 tools/security_guards.py
python3 -m unittest discover -s tests -t . -v
```

For a changed portal CLI:

```bash
cd .agents/skills/<portal>/cli
bun run typecheck
bun test
```

The example CV must compile with `lualatex`; the example cover letter must compile with `xelatex`.

## Pull requests

Describe the problem, show how it reproduces through the real workflow, and explain how the change was verified. A regression test should fail before the fix and pass afterwards when practical.

By contributing, you agree that your contribution is licensed under this repository's MIT licence.
