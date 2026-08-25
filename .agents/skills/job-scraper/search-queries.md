# Search Queries for Job Scraper

<!-- SETUP: Customize these queries based on your skills, target roles, and location -->

## Search Sites

Primary (Australian job market):
- **seek.com.au** - broad Australian job board; use direct browsing or targeted web searches
- **au.linkedin.com/jobs** - LinkedIn Australia job listings
- **workforceaustralia.gov.au** - Australian Government job search
- **apsjobs.gov.au** - Australian Public Service roles
- **company career pages** - Greenhouse, Lever, Workday, SmartRecruiters, Ashby, and direct employer careers pages

Secondary:
- **ethicaljobs.com.au** - purpose-led, non-profit, education, health, and community roles
- **jobs.theconversation.com** - higher education and research roles
- Specialist boards relevant to the candidate's field, if identified during setup

## Query Categories

Queries are grouped by priority. Combine each query with the user's Australian location terms where useful, such as "Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", "Canberra", "Australia", "remote Australia", or a state abbreviation.

### Priority 1: [YOUR_PRIMARY_ROLE_TYPE]

These match your strongest and most desired career direction.

```
site:seek.com.au "[YOUR_PRIMARY_JOB_TITLE]" [YOUR_CITY]
site:au.linkedin.com/jobs "[YOUR_PRIMARY_JOB_TITLE]" Australia
site:workforceaustralia.gov.au "[YOUR_PRIMARY_JOB_TITLE]" [YOUR_CITY]
site:apsjobs.gov.au "[YOUR_PRIMARY_JOB_TITLE]" [YOUR_STATE]
```

### Priority 2: [YOUR_DOMAIN_EXPERTISE]

These match your domain expertise.

```
site:seek.com.au [YOUR_DOMAIN_KEYWORD_1] [YOUR_CITY] OR [YOUR_STATE]
site:au.linkedin.com/jobs [YOUR_DOMAIN_KEYWORD_1] [YOUR_CITY] Australia
site:greenhouse.io [YOUR_DOMAIN_KEYWORD_1] Australia
site:lever.co [YOUR_DOMAIN_KEYWORD_2] Australia
```

### Priority 3: [YOUR_ADJACENT_ROLE_TYPE]

Adjacent roles you could pivot into.

```
site:seek.com.au "[YOUR_ADJACENT_TITLE_1]" [YOUR_KEY_SKILL] [YOUR_CITY]
site:au.linkedin.com/jobs "[YOUR_ADJACENT_TITLE_2]" [YOUR_KEY_SKILL] Australia
site:workdayjobs.com "[YOUR_ADJACENT_TITLE_1]" Australia
```

### Priority 4: Broader Technical / Consulting

Wider net for general technical roles.

```
site:seek.com.au [YOUR_KEY_SKILL] developer [YOUR_CITY]
site:au.linkedin.com/jobs "[YOUR_KEY_SKILL] developer" Australia
site:seek.com.au "technical consultant" [YOUR_DOMAIN] [YOUR_CITY]
site:smartrecruiters.com [YOUR_KEY_SKILL] Australia
```

## Location Filter

When evaluating results, verify the job location is within reasonable commute distance from your home. Define acceptable areas:
- [YOUR_CITY] and surrounding areas
- [ACCEPTABLE_AREA_1]
- [ACCEPTABLE_AREA_2]
- [BORDERLINE_AREA] (borderline - ~X min by transit)
- [TOO_FAR_AREA] (too far)

For Australian roles, distinguish:
- Local office roles within commute range
- Hybrid roles with a named office and expected office cadence
- Remote roles limited to Australia, which may still require Australian work rights or a state time zone
- FIFO, rostered, or travel-heavy roles, which should be flagged before evaluation

## Date Filter

Only include jobs posted within the last 14 days, or with an application deadline that has not yet passed. If a posting date cannot be determined, include it but flag as "date unknown".

## Adapting Queries

If the user specifies a focus area, select queries from the matching category and also generate 2-3 custom queries for that focus. For example:
- "/scrape [focus_area]" -> relevant category queries + custom focus-specific queries
