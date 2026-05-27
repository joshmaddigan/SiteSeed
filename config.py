"""
config.py — Application configuration.

All settings that vary between environments (development, production)
live here. Values are read from environment variables so that no
secrets ever appear in source code.

Usage:
    The Flask app factory (app/__init__.py) loads this class via
    app.config.from_object(Config).

Adding a new config value:
    1. Add it to the Config class below using os.getenv()
    2. Add a matching line to .env.example (with no real value)
    3. Add the real value to your local .env file (which is gitignored)
"""

import os


class Config:
    """
    Central configuration class for SiteSeed.

    Reads all settings from environment variables. A .env file
    (loaded by python-dotenv in the app factory) provides those
    variables during local development.
    """

    # SECRET_KEY is used by Flask to sign session cookies and other
    # security-sensitive data. It must be a long, random string in
    # production. The fallback here is fine for development only.
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")

    # Your Anthropic API key. Loaded from the environment so it never
    # appears in code or git history. Will be None if not set — the
    # ContentGenerator class (Phase 5) will surface a clear error
    # rather than silently failing.
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", None)

    # Absolute path to the folder where SiteSeed writes finished
    # preview sites. Using os.path keeps this portable across
    # Windows, Mac, and Linux — no hardcoded slashes.
    GENERATED_SITES_DIR = os.getenv(
        "GENERATED_SITES_DIR",
        os.path.join(os.path.dirname(__file__), "generated_sites"),
    )
