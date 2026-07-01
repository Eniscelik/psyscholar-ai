from pydantic import BaseModel, Field

from app.schemas.paper import Paper


class ResearchQueryRequest(BaseModel):
    query: str = Field(..., min_length=3)
    max_results: int = Field(default=5, ge=1, le=20)


class ResearchQueryResponse(BaseModel):
    query: str
    papers: list[Paper]
    draft_answer: str | None = None
