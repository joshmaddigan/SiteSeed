# CLAUDE.md — SiteSeed Project Context

> **Read this file before every task.** This is the source of truth
> for the SiteSeed project. If anything in a phase prompt contradicts
> this file, pause and ask for clarification before proceeding.

---

## What is SiteSeed?

SiteSeed is a Python/Flask tool that generates personalized preview
websites for small businesses using the Anthropic API. A human
operator collects minimal information from a small business, feeds
it into SiteSeed, and SiteSeed produces a polished preview website.
The preview is used as a sales tool to convert the business into a
paid customer for a full website.

**Business model:** Free preview → paid full site (pricing TBD).
**Initial outreach:** Human-driven, not automated.
**Target customers:** Small businesses without existing websites.

---

## Who you're working with

The project owner is a beginner-to-intermediate Python developer.

**Comfortable with:**
- Python basics: loops, functions, lists, dictionaries
- Classes with `__init__` and methods
- Basic Flask routing
- HTML and CSS (can debug)
- Git basics
- Command line basics

**Currently learning:**
- OOP fundamentals (instance variables, methods, object relationships)
- Encapsulation and dunder methods (next focus)
- Project structure and architecture

**Not yet comfortable with:**
- Anthropic API / external APIs
- Databases beyond surface level
- Testing patterns
- FastAPI (knows Flask)
- Complex deployment

**Long-term goal:** Backend Python developer role within 1–2 years.

---

## Division of labor

There are three roles on this project:

- **Owner (human)** — vision, decisions, final approval, builds
  specific learning-focused pieces themselves
- **Claude (chat)** — director, planner, prompt-writer, code reviewer
- **Claude Code (you)** — builds nearly everything; the hands of
  the project

**Rule:** Nothing ships without owner approval. When in doubt, ask.

---

## Rules of engagement

1. **Always read this file first.** Every task. Every phase.
2. **Pause and ask when unclear.** If a phase prompt is ambiguous,
   contradicts this file, or expects something you can't reasonably
   infer, stop and ask the owner before doing anything destructive.
3. **One phase at a time.** Do not build features from future phases.
   If you finish early, summarize and wait.
4. **Update `NOTES.md` after every task.** This is the owner's
   private dev log and the most important document in the project
   for the owner. See the NOTES.md section below.
5. **Never push to remote git.** Commit locally only. The owner
   handles all pushes.
6. **Never commit secrets.** No API keys, no `.env` contents.
7. **Stay in the established architecture.** If you think a
   refactor is needed, propose it in `NOTES.md` and wait for
   approval before doing it.
8. **Default to teaching, not just doing.** When you make a
   non-obvious decision, explain it in `NOTES.md` so the owner
   understands their own codebase.

---

## Architecture overview

SiteSeed is built around four core classes:

- **`BusinessProfile`** — represents a small business's information.
  The data backbone. *Owner will build this themselves in Phase 2
  as an OOP learning exercise.*
- **`ContentGenerator`** — wraps the Anthropic API. Takes a
  `BusinessProfile`, returns AI-generated content (headlines, copy,
  service descriptions).
- **`Template`** — represents a site template. Self-contained
  HTML/CSS. Multiple templates exist; a registry pattern lets new
  templates be added by dropping a folder in.
- **`PreviewSite`** — the orchestrator. Combines a `BusinessProfile`,
  generated content, and a `Template` to produce a finished
  preview site (HTML files on disk + Flask route to view it).

**Data flow:**

```
User input (form)
   ↓
BusinessProfile (validates, stores)
   ↓
ContentGenerator (calls Anthropic API)
   ↓
Template (renders content into HTML/CSS)
   ↓
PreviewSite (writes files, exposes URL)
   ↓
Operator shares preview link with business
```

---

## Tech stack

- **Language:** Python 3.11+
- **Web framework:** Flask (application factory pattern)
- **AI provider:** Anthropic Claude API (via `anthropic` Python SDK)
- **Testing:** pytest
- **Environment:** `python-dotenv` for local env vars
- **Version control:** Git
- **Future deployment target:** TBD — see "Deployment vision" below.

---

## Deployment vision

SiteSeed is a fully deployed web service. The endgame:

- Hosted on the public internet at a real domain
- No end user — operator or customer — installs or runs anything
  locally
- Internet access is the only requirement on any user's end
- Operators log in via a browser to access SiteSeed's interface
- Customers receive shareable preview links viewable in any browser
- Final preview and paid-site URLs must look professional. Generic
  platform subdomains (e.g. `*.railway.app`) are not acceptable
  customer-facing URLs.

Local development is for the owner only. All architectural
decisions should support eventual public deployment without
requiring a refactor. If a decision would foreclose on this
endgame, propose an alternative in `NOTES.md`.

Hosting platforms that produce generic URLs (Railway's
`*.railway.app`, PythonAnywhere's `*.pythonanywhere.com`, etc.)
are acceptable for development and internal tooling, but are
**not acceptable for customer-facing preview or paid-site URLs.**
Customer-facing URLs must be on SiteSeed's own domain or a
customer-owned domain. This will require dedicated hosting
infrastructure decided at Phase 11.

---

## Operator and customer model

SiteSeed has two distinct user types: operators and customers.

### Operators
- Use SiteSeed's web interface to generate preview sites
- Initially the owner only; eventually a small team
- Long-term: small business owners themselves may become operators
  via public signup (self-serve mode)
- Access via login

### Customers
- Small business owners who receive preview links
- Do not log in or install anything
- View their preview in a browser via a shareable link
- Convert into paid customers by upgrading to a paid tier

### Form design principle
There is **one universal form** for collecting business
information. Industry is a field in the form, not a branching
question set. The backend uses the industry value to select
templates and shape AI content generation.

**Output parity is a hard requirement.** The form must produce
identical output regardless of who fills it out:

- An operator filling it out on behalf of a customer
- A customer filling it out themselves

Additionally, operators must be able to **edit submissions made
by customers** — if a customer submits the form and then a sales
call happens, the operator pulls up the submission and refines
it. Same form, viewed in edit mode.

---

## Customer tiers (product strategy)

SiteSeed offers a tiered product:

### Free Preview (lead magnet)
- Generic-but-personalized preview site
- Industry-appropriate template and AI-generated copy
- Visible placeholders inviting the customer to add their own
  content ("Your testimonial here", "Add your photos", "Insert
  your story") — these serve dual purpose: showing potential
  and demonstrating ownership
- Premium features teased, not hidden
- Shared via a SiteSeed-hosted link
- Pricing: free

### Hosted Tier (low-cost paid)
- Full site hosted on SiteSeed's infrastructure
- SiteSeed-style URL (e.g. `joesplumbing.siteseed.com`)
- No custom domain required
- Lower price point for budget-conscious customers
- Pricing: TBD

### Custom Domain Tier (premium paid)
- Full site with customer's own domain
- Either customer brings a domain, or SiteSeed sources one for them
- Pricing: TBD

### Voice and tone (critical)
- Gracious, not pushy
- Earned conversion, not pressured conversion
- The quality of the preview does the selling
- **Premium features should feel like the customer's own idea,
  not the provider's pitch.** The preview should be designed so
  the customer notices gaps and limitations themselves — the
  desire for "more" comes from them, not from us telling them
  they need more.
- Modern customers are hesitant about aggressive sales tactics
- Premium features may be acknowledged with neutral phrasing like
  "available with full site" — never popups, pressure CTAs, or
  guilt-driven framing
- The free preview must feel like a gift, not a trap

---

## Full roadmap

Phases marked 🧑 are built by the owner with Claude (chat) as tutor.
Phases marked 🤖 are built by you (Claude Code). Phases marked 🟡
require a planning conversation before starting.

- 🤖 **Phase 1** — Scaffolding and project skeleton
- 🧑 **Phase 2** — `BusinessProfile` Part A: basics (`__init__`,
  instance variables)
- 🧑 **Phase 3** — `BusinessProfile` Part B: methods
- 🤖 **Phase 4** — JSON save/load for `BusinessProfile`
- 🤖 **Phase 5** — `ContentGenerator` with full Anthropic API
  integration
- 🤖 **Phase 6** — Template system + first generic template
- 🧑 **Phase 7** — Flask form for business info input. **This form
  is real product code, not throwaway dev tooling.** It must work
  for both operator-input and (eventual) customer self-serve modes,
  producing identical output regardless of who fills it out. Must
  support operator edit mode for customer-submitted forms. Build
  with auth-readiness in mind, even though auth comes later.
- 🤖 **Phase 8** — `PreviewSite` orchestrator + preview route
- 🤖 **Phase 9** — Polish pass (mobile responsiveness, error
  handling, quality tuning)
- 🤖 **Phase 10** — Second template (trades industry)
- 🟡 **Phase 11** — Hosting decision and setup. Tied to product
  tier strategy: hosted tier vs. custom domain tier infrastructure.
  Pricing decided here, only after the product quality justifies
  charging for it.
- 🟡 **Phase 12** — Payments and conversion flow

**Future (post-MVP):** more templates (food, professional services,
personal services, retail, wellness, pet services, mobile services),
user-facing self-serve form, analytics on previews, refactor pass.

---

## File conventions

- `README.md` — public-facing, professional, kept up to date
- `NOTES.md` — private dev log, gitignored, **the owner's primary
  reference**
- `prompts/` — every Claude Code prompt used on this project, kept
  for record. Naming convention:
  - `phase_XX_*.md` — phase prompts (major build steps)
  - `update_XX_*.md` — updates to docs or strategy
  - `fix_XX_*.md` — bug fixes or rework
  - `task_XX_*.md` — one-off tasks that don't fit elsewhere
- `CLAUDE.md` — this file
- All Python follows PEP 8
- Every class and public function has a docstring

---

## How to write `NOTES.md` entries

After every task, append a new section to `NOTES.md` with:

1. **Phase and date** — e.g., `## Phase 1 — 2026-05-26`
2. **What was built** — every file created or modified, one line
   each, plain English
3. **How the pieces connect** — short data-flow explanation if
   anything new was added to the flow
4. **Where to look when X breaks** — short debugging tips for
   anything new (e.g., "If previews aren't generating, check
   `ContentGenerator.generate()` first")
5. **Glossary additions** — any term used that's beyond beginner
   Python, explained in plain English
6. **Decisions made and why** — anything where you made a judgment
   call the owner should know about
7. **Questions to ask Claude (chat)** — pre-written prompts the
   owner can paste into a Claude conversation if they get stuck
   debugging this phase's code
8. **Anything you weren't sure about** — flag for owner review

This file is the owner's safety net. Take it seriously.

---

## Anti-patterns (do not do these)

- Don't hardcode API keys, paths, or business names
- Don't install dependencies the project doesn't actually need
- Don't refactor existing code without asking
- Don't build ahead of the current phase
- Don't write tests just for coverage — test what matters
- Don't use complex patterns where simple ones work (the owner is
  still learning)
- Don't silently swallow errors — surface them clearly