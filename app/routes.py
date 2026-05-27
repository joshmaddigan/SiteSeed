"""
app/routes.py — URL routes for the SiteSeed application.

A "route" is the connection between a URL (like "/") and a Python
function that handles requests to that URL. Flask calls these
handler functions "view functions."

HOW BLUEPRINTS WORK:
--------------------
Instead of decorating routes directly on the `app` object, we use
a Blueprint. A Blueprint is a collection of routes that can be
registered onto any Flask app. This keeps routes organized and
makes the app factory pattern work cleanly.

When create_app() runs `app.register_blueprint(main)`, Flask
attaches all routes defined here to the app.

ADDING YOUR OWN ROUTES (Phase 7):
----------------------------------
To add a new route, follow this pattern:

    @main.route("/your-path")
    def your_function_name():
        return render_template("your_template.html")

The function name must be unique within the blueprint.
"""

from flask import Blueprint, render_template

# Create a Blueprint named "main".
# The first argument ("main") is an internal name Flask uses to
# identify this blueprint — you'll reference it in url_for() calls.
# The second argument (__name__) helps Flask locate this blueprint's
# templates and static files if it had its own.
main = Blueprint("main", __name__)


@main.route("/")
def index():
    """Render the SiteSeed home/status page."""
    return render_template("index.html")
