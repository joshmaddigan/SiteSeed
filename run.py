"""
run.py — Development server entry point.

Run this file to start the Flask development server:
    python run.py

This file is only used for local development. In production,
a proper WSGI server (like Gunicorn) would import `create_app`
directly and serve it — this file wouldn't be involved.
"""

from app import create_app

# Create the Flask application using the factory function.
# The factory lives in app/__init__.py and handles all setup.
app = create_app()

if __name__ == "__main__":
    # debug=True enables:
    #   - Auto-reload when you save a file (no restart needed)
    #   - Detailed error pages in the browser if something breaks
    # NEVER run with debug=True in production.
    app.run(debug=True)
