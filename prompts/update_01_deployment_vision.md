# SiteSeed — Update 01: Deployment Vision & Product Strategy

**Date:** 2026-05-26
**Author:** Owner (manual edit to CLAUDE.md)
**Committed as:** "Add deployment vision and product strategy to CLAUDE.md"

---

## What this update added to CLAUDE.md

### 1. Deployment vision (new section)

SiteSeed is a fully deployed public web service — not a local tool.
Key constraints established:

- Hosted at a real domain; no local installs for operators or customers
- Generic platform subdomains (`*.railway.app`, `*.pythonanywhere.com`)
  are acceptable for dev/internal use only — **never customer-facing**
- All architectural decisions must support public deployment without
  requiring a refactor
- Hosting infrastructure decided at Phase 11

### 2. Operator and customer model (new section)

Two distinct user types:

**Operators** — use SiteSeed's web UI to generate previews; initially
owner only; eventually potentially public self-serve.

**Customers** — small business owners who receive and view preview
links; no login or install required; convert by upgrading to paid tier.

**One universal form** — industry is a field, not a branching question
set. Output parity is a hard requirement (identical output regardless
of who fills it in). Operators can edit customer-submitted forms.

### 3. Customer tiers / product strategy (new section)

Three tiers established:

| Tier | Description | URL style | Price |
|---|---|---|---|
| Free Preview | Personalized preview with visible placeholders | SiteSeed-hosted link | Free |
| Hosted | Full site on SiteSeed infra | `business.siteseed.com` | TBD |
| Custom Domain | Full site on customer's own domain | Customer domain | TBD |

**Voice and tone:** Gracious, not pushy. The preview does the selling.
Premium features should feel like the customer's own idea.

### 4. Phase 7 annotation updated

Phase 7 (Flask form) is now explicitly real product code. Requirements
added: operator-input and customer self-serve parity; operator edit
mode; auth-readiness.

### 5. Phase 11 annotation updated

Hosting decision tied to tier pricing strategy; pricing only decided
when product quality justifies charging.

### 6. `prompts/` naming convention added

- `phase_XX_*.md` — phase prompts (major build steps)
- `update_XX_*.md` — updates to docs or strategy
- `fix_XX_*.md` — bug fixes or rework
- `task_XX_*.md` — one-off tasks that don't fit elsewhere

### 7. Tech stack note updated

"Future deployment target: TBD — see Deployment vision below"

---

## Why this matters for future phases

- **Phase 6 (templates):** Preview placeholders should be visually
  inviting, not just blank — they're a selling feature per the tier strategy.
- **Phase 7 (form):** Must be designed for both operator and customer
  paths from day one. Auth-readiness (even without auth yet) means
  no assumptions about who's submitting.
- **Phase 8 (PreviewSite):** Preview URLs will eventually need to be
  on a real domain. The local URL scheme should abstract this so
  swapping in a production URL is trivial.
- **Phase 11 (hosting):** Subdomain routing (`business.siteseed.com`)
  implies DNS and reverse proxy work — flag for planning conversation.
