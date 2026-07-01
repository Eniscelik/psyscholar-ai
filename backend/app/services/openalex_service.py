import httpx

from app.config import settings
from app.schemas.paper import Paper

OPENALEX_WORKS_URL = "https://api.openalex.org/works"


async def search_openalex(query: str, max_results: int = 5) -> list[Paper]:
    params: dict[str, str | int] = {
        "search": query,
        "per-page": max_results,
    }

    if settings.openalex_email:
        params["mailto"] = settings.openalex_email

    async with httpx.AsyncClient(timeout=20) as client:
        response = await client.get(OPENALEX_WORKS_URL, params=params)
        response.raise_for_status()
        data = response.json()

    papers: list[Paper] = []
    for item in data.get("results", []):
        authorships = item.get("authorships", [])
        authors = [
            authorship.get("author", {}).get("display_name")
            for authorship in authorships
            if authorship.get("author", {}).get("display_name")
        ]

        primary_location = item.get("primary_location") or {}
        source = primary_location.get("source") or {}

        papers.append(
            Paper(
                title=item.get("display_name") or "Untitled",
                authors=authors,
                year=item.get("publication_year"),
                venue=source.get("display_name"),
                doi=item.get("doi"),
                abstract=None,
                source="OpenAlex",
                url=item.get("id"),
            )
        )

    return papers
