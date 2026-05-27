"""
app/models/template.py — Template class stub.

STATUS: Stub only. Full implementation is Phase 6 (Claude Code).
Do not add logic here until instructed.
"""


class Template:
    """
    Represents a site template — a self-contained HTML/CSS design
    that can be populated with generated content to produce a
    finished preview website.

    Multiple templates will exist (generic, trades, food, etc.).
    A registry pattern lets new templates be added simply by
    dropping a folder into `site_templates/`. The Template class
    knows how to discover, load, and render any of them.

    Planned interface (Phase 6):
        __init__(template_name): Load a template by name from
            the site_templates/ directory.
        render(content_dict): Accept generated content from
            ContentGenerator, inject it into the HTML/CSS, and
            return the finished markup as a string.
        list_available(): Class method that returns all template
            names found in site_templates/.

    Built by: Claude Code (Phase 6).
    """

    pass
