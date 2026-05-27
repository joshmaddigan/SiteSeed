"""
app/models/content_generator.py — ContentGenerator class stub.

STATUS: Stub only. Full implementation is Phase 5 (Claude Code).
Do not add logic here until instructed.
"""


class ContentGenerator:
    """
    Wraps the Anthropic Claude API to generate website copy for
    a small business.

    Receives a BusinessProfile and uses its data to craft prompts
    that produce tailored content: headlines, taglines, service
    descriptions, about-us blurbs, and calls to action.

    Planned interface (Phase 5):
        __init__(api_key): Initialize with the Anthropic API key.
        generate(profile): Accept a BusinessProfile, return a
            dictionary of generated content keyed by content type
            (e.g., {"headline": "...", "services": [...]}).

    This class is responsible for all communication with the
    Anthropic API. If the API is unavailable or returns an error,
    this is where that gets caught and surfaced clearly.

    Built by: Claude Code (Phase 5).
    """

    pass
