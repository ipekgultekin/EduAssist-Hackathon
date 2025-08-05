# 🎓 EduAssist - Yapay Zekâ Destekli Eğitim Asistanı

**EduAssist**, öğrencilerin bireysel öğrenme süreçlerini destekleyen çok sayfalı, modern ve yapay zekâ tabanlı bir web uygulamasıdır. Kullanıcılar, konuları yapay zekâdan dinleyebilir, sorularını çözümletip açıklamalar alabilir, eksik olduğu alanları analiz edebilir ve diğer kullanıcılarla forum üzerinden etkileşim kurabilir.

---

## 🎯 Projenin Amacı

EduAssist, eğitimde kişiselleştirilmiş destek sağlamak amacıyla geliştirilmiştir. Uygulama sayesinde:

- Öğrenciler, zorlandıkları konuları yapay zekâdan sade ve açıklayıcı şekilde öğrenebilir.
- Sınav sorularının çözüm mantığını adım adım analiz edebilir.
- AI destekli testlerle hangi konularda eksikleri olduğunu belirleyebilir.
- Forum sayfası aracılığıyla sorularını paylaşabilir, beğeni ve yorum alabilir.

---

## 👤 Hedef Kullanıcılar

- Lise ve üniversite öğrencileri  
- KPSS, YKS, ALES gibi sınavlara hazırlanan bireyler  
- Akademik konuları tekrar etmek isteyen kullanıcılar  
- Yapay zekâdan yardım alarak öğrenmek isteyen herkes  

---

## 🌟 Öne Çıkan Özellikler

| Özellik | Açıklama |
|--------|----------|
| ✅ **Konu Anlatımı** | Kullanıcı, istediği konunun sade bir şekilde AI tarafından anlatılmasını talep edebilir. |
| ✅ **Soru Çözümü** | AI, verilen soruları detaylıca çözerek açıklamalı şekilde sunar. |
| ✅ **Eksik Tespiti** | AI, kullanıcıya 5 soruluk mini test yapar. Cevaplara göre eksik konuları analiz eder. |
| ✅ **Forum** | Kayıtlı kullanıcılar soru paylaşabilir, yorum yapabilir, beğeni bırakabilir ve içerikleri kaydedebilir. |
| ✅ **Profil Sayfası** | Kullanıcılar geçmiş etkinliklerini görüntüleyebilir. |

---

## 🧠 Kullanılan Teknolojiler

- **Backend:** FastAPI (Python)
- **Frontend:** HTML, CSS, JavaScript (Vanilla)
- **Database:** SQLAlchemy (ORM) + SQLite
- **AI API:** Gemini Pro (Google)
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

## 📸 Uygulama Görselleri
<img width="1897" height="867" alt="Ekran görüntüsü 2025-08-05 232709" src="https://github.com/user-attachments/assets/4293466f-0e78-4ac3-ae8a-06045eaeaa9b" />
<img width="1895" height="856" alt="Ekran görüntüsü 2025-08-05 234053" src="https://github.com/user-attachments/assets/c479a123-cf87-42d9-aa93-3b12e13df7ef" />
<img width="1890" height="843" alt="Ekran görüntüsü 2025-08-05 234110" src="https://github.com/user-attachments/assets/d9d56ca2-7114-4a00-b287-d47d2b0f905b" />
<img width="1900" height="853" alt="Ekran görüntüsü 2025-08-05 233830" src="https://github.com/user-attachments/assets/2df2df0b-e77b-40f7-92d2-8083d22d5b02" />
<img width="1895" height="853" alt="Ekran görüntüsü 2025-08-05 233922" src="https://github.com/user-attachments/assets/d92af4de-9a24-43e5-b79e-1983353142d4" />
<img width="1892" height="850" alt="Ekran görüntüsü 2025-08-05 233940" src="https://github.com/user-attachments/assets/68673138-2e43-49de-9f2c-da4eaddecdc4" />
<img width="1918" height="856" alt="Ekran görüntüsü 2025-08-05 233357" src="https://github.com/user-attachments/assets/e88954e0-ea8f-47b3-b201-e7d17dcebe64" />

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
