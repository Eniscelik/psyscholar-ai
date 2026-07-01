# MVP Scope

## MVP Amacı

İlk sürümün amacı, kullanıcının psikoloji alanında yazdığı akademik soruya karşılık ilgili kaynakları bulmak ve bu kaynaklara dayalı yapılandırılmış cevap üretmektir.

## MVP Kullanıcı Akışı

1. Kullanıcı prompt yazar.
2. Backend promptu alır.
3. Soru tipi sınıflandırılır.
4. OpenAlex, Crossref ve PubMed gibi kaynaklardan ilgili çalışmalar aranır.
5. Makale metadata bilgileri normalize edilir.
6. Sistem akademik cevap formatında yanıt üretir.
7. Kullanıcı kaynakça, özet, sınırlılık ve karşıt görüşleri görür.

## MVP Modülleri

### 1. Academic Research Query

Kullanıcı doğal dilde akademik soru sorar.

Örnek:

> Kaygılı bağlanma yetişkin romantik ilişkilerde nasıl açıklanır? Temel kaynaklar ve eleştirilerle açıkla.

### 2. Paper Discovery

Sistem konuya uygun akademik kaynakları getirir.

Alanlar:

- title
- authors
- year
- venue
- doi
- abstract
- source
- url

### 3. Academic Answer Generation

Cevap şu formatta üretilir:

1. Kısa akademik özet
2. Kavramsal tanım
3. Temel kaynaklar
4. Bulgular
5. Tez / anti-tez
6. Sınırlılıklar
7. Klinik veya akademik yorum sınırı
8. Sonuç
9. APA kaynakça

### 4. Psychometric Test Explanation

Test maddesi paylaşmadan, testin akademik kullanımını açıklar.

### 5. Clinical Safety Guardrail

Tanı koymayı, terapi önerisini ve kullanıcıyı etiketlemeyi engeller.

## MVP Dışı Bırakılanlar

- Kullanıcı hesabı ve abonelik sistemi
- PDF upload ve PDF tam metin analizi
- Gelişmiş frontend tasarımı
- Çoklu dil desteği
- Kurumsal admin paneli
- Klinik rapor üretimi

## MVP Tamamlanma Kriteri

MVP, aşağıdaki uçtan uca akış çalıştığında tamamlanmış sayılır:

```text
Prompt → kaynak arama → makale listesi → kaynaklı akademik cevap
```
