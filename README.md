# PsyScholar AI

PsyScholar AI, psikoloji alanında akademik kaynaklara dayalı araştırma, literatür tarama, psikometrik test açıklama ve kuramsal görüş karşılaştırması yapmak için tasarlanan web tabanlı yapay zekâ asistanıdır.

Bu proje, psikoloji öğrencileri, akademisyenler, araştırmacılar ve ruh sağlığı profesyonellerinin akademik literatürde daha hızlı ve güvenilir şekilde yol bulmasını hedefler.

## Temel İlke

**Önce kaynak, sonra cevap.**

Sistem, kullanıcının sorduğu psikoloji konusuyla ilgili akademik kaynakları bulur, bu kaynakların yazarlarını, yayın bilgilerini, temel argümanlarını, yöntemlerini, bulgularını ve sınırlılıklarını analiz eder. Ardından kaynaklı, dengeli ve akademik bir cevap üretir.

## Ürün Kapsamı

İlk MVP aşağıdaki yeteneklere odaklanır:

- Prompt ile akademik psikoloji sorusu sorma
- Akademik makale bulma ve özetleme
- Tez / anti-tez karşılaştırması yapma
- Psikometrik testleri akademik olarak açıklama
- Psikopatoloji konularını tanı koymadan akademik çerçevede açıklama
- APA 7 formatında kaynakça üretme

## Yapmayacakları

Bu uygulama aşağıdaki amaçlarla kullanılmayacaktır:

- Klinik tanı koymak
- Terapi yapmak
- Kullanıcıyı psikolojik olarak etiketlemek
- Lisanslı psikometrik test maddelerini paylaşmak
- Test puanlama anahtarlarını vermek
- Klinik karar veya uzman değerlendirmesi yerine geçmek

## Planlanan Teknik Yapı

- Frontend: Next.js / React
- Backend: Python FastAPI
- Database: PostgreSQL
- Vector Search: pgvector
- Academic Sources: OpenAlex, Crossref, PubMed
- AI Architecture: RAG tabanlı kaynaklı cevap üretimi

## Klasör Yapısı

```text
psyscholar-ai/
├── docs/
├── backend/
│   └── app/
└── frontend/
```

## İlk Hedef

İlk hedef, basit bir API üzerinden şu akışı çalıştırmaktır:

```text
Kullanıcı prompt yazar
↓
Backend akademik kaynak arar
↓
Makale bilgileri normalize edilir
↓
Yapay zekâ kaynaklı akademik cevap üretir
↓
Kullanıcıya özet, karşıt görüşler, sınırlılıklar ve kaynakça sunulur
```

## Durum

Proje başlangıç aşamasındadır. İlk fazda ürün dokümantasyonu, backend iskeleti ve akademik kaynak entegrasyonları hazırlanacaktır.
