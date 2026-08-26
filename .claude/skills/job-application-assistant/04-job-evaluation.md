# Job Evaluation Framework

<!-- SETUP: Skill match areas and career goals are personalized by running /setup -->

## Scoring Dimensions

Evaluate each job posting against these five dimensions:

### 1. Technical Skills Match (0-100)
How well do the required/preferred skills align with the candidate's capabilities?

| Score | Meaning |
|-------|---------|
| 80-100 | Core requirements are primary skills |
| 60-79 | Most requirements match, 1-2 gaps that are learnable |
| 40-59 | Partial match, significant upskilling needed |
| 0-39 | Fundamental mismatch |

**Strong match areas:** AI product strategy, GenAI product development, agentic workflows, LLM implementation and prompt engineering, enterprise SaaS platforms, AI-powered decisioning systems, A/B experimentation engines, product roadmap ownership, product ownership, Senior Product Owner scope, product strategy, AI/digital transformation, strategy-to-execution operating models, Agile/Scrum delivery, GTM strategy, stakeholder management.
**Moderate match areas:** Product Owner roles with narrower delivery scope, iOS architecture and Swift, mobile application development, system design, API integration, SQL working knowledge, RAG, user research and analytics, product consulting, OKR frameworks.
**Weak match areas:** Deep hands-on backend engineering, infrastructure/platform engineering, cybersecurity, data engineering implementation, formal people-management-only roles, and domains not supported by CV evidence.

### 2. Experience Match (0-100)
Does work history align with what they're looking for?

| Score | Meaning |
|-------|---------|
| 80-100 | Direct experience in the same domain and role type |
| 60-79 | Related experience, transferable skills clear |
| 40-59 | Adjacent experience, would need to make the case |
| 0-39 | Unrelated experience |

**Strong:** Senior product management, product ownership with strategic/platform scope, AI product management, GenAI strategy, product strategy, AI/digital transformation, strategy-to-execution leadership, enterprise B2B platforms, retail pricing platforms, CPG, eCommerce, financial services, healthcare AI products, experimentation platforms, mobile consumer products at scale.
**Moderate:** Product Owner roles that are mostly delivery/backlog management, solutions/product consulting, technical program leadership, platform partnerships, B2C growth/product roles.
**Entry-level:** Roles requiring direct ownership of pure sales, pure data science modelling, cloud infrastructure engineering, or regulated security-clearance delivery without product leadership scope.

### 3. Behavioral/Culture Fit (0-100)
Does the role and company culture match the behavioral profile?

| Score | Meaning |
|-------|---------|
| 80-100 | Culture strongly matches behavioral preferences |
| 60-79 | Mixed signals but mostly compatible |
| 40-59 | Some friction areas |
| 0-39 | Significant culture mismatch |

**Red flags to research:** Department disorganization, work dominated by maintenance over development, poor chemistry with leadership, culture mismatches. Check reviews, media coverage, LinkedIn connections, and network contacts for insider perspective.

### 4. Location & Logistics (Pass/Fail + Notes)
- Sydney, hybrid Sydney, or remote Australia: PASS
- Melbourne with flexible, hybrid, or non-rigid weekly office cadence: PASS with note
- Melbourne with fixed weekly office cadence: FLAG before applying
- Brisbane or Canberra with remote-first setup or occasional travel: PASS with note
- Brisbane or Canberra with fixed weekly office cadence: FLAG before applying
- Requires relocation outside Australia: FAIL
- Travel required for the role: PASS with note when reasonable for senior product/strategy work; flag cadence before applying
- Frequent international travel: FLAG before applying
- FIFO or rostered work: FAIL unless user explicitly requests a review
- Australian work rights required: PASS; candidate is an Australian Permanent Resident
- Security clearance, police check, or background check: FLAG for awareness, not a fit penalty unless clearance is mandatory and unavailable
- Salary excludes superannuation, uses total-package wording, or appears below senior Australian PM market expectations: FLAG before applying

### 5. Career Alignment & Motivation (0-100)
Does this role advance career goals and contain tasks that energize?

| Score | Meaning |
|-------|---------|
| 80-100 | Strongly aligned with career direction, clear growth path |
| 60-79 | Good role but only partially aligned with long-term goals |
| 40-59 | Decent job but doesn't build toward career goals |
| 0-39 | Dead end or backwards step |

**Career goals:**
- Target senior product roles where AI, GenAI, agentic workflows, or decisioning systems are central to the product strategy.
- Include Product Owner, Senior Product Owner, and strategy/transformation roles when they carry product ownership, digital/AI transformation, platform strategy, or measurable business outcome accountability.
- Prioritise roles with end-to-end ownership across discovery, roadmap, delivery, go-to-market, and measurable commercial outcomes.
- Build on enterprise SaaS, retail/CPG/eCommerce, financial services, healthcare, and product consulting experience in the Australian market.

**Motivation filter:** Evaluate not just whether you *can* do the tasks, but whether the tasks will *energize* you. Consider:
- Tasks that energize: AI product strategy, agentic workflow design, enterprise platform roadmaps, product ownership, strategy-to-execution transformation, product operating model work, pricing/decisioning systems, experimentation, cross-functional leadership, C-suite stakeholder work, products with clear revenue or operational-impact metrics.
- Tasks that drain or reduce priority: maintenance-heavy product roles, pure delivery coordination, backlog-only Product Owner roles, narrow feature ownership, coding-first roles without product strategy scope, formal people-management-only roles, or roles dominated by sales/account ownership rather than product ownership.
- Non-task factors: leadership style, department culture, company values, degree of autonomy, product ownership clarity, executive alignment, and maturity of AI/product operating model.

**Life situation alignment:** Consider personal constraints:
- **Security**: Salary must be checked before applying. Flag below-market senior PM packages, missing superannuation clarity, or total-package ambiguity.
- **Flexibility**: Sydney-based Australian Permanent Resident. Prioritise Sydney, hybrid Sydney, remote Australia, and Melbourne roles when flexible or hybrid. Travel roles are acceptable when cadence is reasonable; clarify travel expectations before applying.
- **Professional development**: Strongest signal is growth through senior AI product leadership, product ownership, platform strategy, strategy/transformation work, GenAI/product operating frameworks, and enterprise stakeholder influence.

### 6. Salary Benchmark (Optional)

If the salary lookup tool is configured (`salary_data.json` exists), look up the company:
```
python salary_lookup.py "<Company Name>" --json
```

If a city is known from the posting, add `--city "<City>"` to narrow results.

Present findings as:
```
### Salary Benchmark
| Metric | Value |
|--------|-------|
| [Category] index | XX.X (+/-X.X% vs baseline) |
| Overall index | XX.X (+/-X.X% vs baseline) |
```

Interpret results relative to the baseline defined in the data file's metadata. For index-based data, higher typically means above-market compensation.

If the salary tool is not configured, skip this section.

## Output Format

Present the evaluation as:

```
## Job Fit Evaluation: [Role] at [Company]

| Dimension | Score | Notes |
|-----------|-------|-------|
| Technical Skills | XX/100 | [brief note] |
| Experience Match | XX/100 | [brief note] |
| Behavioral Fit | XX/100 | [brief note] |
| Location | PASS/FAIL | [brief note] |
| Career Alignment | XX/100 | [brief note] |

**Overall Score: XX/100** (weighted average of scored dimensions)

### Verdict: [Strong Fit / Good Fit / Moderate Fit / Weak Fit / Poor Fit]

### Key Strengths for This Role
- [bullet points]

### Gaps to Address
- [bullet points]

### Recommendation
[1-2 sentences: apply/skip/apply with caveats]

### Company Research Checklist
- [ ] Checked company website (mission, values, recent news)
- [ ] Checked review/salary sites relevant to Australia (SEEK company reviews, Glassdoor, Indeed, LinkedIn)
- [ ] Checked LinkedIn for team size, recent hires, connections
- [ ] Checked media for restructuring, growth, or workplace issues
- [ ] Identified network contacts who may know the team/manager
```

## Weighting
- Technical Skills: 30%
- Experience Match: 25%
- Behavioral Fit: 15%
- Career Alignment: 30%

(Location is pass/fail, not weighted)

## Thresholds
- **Strong Fit** (75+): Definitely apply, tailor everything
- **Good Fit** (60-74): Apply, address gaps in cover letter
- **Moderate Fit** (45-59): Consider carefully, discuss with user
- **Weak Fit** (30-44): Probably skip unless strategic reasons
- **Poor Fit** (<30): Skip

## Pre-Application: Call the Employer (Best Practice)

Before writing the application, consider whether the candidate should call the contact person listed in the posting. **Only call if there are substantive questions** - never call just to "be remembered."

### When to Suggest Calling
- The posting has unclear or ambiguous requirements
- It's unclear which competencies are essential vs. nice-to-have
- The role description is vague about day-to-day tasks
- There's a named contact person who invites questions

### Good Questions to Ask
- "What are the primary challenges in this role?"
- "How is time typically divided across the listed responsibilities?"
- "Which competencies are most critical for success in this position?"
- "What does success look like in the first 6-12 months?"
- "What is the expected office cadence for this team?"
- "Is the listed salary package inclusive or exclusive of superannuation?"
- "Are Australian work rights, baseline checks, or security clearances required?"

### Rules for the Call
- Prepare a 30-second "elevator pitch" about your background in case they ask
- The call's purpose is **gathering information**, not delivering a pitch
- Take notes - use what you learn to tailor the application
- Reference the conversation naturally in the cover letter ("After speaking with [name], I was especially drawn to...")
