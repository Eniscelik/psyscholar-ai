from fastapi import APIRouter

from app.schemas.research import ResearchQueryRequest, ResearchQueryResponse
from app.services.ai_answer_service import build_draft_academic_answer
from app.services.crossref_service import search_crossref
from app.services.openalex_service import search_openalex
from app.services.pubmed_service import search_pubmed

router = APIRouter(prefix="/research", tags=["research"])


@router.post("/query", response_model=ResearchQueryResponse)
async def research_query(payload: ResearchQueryRequest) -> ResearchQueryResponse:
    openalex_results = await search_openalex(payload.query, payload.max_results)
    crossref_results = await search_crossref(payload.query, payload.max_results)
    pubmed_results = await search_pubmed(payload.query, payload.max_results)

    papers = [*openalex_results, *crossref_results, *pubmed_results]
    draft_answer = build_draft_academic_answer(payload.query, papers[: payload.max_results])

    return ResearchQueryResponse(
        query=payload.query,
        papers=papers[: payload.max_results],
        draft_answer=draft_answer,
    )
