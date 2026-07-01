import httpx

from app.schemas.paper import Paper

CROSSREF_WORKS_URL = "https://api.crossref.org/works"


async def search_crossref(query: str, max_results: int = 5) -> list[Paper]:
    params = {
        "query": query,
        "rows": max_results,
    }

    async with httpx.AsyncClient(timeout=20) as client:
        response = await client.get(CROSSREF_WORKS_URL, params=params)
        response.raise_for_status()
        data = response.json()

    items = data.get("message", {}).get("items", [])
    papers: list[Paper] = []

    for item in items:
        title_list = item.get("title") or []
        authors = [
            " ".join(filter(None, [author.get("given"), author.get("family")]))
            for author in item.get("author", [])
        ]
        issued = item.get("issued", {}).get("date-parts", [[None]])
        year = issued[0][0] if issued and issued[0] else None

        papers.append(
            Paper(
                title=title_list[0] if title_list else "Untitled",
                authors=authors,
                year=year,
                venue=(item.get("container-title") or [None])[0],
                doi=item.get("DOI"),
                abstract=item.get("abstract"),
                source="Crossref",
                url=item.get("URL"),
            )
        )

    return papers
