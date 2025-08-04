# 🎓 EduAssist - Yapay Zekâ Destekli Eğitim Asistanı

EduAssist, öğrencilerin öğrenme sürecini kolaylaştırmak için geliştirilmiş çok sayfalı, yapay zekâ destekli bir web uygulamasıdır. Kullanıcılar konu anlatımı alabilir, soru çözümleri yapabilir, eksiklerini tespit edebilir ve forum üzerinden soru paylaşabilir.

---

## 🎯 Uygulamanın Amacı

EduAssist, öğrencilerin bireysel olarak:

- Konuları sade ve detaylı şekilde öğrenmesine
- Soru çözüm süreçlerini adım adım analiz etmesine
- Eksik olduğu alanları tespit etmesine
- Forum aracılığıyla başkalarıyla etkileşime geçmesine olanak tanır.

---

## 👤 Hedef Kullanıcılar

- Lise ve üniversite öğrencileri
- Tekrar yaparak eksiklerini görmek isteyen bireyler
- Sınavlara hazırlanan öğrenciler
- Konu anlatımına ihtiyaç duyan herkes

---

## 🛠️ Proje Özellikleri

- ✅ Yapay zekâ destekli konu anlatımı (Gemini API ile)
- ✅ Soru çözüm desteği
- ✅ Eksik tespiti (AI bazlı zayıf konular)
- ✅ Forum sayfası: Soru paylaşma, beğeni, yorum, kaydetme
- ✅ Şifre sıfırlama özelliği (e-posta üzerinden)
- ✅ Dinamik kullanıcı profili sayfası
- ✅ Türkçe ve İngilizce dil desteği (tercihli)

---

## 🧠 Kullanılan Teknolojiler

- **Backend:** FastAPI
- **Frontend:** HTML, CSS, JavaScript (Vanilla)
- **Database:** SQLAlchemy
- **AI API:** Gemini Pro (Google)
- **Mail Servisi:** Gmail SMTP (şifre sıfırlama)
- **Deployment:** Lokal çalıştırma (uvicorn)
  
---

## 🚀 Projeyi Çalıştırma Adımları

Aşağıdaki adımları izleyerek uygulamayı kendi bilgisayarınızda çalıştırabilirsiniz:

### 1. 📦 Gerekli Paketleri İndirin

İlk olarak sanal ortamı aktif edip bağımlılıkları yükleyin:

```bash
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. 🔑 Gemini API Anahtarınızı Alın

Uygulama, yapay zekâ yanıtlarını almak için Google'ın **Gemini API** servisinden faydalanır.

- Ücretsiz bir API anahtarı almak için [buraya tıklayın](https://makersuite.google.com/app/apikey).
- `.env` dosyası oluşturun ve içine aşağıdaki satırı ekleyin:

```
GEMINI_API_KEY=your_api_key_here
```

### 3. ⚙️ Uygulamayı Başlatın

```bash
uvicorn main:app --reload
```

Tarayıcıda [http://localhost:8000](http://localhost:8000) adresine giderek uygulamayı başlatabilirsiniz.

---

## 👩‍💻 Geliştiriciler

| İsim | Rol |
|------|-----|
| [İpek Gültekin](https://github.com/ipekgultekin) | Developer |
| [Yusuf Mert Genç](https://github.com/YusufMertGenc) | Product Owner, Developer |

---

## 🔗 Proje Bağlantısı

📂 GitHub Repository: [https://github.com/ipekgultekin/Hackathon](https://github.com/ipekgultekin/Hackathon)

---

## 📄 Lisans

Bu proje açık kaynaklıdır ve MIT lisansı ile lisanslanmıştır.
