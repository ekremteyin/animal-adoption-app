
# 🐾 HiPet - Hayvanlar İçin Yardımlaşma Platformu

HiPet, Django framework'ü kullanılarak geliştirilmiş açık kaynaklı bir web uygulamasıdır. Proje; sahipsiz hayvanlar için sahiplendirme, mama yardımı ve sağlık desteği gibi temel ihtiyaçların karşılanmasını kolaylaştırmayı hedefler.

## 🔧 Özellikler

- 🐕 **Sahiplendirme Modülü:** Hayvanları sahiplenmek isteyen kullanıcılarla buluşturur.
- 🥫 **Mama Yardımı:** Gönüllü kullanıcılar mama bağışında bulunabilir.
- 💉 **Sağlık Desteği:** Veteriner yardımı veya sağlık harcamaları için destek başvuruları.
- 👤 **Kullanıcı Yönetimi:** Kayıt, giriş ve yetkilendirme sistemleri.
- 📬 **Yönetici Paneli:** Django admin paneli ile kullanıcı ve içerik yönetimi.

## 🚀 Kurulum Talimatları

## 1. Depoyu Klonlayın
```bash
git clone https://github.com/ekremteyin/animal-adoption-app.git
cd animal-adoption-app/HiPet


## 2. Sanal Ortam Oluşturun ve Aktifleştirin
 ```bash
python -m venv env
env\Scripts\activate  # macOS/Linux: source env/bin/activate

## 3. Gereksinimleri Yükleyin
```bash
pip install -r requirements.txt

## 4. Veritabanını Başlatın
```bash
python manage.py migrate

## Geliştirme Sunucusunu Başlatın
python manage.py runserver

## Admin Paneli
python manage.py createsuperuser

## ⚙️ Gereksinimler
**Python 3.10+**

**Django 4.x**

**SQLite (varsayılan veritabanı)**

**pip (Python paket yöneticisi)**

