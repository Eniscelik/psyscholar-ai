# Product Requirements Document

## 1. Ürün Tanımı

PsyScholar AI, psikoloji alanında akademik kaynaklara dayalı bilgiye erişimi kolaylaştıran web tabanlı yapay zekâ destekli araştırma asistanıdır.

Uygulama, kullanıcının doğal dilde yazdığı soruları akademik literatür, psikometrik test çalışmaları, kuramsal yaklaşımlar ve psikopatoloji sınıflandırmaları çerçevesinde analiz eder. Cevaplar yalnızca genel bilgi olarak değil; kaynak, yazar, yayın yılı, çalışma tipi, temel argüman, yöntem, bulgu, sınırlılık ve alternatif görüşlerle birlikte sunulur.

## 2. Hedef Kullanıcılar

- Psikoloji lisans öğrencileri
- Klinik psikoloji yüksek lisans ve doktora öğrencileri
- Akademisyenler
- Araştırma görevlileri
- Tez, makale veya literatür taraması hazırlayan kullanıcılar
- Psikometrik testler hakkında akademik bilgi arayan profesyoneller
- Ruh sağlığı alanında çalışan ancak klinik karar yerine literatür desteği arayan kullanıcılar

## 3. Temel Problem

Psikoloji alanındaki akademik literatür geniş, parçalı ve çoğu zaman farklı kuramsal yaklaşımlara bölünmüş durumdadır. Kullanıcılar güvenilir kaynak bulmak, kaynakları hızlı anlamlandırmak, tez ve anti-tezleri karşılaştırmak ve psikometrik testleri bilimsel sınırlar içinde değerlendirmek için zaman kaybeder.

## 4. Ürün Yaklaşımı

Temel ilke: **Önce kaynak, sonra cevap.**

Sistem, modelin yalnızca kendi hafızasına dayanarak cevap vermesi yerine akademik veri kaynaklarından ilgili çalışmaları bulur. Daha sonra bu kaynakları özetler ve kullanıcıya yapılandırılmış akademik cevap üretir.

## 5. İlk MVP Özellikleri

1. Prompt ile akademik soru sorma
2. Akademik makale arama
3. Makale metadata ve abstract gösterimi
4. Makale özetleme
5. Tez / anti-tez karşılaştırması
6. Psikometrik test açıklama modu
7. Psikopatoloji akademik rehber modu
8. APA 7 kaynakça formatı

## 6. Ürün Dışı Kapsam

Sistem aşağıdakileri yapmaz:

- Tanı koymaz
- Terapi veya tedavi önerisi vermez
- Kullanıcının yazısından patolojik etiketleme yapmaz
- Lisanslı test maddelerini paylaşmaz
- Test puanlama anahtarını vermez
- Klinik karar yerine geçmez

## 7. Başarı Kriterleri

- Kullanıcı psikoloji alanındaki sorusuna kaynaklı cevap alabilir.
- Cevaplarda kaynak adı, yazar, yıl ve DOI bilgisi sunulur.
- Psikometrik testlerde test güvenliği korunur.
- Patolojik konularda tanı koymadan akademik açıklama yapılır.
- Farklı kuramsal görüşler dengeli biçimde gösterilir.
