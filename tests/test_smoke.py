"""
tests/test_smoke.py — Smoke tests for Phase 1 scaffolding.

A "smoke test" is the most basic possible test: just turn it on
and see if it explodes. If these pass, the project structure is
sound and imports are working correctly.

These tests don't check any business logic (there isn't any yet).
They just confirm:
  1. The app factory can be imported and called
  2. It returns something that looks like a Flask app
  3. The app can handle a basic request without crashing
"""

import pytest
from app import create_app


@pytest.fixture
def app():
    """
    Create a test instance of the Flask app.

    A pytest "fixture" is a reusable setup function. By naming this
    function `app` and marking it with @pytest.fixture, pytest will
    automatically call it and pass the result to any test function
    that lists `app` as a parameter.

    We pass a minimal test config override to make sure tests don't
    accidentally depend on your local .env file.
    """

    class TestConfig:
        TESTING = True
        SECRET_KEY = "test-secret-key"
        ANTHROPIC_API_KEY = None
        GENERATED_SITES_DIR = "/tmp/siteseed_test"

    app = create_app(config_class=TestConfig)
    return app


@pytest.fixture
def client(app):
    """
    Create a test client for making HTTP requests to the app.

    Flask's test client lets you simulate GET/POST requests without
    running a real server. `app.test_client()` returns one.
    """
    return app.test_client()


def test_app_factory_returns_flask_app(app):
    """create_app() should return a Flask application object."""
    from flask import Flask
    assert isinstance(app, Flask), "create_app() did not return a Flask instance"


def test_index_route_returns_200(client):
    """GET / should return HTTP 200 OK."""
    response = client.get("/")
    assert response.status_code == 200, (
        f"Expected status 200, got {response.status_code}"
    )


def test_index_page_contains_siteseed(client):
    """The home page should mention SiteSeed."""
    response = client.get("/")
    assert b"SiteSeed" in response.data, (
        "Expected 'SiteSeed' in the response body, but it wasn't found"
    )
