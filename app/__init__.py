"""
app/__init__.py — The Flask application factory.

This file is the heart of the Flask app. It defines create_app(),
a function that builds and configures a Flask application object
and returns it. This pattern is called the "application factory"
pattern.

WHY A FACTORY INSTEAD OF A GLOBAL APP OBJECT?
----------------------------------------------
A common beginner Flask pattern is:

    app = Flask(__name__)   # global, created at import time

That works for tiny scripts, but it causes problems as projects grow:

  - You can't create multiple app instances (e.g., one for tests,
    one for the real server) without them colliding.
  - Configuration is tangled up with app creation, making it hard
    to swap settings between environments.

The factory pattern solves this: create_app() builds a fresh app
each time it's called, with whatever config you pass in. The test
suite can call create_app() with test settings; run.py calls it
with production settings. Same code, clean separation.

HOW IT CONNECTS TO THE REST OF THE PROJECT:
-------------------------------------------
  run.py  →  calls create_app()  →  gets back a configured Flask app
  tests/  →  also calls create_app()  →  gets a test-safe app instance
"""

from flask import Flask
from config import Config


def create_app(config_class=Config):
    """
    Build and return a configured Flask application.

    Parameters
    ----------
    config_class : class, optional
        A configuration class to load settings from.
        Defaults to Config (from config.py).
        Tests can pass in a different class to override settings.

    Returns
    -------
    Flask
        A fully configured Flask application instance.
    """

    # Flask(__name__) tells Flask where this application lives.
    # __name__ resolves to the name of the current package ("app"),
    # which Flask uses to locate templates and static files.
    app = Flask(__name__)

    # Load all settings from the Config class (config.py).
    # This reads SECRET_KEY, ANTHROPIC_API_KEY, etc. from environment
    # variables so nothing sensitive is hardcoded.
    app.config.from_object(config_class)

    # --- Register blueprints here as the project grows ---
    # A "blueprint" is Flask's way of grouping related routes.
    # Right now we only have one set of routes, so we import and
    # register them directly. In later phases, each feature area
    # (preview generation, admin, etc.) may get its own blueprint.
    from app.routes import main
    app.register_blueprint(main)

    # Return the assembled app. The caller (run.py or a test) is
    # responsible for running it or using it however they need.
    return app
