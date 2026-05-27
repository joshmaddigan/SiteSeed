# 🌱 SiteSeed

> Turn a few facts about a small business into a polished preview website — powered by AI.

SiteSeed is a Python/Flask tool built for human sales operators. You collect a small amount of information from a small business (name, services, location, tone), feed it into SiteSeed, and out comes a professional-looking preview website. That preview is then shared with the business as a sales tool to convert them into a paying customer for a full site.

The entire pipeline — data collection, AI copywriting, template rendering, and preview delivery — is automated. The operator's job is outreach and closing; SiteSeed handles the demo.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11+ |
| Web framework | Flask |
| AI provider | Anthropic Claude API |
| Config | python-dotenv |
| Tests | pytest |

---

## Setup

### Prerequisites
- Python 3.11 or newer
- An Anthropic API key (required for Phase 5+; not needed to run the scaffold)

### Install

```bash
# 1. Clone the repository
git clone https://github.com/<username>/siteseed.git
cd siteseed

# 2. Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
copy .env.example .env      # Windows
cp .env.example .env        # Mac/Linux
# Then edit .env and fill in your values

# 5. Run the development server
python run.py
```

Visit `http://localhost:5000` to confirm the app is running.

### Run tests

```bash
pytest
```

---

## Current Status

**Phase 1 — Scaffolding complete.**

The project skeleton is in place: Flask app factory, configuration, stub model classes, smoke tests, and this README. No business logic yet — that begins in Phase 2.

See the [full roadmap in CLAUDE.md](CLAUDE.md) for what's coming.

---

## Project Structure

```
siteseed/
├── app/                    # Flask application
│   ├── __init__.py         # App factory (create_app)
│   ├── routes.py           # URL routes
│   ├── models/             # Core business logic classes
│   ├── templates/          # Jinja2 HTML templates
│   └── static/             # CSS, JS, images
├── site_templates/         # HTML/CSS site designs (Phase 6+)
├── generated_sites/        # Output: generated preview sites
├── tests/                  # pytest test suite
├── prompts/                # Archived Claude Code prompts
├── config.py               # App configuration
├── run.py                  # Dev server entry point
└── requirements.txt        # Python dependencies
```

---

> ⚠️ **Active development.** This project is being built incrementally. Features and APIs will change between phases. Not production-ready.
