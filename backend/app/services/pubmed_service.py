from app.schemas.paper import Paper


async def search_pubmed(query: str, max_results: int = 5) -> list[Paper]:
    """PubMed integration placeholder.

    PubMed will be added with NCBI E-utilities in a later step.
    For MVP skeleton, this function keeps the service interface stable.
    """
    return []
