from app.schemas.paper import Paper


def build_draft_academic_answer(query: str, papers: list[Paper]) -> str:
    """Temporary deterministic draft answer.

    The real LLM-based RAG answer generation will be added after academic
    source search is stable.
    """
    if not papers:
        return (
            "Bu konuda ilk aramada yeterli akademik kaynak bulunamadı. "
            "Daha dar bir konu, test adı, kuram adı veya anahtar kelime ile tekrar aranmalıdır."
        )

    source_lines = []
    for index, paper in enumerate(papers, start=1):
        author_text = ", ".join(paper.authors[:3]) if paper.authors else "Yazar bilgisi yok"
        source_lines.append(
            f"{index}. {paper.title} — {author_text}, {paper.year or 'yıl yok'}"
        )

    return (
        "Kısa akademik özet taslağı:\n"
        f"'{query}' sorusu için bulunan ilk akademik kaynaklar aşağıdadır. "
        "Bir sonraki fazda bu kaynaklar yöntem, bulgu, sınırlılık ve tez/anti-tez formatında özetlenecektir.\n\n"
        + "\n".join(source_lines)
    )
