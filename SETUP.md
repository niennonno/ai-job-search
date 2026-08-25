# Setup Guide

Step-by-step instructions for getting the AI Job Search framework running.

## 1. Prerequisites

### Codex

Open this repository in Codex. Codex reads `AGENTS.md` and uses the local skills under `.codex/skills/` as natural-language entrypoints.

### Python

Python 3.10+ is required for the salary lookup tool. Check with:

```bash
python --version
```

### Bun (optional, for LinkedIn job search)

The optional LinkedIn job search CLI is written in TypeScript and runs with Bun:

```bash
curl -fsSL https://bun.sh/install | bash
```

### LaTeX (for compiling CVs and cover letters)

Install a LaTeX distribution to compile the generated `.tex` files to PDF:

- **Windows:** [MiKTeX](https://miktex.org/download)
- **macOS:** [MacTeX](https://tug.org/mactex/)
- **Linux:** `sudo apt install texlive-full` or `sudo dnf install texlive-scheme-full`

The CV compiles with `lualatex` (pdflatex often fails on modern MiKTeX installs with `fontawesome5` font-expansion errors). The cover letter compiles with `xelatex` because `cover.cls` requires `fontspec` for its custom Lato/Raleway fonts.

## 2. Fork and clone

```bash
gh repo fork MadsLorentzen/ai-job-search --clone
cd ai-job-search
```

Or manually: fork on GitHub, then clone your fork.

## 3. Install optional job search CLI dependencies

```bash
cd .agents/skills/linkedin-search/cli && bun install && cd ../../../..
```

For `linkedin-search` the install is optional: it has zero runtime dependencies and runs with plain `bun`; `bun install` only pulls TypeScript dev types. The old Danish portal CLIs remain in `.agents/skills/` as legacy examples but are not part of the Australian default workflow.

## 4. Run the setup interview

Open this repository in Codex and say:

```text
Set up my job search profile.
```

Codex will offer setup paths based on what it finds in `documents/`:

- **Path A (recommended when populated):** Read the `documents/` folder and build the profile from source materials.
- **Path B:** Import a single CV or resume.
- **Path C:** Answer structured interview questions section by section.

Both paths produce the same result: fully populated profile files.

### What gets populated

| File | Content |
|------|---------|
| `CLAUDE.md` | Your full candidate profile |
| `01-candidate-profile.md` | Structured education, experience, skills |
| `02-behavioral-profile.md` | Behavioral assessment |
| `04-job-evaluation.md` | Personalized skill match areas and career goals |
| `05-cv-templates.md` | Profile statement templates for your background |
| `07-interview-prep.md` | STAR examples from your experience |
| `cv/Aditya_Godawat_PM.tex` | Your LaTeX CV with actual details |
| `search-queries.md` | Job search queries for job scraping |

### Re-running setup

You can update specific sections later:

```text
Update the skills section of my job search profile.
Update the experience section of my job search profile.
Update my job search preferences.
```

The `--section search` option is especially useful as your priorities evolve. It re-runs the search configuration interview and suggests role types you may not have considered based on your full profile.

## 5. Optional: Set up salary benchmarking

If you have Australian salary data (from SEEK salary insights, recruiter salary reports, Glassdoor, Levels.fyi, networking, or personal research):

1. **Option A:** Create `salary_data.json` manually in the repo root (see `tools/README_SALARY_TOOL.md` for the format)
2. **Option B:** Convert from Excel:
   ```bash
   pip install openpyxl
   python tools/convert_salary_excel.py path/to/salary-data.xlsx --source "My Salary Data 2025"
   ```

This creates `salary_data.json` which the application workflow uses for salary benchmarking. If you skip this step, salary lookup is simply omitted.

## 6. Test the workflow

Find a job posting you're interested in, then:

```text
Evaluate and apply to https://www.seek.com.au/job/12345678
```

Or paste the job description directly:

```text
Evaluate this job posting:
[paste job posting text here]
```

Codex will:
1. Evaluate the fit against your profile
2. Ask if you want to proceed
3. Draft a tailored CV and cover letter
4. Run an independent review pass on the drafts
5. Revise and present the final output

## 7. Compile your documents

Codex normally compiles and inspects generated PDFs as part of the application workflow. To compile manually:

```bash
# Compile CV
cd cv && lualatex main_<company>.tex && cd ..

# Compile cover letter
cd cover_letters && xelatex cover_<company>_<role>.tex && cd ..
```

## Troubleshooting

### "salary_data.json not found"
This is expected if you haven't set up salary benchmarking. The application workflow skips this step automatically.

### Job search CLI tools not working
Make sure Bun is installed. The Australian default workflow can use normal web searches without portal CLIs; only the optional LinkedIn CLI needs its local setup. Any job-source search requires network access.

### LaTeX compilation errors
- CV: uses `lualatex` (pdflatex often fails on modern MiKTeX with `fontawesome5` font-expansion errors; lualatex handles the same sources cleanly)
- Cover letter: uses `xelatex` (for custom fonts in `OpenFonts/fonts/`)
- Make sure your LaTeX distribution includes the `moderncv` package

### Fonts not found in cover letter
The cover letter template expects fonts in `cover_letters/OpenFonts/fonts/`. Make sure this directory exists and contains the Lato and Raleway font files.

### Stale `.claude/settings.local.json` from an older clone
Shared Claude Code permissions now live in `.claude/settings.json` (scoped to `bun run` and `python salary_lookup.py`). Earlier versions of this repo committed a broader `.claude/settings.local.json` that pre-approved `Bash(curl:*)`, `Bash(python:*)` and `Bash(bun:*)`. If you cloned before that change, git leaves the old file behind in your working copy, and its permissions still apply on top of `settings.json`. Delete it (or trim it to your own personal overrides):

```bash
rm .claude/settings.local.json
```
