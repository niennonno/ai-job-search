# Search Queries for Job Scraper

<!-- SETUP: Customised from Aditya Vikram Godawat's CV on 2026-08-25. -->

## Installed portal CLIs (primary for `/scrape`)

`/scrape` discovers every portal skill under `.agents/skills/*/SKILL.md` and runs its CLI first. Shipped country-agnostic CLIs include `linkedin-search` and `freehire-search`; Danish demos and any skill you add with `/add-portal` are included the same way. You do **not** need a matching `site:` line below for those CLIs to run.

The `site:` query templates in this file are the **WebSearch fallback** — for portals without a CLI, company career pages, or when a CLI fails.

**Language scope:** write every query category in every language listed in your CODEX.md Languages table (typically 1-2, sometimes more). A posting requiring a language you have *not* declared, as a job condition, is excluded before scoring; a posting requiring a *higher level* than you declared in a language you *do* work in is flagged for your own judgment, not excluded — see `04-job-evaluation.md`'s Language Gate, the single source of truth for this rule. Translate each category's keywords rather than machine-translating word-for-word (e.g. "Frontend Developer" -> "Desarrollador Frontend", not a literal word-for-word translation) if you work in more than one language.

## Search Sites

Primary (Australian job market):
- **seek.com.au** - broad Australian job board; use direct browsing or targeted web searches
- **au.linkedin.com/jobs** - LinkedIn Australia job listings
- **workforceaustralia.gov.au** - Australian Government job search
- **apsjobs.gov.au** - Australian Public Service roles
- **company career pages** - Greenhouse, Lever, Workday, SmartRecruiters, Ashby, and direct employer careers pages

Secondary:
- **wellfound.com** - startup and AI/product roles
- **builtin.com** - product and technology roles where Australian listings appear
- **ethicaljobs.com.au** - purpose-led organisations, only when product/AI scope is relevant
- Specialist boards for product leadership, AI product, fintech, retail technology, and enterprise SaaS if identified later

## Candidate Search Focus

- **Primary role direction:** Senior Product Manager, Product Manager, Technical Product Manager, Product Owner, Senior Product Owner, AI Product Manager, GenAI Product Manager, Principal Product Manager, Product Lead, Product Strategy, AI/Digital Transformation
- **Core skills:** PM persona: GenAI, agentic workflows, AI product strategy, LLM implementation, prompt engineering, enterprise SaaS, customer success, implementation, experimentation, decisioning systems. Strategy/consulting persona: product operating models, technology transformation, executive advisory, AI transformation.
- **Domain strengths:** Retail, CPG, eCommerce, financial services, investment banking, healthcare, technology, B2B platforms, enterprise AI, pricing platforms
- **Location base:** Sydney, NSW, Australia
- **Work rights:** Australian Permanent Resident

## Query Categories

Queries are grouped by priority. Write **each category in every language from your Languages table** (see Language scope above). Combine with "Sydney", "NSW", "Australia", "remote Australia", or "hybrid Sydney" where useful.

**Organize by function, not job title.** The same underlying work carries different titles across companies and markets (a "Data Scientist" role at one employer may be posted as "Insights Analyst" or "Data Consultant" at another). Name each priority category after the function it covers, and list several plausible job titles as query variants within that category rather than betting an entire priority tier on one exact title string.

### Priority 1: Senior AI Product Leadership

These match the strongest and most desired career direction.

```text
site:seek.com.au "Senior Product Manager" "AI" Sydney
site:seek.com.au "AI Product Manager" Sydney
site:seek.com.au "GenAI Product Manager" Australia
site:au.linkedin.com/jobs "Senior Product Manager" "Generative AI" Australia
site:au.linkedin.com/jobs "AI Product Manager" Sydney
site:au.linkedin.com/jobs "Product Lead" "AI" Australia
site:seek.com.au "Senior Product Owner" "AI" Sydney
site:au.linkedin.com/jobs "Senior Product Owner" "AI" Australia
site:workdayjobs.com "AI Product Manager" Australia
site:greenhouse.io "Senior Product Manager" "AI" Australia
site:lever.co "Product Lead" "GenAI" Australia
```

### Priority 2: Enterprise SaaS, Decisioning, and Experimentation

These match enterprise platform and domain expertise.

```text
site:seek.com.au "Principal Product Manager" "enterprise SaaS" Sydney
site:seek.com.au "Product Manager" "customer success" Sydney
site:seek.com.au "Product Manager" "implementation" Australia
site:seek.com.au "Product Manager" "decisioning" Australia
site:seek.com.au "Product Manager" "experimentation" Sydney
site:seek.com.au "Product Owner" "enterprise SaaS" Sydney
site:au.linkedin.com/jobs "Product Manager" "A/B testing" Australia
site:au.linkedin.com/jobs "Product Manager" "pricing" Sydney
site:au.linkedin.com/jobs "Product Owner" "platform" Australia
site:au.linkedin.com/jobs "Product Manager" "customer success" Australia
site:au.linkedin.com/jobs "Product Manager" "implementation" Australia
site:greenhouse.io "Product Manager" "enterprise SaaS" Australia
site:workdayjobs.com "Product Manager" "pricing" Australia
site:smartrecruiters.com "Product Manager" "experimentation" Australia
```

### Priority 3: Domain-Aligned Product Roles

Adjacent roles where retail, CPG, eCommerce, finance, healthcare, or consulting experience is useful.

```text
site:seek.com.au "Product Manager" "retail" "AI" Sydney
site:seek.com.au "Product Manager" "CPG" Australia
site:seek.com.au "Product Manager" "financial services" "AI" Sydney
site:seek.com.au "Product Manager" "healthcare" "AI" Australia
site:au.linkedin.com/jobs "Product Manager" "eCommerce" Sydney
site:au.linkedin.com/jobs "Product Strategy" "AI" Australia
site:greenhouse.io "Product Manager" "fintech" Australia
site:lever.co "Product Manager" "retail technology" Australia
```

### Priority 4: Broader Product Strategy / Advisory

Wider net for the strategy/consulting persona: product strategy, product consulting, product operating model, technology transformation, and AI transformation roles.

```text
site:seek.com.au "Product Strategy" "AI" Sydney
site:seek.com.au "Product Consultant" "AI" Australia
site:seek.com.au "AI Strategy" "Product" Sydney
site:seek.com.au "Technology Transformation" "Product" Sydney
site:seek.com.au "Product Operating Model" Australia
site:seek.com.au "Strategy Transformation" "Product" Sydney
site:seek.com.au "Digital Transformation" "Product Owner" Sydney
site:au.linkedin.com/jobs "Product Strategy Manager" Australia
site:au.linkedin.com/jobs "AI Transformation" "Product" Australia
site:au.linkedin.com/jobs "AI Transformation" "Product Owner" Australia
site:au.linkedin.com/jobs "Technology Transformation" "Product" Australia
site:au.linkedin.com/jobs "Product Strategy" "Transformation" Sydney
site:workforceaustralia.gov.au "Product Manager" "AI" Sydney
site:apsjobs.gov.au "Product Manager" "AI" NSW
site:smartrecruiters.com "AI Strategy" Australia
```

## Target Companies And Categories To Monitor

Monitor companies and categories that repeatedly match Aditya's senior AI/product profile:
- AI-native and enterprise SaaS companies hiring in Australia
- Agentic AI, workflow automation, AI platform, and AI evaluation products
- Retail technology, pricing, experimentation, and decisioning platforms
- Fintech, lending, payments, and financial-services product teams
- Investment banking and enterprise finance transformation product teams
- Healthcare AI, healthtech, and regulated workflow automation companies
- Consulting and product strategy teams with AI transformation work, for the strategy/consulting persona

Known high-interest companies from current tracker/searches include Checkbox, Relevance AI, Culture Amp, Lendi Group, carsales, Cartology, Quantaco, Cotality, Zip, Nuix, Driva, Mable, and Expertech. Skip The Onset for follow-up action unless Aditya explicitly reopens it.

## Location Filter

When evaluating results, verify the job location is compatible with Sydney-based work.
- **Ideal:** Sydney, NSW; hybrid Sydney; remote Australia with Sydney-compatible timezone.
- **Acceptable:** Australia-remote roles; NSW roles with occasional Sydney office cadence.
- **Acceptable:** Melbourne roles when flexible, hybrid, or without a rigid weekly office cadence.
- **Conditional:** Brisbane/Canberra roles only when remote-first or requiring occasional travel.
- **Travel:** Include travel roles when the travel appears reasonable for senior product/strategy work; flag cadence before applying.
- **Skip by default:** Roles requiring relocation outside Australia, FIFO/rostered work, or inflexible non-Sydney/non-Melbourne office cadence.

## Role Level Filter

- **Include:** Senior Product Manager, Product Manager, Technical Product Manager, Product Owner, Senior Product Owner, AI Product Manager, GenAI Product Manager, Principal Product Manager, Product Lead, Product Strategy Manager, Product Strategy Lead, AI Transformation Manager/Lead, and digital/product strategy transformation roles.
- **Skip by default:** Head of Product, CPO, VP Product, Group Product Manager, pure delivery/program roles, backlog-only Product Owner roles, sales-led solutions roles, and coding-first engineering roles without product ownership.

For Australian roles, distinguish:
- Local office roles within commute range
- Hybrid roles with a named office and expected office cadence
- Remote roles limited to Australia, which may still require Australian work rights or a state time zone
- FIFO or rostered roles, which should be flagged before evaluation
- Travel-heavy roles, which should be assessed for cadence rather than skipped automatically
- Salary package inclusive or exclusive of superannuation

## Language Filter

Your working languages and levels are in CODEX.md's Languages table. When filtering scraped results, apply `04-job-evaluation.md`'s Language Gate: a posting requiring a language you haven't declared at all is excluded; a posting requiring a higher level than you declared in a language you do work in is not excluded, flag it clearly instead (see `job-scraper/SKILL.md`'s Step 3 "Quick Fit Assessment" for how the flag surfaces in `/scrape` output). Postings simply *written* in a language you don't work in, that don't require it on the job, are fine.

## Date Filter

Only include jobs posted within the last 14 days, or with an application deadline that has not yet passed. If a posting date is not visible, include only when the source page is live and the role has a working application path; label the date as "not visible on posting".

## Adapting Queries

If the user specifies a focus area, select queries from the matching category and generate 2-3 custom queries for that focus.

Examples:
- "Find GenAI product jobs" -> Priority 1 plus custom agentic workflow / LLM product queries.
- "Find fintech product jobs" -> Priority 3 plus financial services, pricing, decisioning, and collections automation queries.
- "Find remote AI product jobs" -> Priority 1 and 4 with remote Australia filters and travel-cadence checks.
