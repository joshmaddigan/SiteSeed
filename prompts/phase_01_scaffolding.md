# SiteSeed — Phase 1: Scaffolding

Read `CLAUDE.md` at the project root before starting. All project
context, rules of engagement, and architectural decisions live
there. This document only describes Phase 1's specific tasks.

**First task before anything else:** Save a copy of this exact
prompt to `prompts/phase_01_scaffolding.md`. Every prompt used on
this project gets archived there as a paper trail.

If anything below is unclear or contradicts `CLAUDE.md`, pause
and ask before proceeding.

---

## Goal

Create the SiteSeed project skeleton. After Phase 1, the project
should be a runnable Flask app showing a placeholder page — no
business logic yet, just structure. The owner uses GitHub to sync
across devices, so this phase ends with the repo ready to connect
to a remote.

---

## Tasks

### 1. Create the folder structure

```
siteseed/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── business_profile.py
│   │   ├── content_generator.py
│   │   ├── template.py
│   │   └── preview_site.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── css/
│           └── style.css
├── site_templates/
│   └── .gitkeep
├── generated_sites/
│   └── .gitkeep
├── prompts/
│   └── phase_01_scaffolding.md
├── tests/
│   ├── __init__.py
│   └── test_smoke.py
├── .gitignore
├── .env.example
├── CLAUDE.md
├── NOTES.md
├── README.md
├── config.py
├── requirements.txt
└── run.py
```

`CLAUDE.md` already exists at the project root — do not overwrite
it. Everything else is yours to create.

### 2. Stub the four core classes

Each model file (`business_profile.py`, `content_generator.py`,
`template.py`, `preview_site.py`) gets just the class signature
and a docstring explaining its eventual purpose. No methods,
no logic. Refer to the architecture overview in `CLAUDE.md` for
what each class is for.

### 3. Build the Flask skeleton

- `run.py` — starts the Flask dev server
- `app/__init__.py` — uses the application factory pattern with
  a `create_app()` function. **Keep it minimal but annotate
  generously with comments** explaining what each piece does
  and why it exists. The owner is learning Flask architecture
  and will build their own routes in Phase 7.
- `app/routes.py` — one route `/` that renders `index.html`
- `app/templates/index.html` — shows "🌱 SiteSeed is alive" and
  a short blurb describing the project
- `app/static/css/style.css` — clean, minimal styling. White
  background, centered content, readable type. Nothing fancy.

### 4. Configuration

`config.py` contains a `Config` class with at minimum:

- `SECRET_KEY` — from env var, dev default acceptable
- `ANTHROPIC_API_KEY` — from env var, defaults to `None`
- `GENERATED_SITES_DIR` — path to `generated_sites/`

Use `os.getenv()`. Do not hardcode.

Also create `.env.example` listing the env vars the project
uses (no real values).

### 5. requirements.txt

Pin recent stable versions of:

- `flask`
- `anthropic`
- `pytest`
- `python-dotenv`

### 6. .gitignore

Standard Python ignores plus:

- `NOTES.md`
- `.env`
- `generated_sites/*` (but keep the directory)
- `venv/`, `.venv/`
- `__pycache__/`
- `.pytest_cache/`
- `.vscode/` (or other editor folders the owner may use)

### 7. README.md

Public-facing. Include:

- Project name and one-line description
- What SiteSeed does (2–3 sentences)
- Setup instructions (clone, venv, install, run)
- Current status: "Phase 1 — Scaffolding complete"
- Tech stack
- Note that this is in active development

### 8. NOTES.md

Initialize the private dev log following the format described
in `CLAUDE.md` under "How to write NOTES.md entries". The Phase 1
entry should cover everything created in this phase, with extra
care given to:

- Plain-English explanation of the Flask application factory
  pattern (the owner is learning this)
- A glossary section explaining any term used that's beyond
  beginner Python
- A "where to look when X breaks" section for this scaffolding

### 9. Smoke test

`tests/test_smoke.py` — one test that imports the Flask app
factory and asserts it returns an app. Just enough to confirm
`pytest` works and imports are sound.

### 10. Git

- `git init`
- Stage everything
- One commit: `Initial Phase 1 scaffolding`
- **Do not connect to a remote or push.** The owner will handle
  that. After committing, output the exact commands the owner
  needs to run to connect to a GitHub remote and push for the
  first time. Use this format (with placeholders the owner can
  fill in):

```
  # After creating an empty repo on GitHub:
  git remote add origin https://github.com/<username>/<repo>.git
  git branch -M main
  git push -u origin main
```

---

## Done criteria

- [ ] `python run.py` starts Flask with no errors
- [ ] `http://localhost:5000` shows the alive page, styled cleanly
- [ ] `pytest` runs and passes
- [ ] `git log` shows one commit
- [ ] `README.md` is accurate and informative
- [ ] `NOTES.md` exists, is gitignored, and follows the format
      in `CLAUDE.md`
- [ ] All four stub classes exist with docstrings
- [ ] `prompts/phase_01_scaffolding.md` contains this prompt
- [ ] No secrets in code or in commits
- [ ] GitHub remote instructions provided to the owner

---

## When you're done

Provide a summary to the owner:

1. What you built (high level)
2. Any decisions you made that deviated from this prompt and why
3. Anything you weren't sure about
4. Exact commands the owner should run to verify everything works
5. Exact commands the owner should run to connect to GitHub

Then stop. Do not start Phase 2.
