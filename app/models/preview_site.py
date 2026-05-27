"""
app/models/preview_site.py — PreviewSite class stub.

STATUS: Stub only. Full implementation is Phase 8 (Claude Code).
Do not add logic here until instructed.
"""


class PreviewSite:
    """
    The orchestrator. Combines a BusinessProfile, ContentGenerator,
    and Template to produce a finished preview website.

    PreviewSite is the glue that connects all other classes. It
    takes the business data, passes it through the AI content
    pipeline, feeds the result into a template, writes the output
    to disk, and provides a Flask route so the result can be viewed
    in a browser.

    Data flow this class manages:
        BusinessProfile → ContentGenerator → Template → HTML files
        on disk → Flask route → shareable preview URL

    Planned interface (Phase 8):
        __init__(profile, template_name): Set up with a profile
            and a chosen template.
        generate(): Run the full pipeline. Call ContentGenerator,
            render the Template, write files to generated_sites/.
        get_url(): Return the local Flask URL to view the preview.
        preview_exists(): Check whether a preview has already been
            generated for this profile.

    Built by: Claude Code (Phase 8).
    """

    pass
