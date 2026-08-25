# Search Queries for Job Scraper

<!-- SETUP: Customised from Aditya Vikram Godawat's CV on 2026-08-25. -->

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

- **Primary role direction:** Senior Product Manager, AI Product Manager, GenAI Product Manager, Principal Product Manager, Product Lead
- **Core skills:** GenAI, agentic workflows, AI product strategy, LLM implementation, prompt engineering, enterprise SaaS, experimentation, decisioning systems
- **Domain strengths:** Retail, CPG, eCommerce, financial services, healthcare, B2B platforms, enterprise AI, pricing platforms
- **Location base:** Sydney, NSW, Australia
- **Work rights:** Australian Permanent Resident

## Query Categories

Queries are grouped by priority. Combine with "Sydney", "NSW", "Australia", "remote Australia", or "hybrid Sydney" where useful.

### Priority 1: Senior AI Product Leadership

These match the strongest and most desired career direction.

```text
site:seek.com.au "Senior Product Manager" "AI" Sydney
site:seek.com.au "AI Product Manager" Sydney
site:seek.com.au "GenAI Product Manager" Australia
site:au.linkedin.com/jobs "Senior Product Manager" "Generative AI" Australia
site:au.linkedin.com/jobs "AI Product Manager" Sydney
site:au.linkedin.com/jobs "Product Lead" "AI" Australia
site:workdayjobs.com "AI Product Manager" Australia
site:greenhouse.io "Senior Product Manager" "AI" Australia
site:lever.co "Product Lead" "GenAI" Australia
```

### Priority 2: Enterprise SaaS, Decisioning, and Experimentation

These match enterprise platform and domain expertise.

```text
site:seek.com.au "Principal Product Manager" "enterprise SaaS" Sydney
site:seek.com.au "Product Manager" "decisioning" Australia
site:seek.com.au "Product Manager" "experimentation" Sydney
site:au.linkedin.com/jobs "Product Manager" "A/B testing" Australia
site:au.linkedin.com/jobs "Product Manager" "pricing" Sydney
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

Wider net for product strategy, product consulting, and AI transformation roles.

```text
site:seek.com.au "Product Strategy" "AI" Sydney
site:seek.com.au "Product Consultant" "AI" Australia
site:seek.com.au "AI Strategy" "Product" Sydney
site:au.linkedin.com/jobs "Product Strategy Manager" Australia
site:au.linkedin.com/jobs "AI Transformation" "Product" Australia
site:workforceaustralia.gov.au "Product Manager" "AI" Sydney
site:apsjobs.gov.au "Product Manager" "AI" NSW
site:smartrecruiters.com "AI Strategy" Australia
```

## Target Companies To Monitor

Not yet confirmed by user. Based on CV fit, consider monitoring:
- AI-native and enterprise SaaS companies hiring in Australia
- Retail technology, pricing, experimentation, and decisioning platforms
- Fintech and financial-services product teams
- Healthcare AI and workflow automation companies
- Consulting and product strategy teams with AI transformation work

## Location Filter

When evaluating results, verify the job location is compatible with Sydney-based work.
- **Ideal:** Sydney, NSW; hybrid Sydney; remote Australia with Sydney-compatible timezone.
- **Acceptable:** Australia-remote roles; NSW roles with occasional Sydney office cadence.
- **Borderline:** Melbourne/Brisbane/Canberra roles if mostly remote or requiring only occasional travel, pending user confirmation.
- **Too far / flag before evaluating:** Roles requiring relocation outside Sydney/Australia, FIFO/rostered work, or frequent interstate/international travel.

For Australian roles, distinguish:
- Local office roles within commute range
- Hybrid roles with a named office and expected office cadence
- Remote roles limited to Australia, which may still require Australian work rights or a state time zone
- FIFO, rostered, or travel-heavy roles, which should be flagged before evaluation
- Salary package inclusive or exclusive of superannuation

## Date Filter

Only include jobs posted within the last 14 days, or with an application deadline that has not yet passed. If a posting date cannot be determined, include it but flag as "date unknown".

## Adapting Queries

If the user specifies a focus area, select queries from the matching category and generate 2-3 custom queries for that focus.

Examples:
- "Find GenAI product jobs" -> Priority 1 plus custom agentic workflow / LLM product queries.
- "Find fintech product jobs" -> Priority 3 plus financial services, pricing, decisioning, and collections automation queries.
- "Find remote AI product jobs" -> Priority 1 and 4 with remote Australia filters and stricter travel checks.
