"""
app/models/business_profile.py — BusinessProfile class stub.

STATUS: Stub only. Full implementation is a Phase 2 + Phase 3
owner-built exercise. Do not add logic here until instructed.
"""


class BusinessProfile:
    """
    Represents a small business and all the information SiteSeed
    needs to generate a preview website for it.

    This is the data backbone of SiteSeed. Every other class
    (ContentGenerator, Template, PreviewSite) receives a
    BusinessProfile and uses its data to do its job.

    Planned attributes (Phase 2):
        business_name (str): The name of the business.
        owner_name (str): The name of the business owner.
        industry (str): The type of business (e.g., "plumbing").
        location (str): City or region the business operates in.
        services (list): Services the business offers.
        tone (str): Desired personality of the site copy
                    (e.g., "friendly", "professional").
        contact_info (dict): Phone, email, website, etc.

    Planned methods (Phase 3):
        validate(): Check that required fields are present.
        to_dict(): Serialize the profile to a dictionary.
        from_dict(): Class method to rebuild from a dictionary.
        __repr__(): Readable string representation.

    Built by: Owner (Phase 2 & 3) with Claude (chat) as tutor.
    """

    pass
