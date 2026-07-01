# Backend

PsyScholar AI backend, FastAPI ile geliştirilecektir.

## Lokal Çalıştırma

1. `cd backend`
2. Python virtual environment oluştur.
3. `pip install -r requirements.txt`
4. `uvicorn app.main:app --reload`

## İlk Endpointler

- `GET /health`
- `POST /api/v1/research/query`

## Amaç

Backend ilk aşamada kullanıcı promptunu alacak, akademik kaynak servislerinden ilgili makaleleri arayacak ve normalize edilmiş sonuçları döndürecektir.
