# 🎶 Ruh Hali Önerici (RuhHaliOnerici)

Bu proje, kullanıcının o anki ruh halini seçmesine göre dinamik olarak **müzik ve aktivite önerileri** sunan bir Streamlit uygulamasıdır. Kullanıcı etkileşimlerini takip etmek amacıyla tüm ruh hali seçimleri ve öneriler bir Excel dosyasına kaydedilerek kişisel bir geçmiş günlüğü oluşturulur.

## 🌟 Özellikler

* **Ruh Hali Tespiti:** Kullanıcının mevcut ruh halini (mutlu, üzgün, enerjik vb.) seçebilmesi.
* **Akıllı Öneri Sistemi:** Seçilen ruh haline özel olarak belirlenmiş müzik türlerini ve uygun aktiviteleri (spor, okuma, dinlenme vb.) anlık olarak önerme.
* **Geçmiş Kaydı (Loglama):** Kullanıcının her bir seçimini ve aldığı öneriyi tarih/saat bilgisiyle birlikte otomatik olarak bir Excel dosyasına (`gecmis_log.xlsx`) kaydetme.
* **Kullanıcı Dostu Arayüz:** Streamlit kütüphanesi sayesinde basit, hızlı ve etkileşimli bir web arayüzü sunma.
* **Esnek Yapı:** İstenildiğinde yeni ruh halleri, müzik ve aktivite eşleştirmelerinin kolayca sisteme dahil edilebilmesi.

## 🚀 Kurulum ve Çalıştırma

Bu projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları takip edin.

### 1. Ön Gereksinimler

* Python 3.10 veya üzeri kurulu olmalıdır.

### 2. Gerekli Paketleri Yükleme

Projenin bağımlılıklarını yüklemek için terminalinizde aşağıdaki komutu çalıştırın:

```bash
pip install streamlit pandas openpyxl
