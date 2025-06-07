# 💕 Telegram Aşk Botu

Sevgiliniz için özel olarak tasarlanmış romantik Telegram botu. Bu proje örnek olarak **Oğuz** ve **Tuanna** için geliştirilmiştir, ancak herkes kendi isimlerini değiştirerek kullanabilir.

## ✨ Kişiselleştirme

Bu bot **tamamen kişiselleştirilebilir**! `config/settings.py` dosyasında sadece isimleri değiştirerek kendi sevgiliniz için kullanabilirsiniz:

```python
OWNER_NAME = "Sizin_Adınız"      # Örnek: "Ahmet", "Can", "Mert"
BELOVED_NAME = "Sevgilinizin_Adı" # Örnek: "Ayşe", "Elif", "Zeynep"
```

Bu değişiklik yapıldıktan sonra tüm mesajlar otomatik olarak sizin isimlerinizle gelecektir!

## 🌟 Özellikler

### 💬 Ana Komutlar
- `/start` - Botu başlat ve komut listesini gör
- `/seviyormu` - "Beni seviyor mu?" sorusunun cevabı
- `/nekadarseviyor` - Aşk yüzdesini öğren (her zaman %100! + bonus şiir)
- `/sayitahmin` - Eğlenceli sayı tahmin oyunu (1-10 arası)
- `/roldegistir` - Romantik rol yapma oyunları
- `/hikaye` - Emoji hikaye tamamlama
- `/kombin` - Günlük kombin önerileri (kıskançlık uyarıları ile! 😤💕)

### 🎮 Özel Özellikler
- **Akıllı Oyun Sistemi**: Sayı tahmin oyununda oturum yönetimi
- **Dinamik İçerik**: Her seferinde farklı mesajlar ve şiirler
- **Kişiselleştirilmiş Deneyim**: Sevgilinize özel romantik içerikler
- **Etkileşimli Yanıtlar**: Typing efektleri ve gecikmeli mesajlar
- **Emoji Zenginliği**: Her mesajda sevgi dolu emojiler
- **Kolay Kişiselleştirme**: `config/settings.py` ile isim değişiklikleri

## 🏗️ Teknik Yapı

### Proje Yapısı
```
lovebot/
├── bot.py                  # Ana başlangıç noktası
├── config/
│   └── settings.py         # Konfigürasyon ve isim ayarları (KİŞİSELLEŞTİRME BURADAN!)
├── handlers/               # Komut handler'ları
│   ├── start.py           # /start komutu
│   ├── love_check.py      # /seviyormu komutu
│   ├── love_rate.py       # /nekadarseviyor komutu
│   ├── guess_number.py    # /sayitahmin oyunu
│   ├── role_switch.py     # /roldegistir komutu
│   ├── emoji_story.py     # /hikaye komutu
│   └── outfit_suggestion.py # /kombin komutu
├── core/
│   ├── messages.py        # Tüm mesaj içerikleri
│   └── utils.py          # Yardımcı fonksiyonlar
├── .env                   # Bot token'ı
├── requirements.txt       # Python bağımlılıkları
└── Procfile              # Railway deployment
```

### Kullanılan Teknolojiler
- **Python 3.9+**
- **python-telegram-bot 20.7**: Modern async Telegram bot framework'ü
- **python-dotenv**: Çevre değişkeni yönetimi
- **asyncio**: Asenkron programlama

## 🚀 Kurulum

### 1. İsimleri Kişiselleştirin
`config/settings.py` dosyasını açıp isimleri değiştirin:
```python
OWNER_NAME = "Sizin_Adınız"      # Örnek: "Ahmet"
BELOVED_NAME = "Sevgilinizin_Adı" # Örnek: "Ayşe"
```

### 2. Gereksinimler
```bash
pip install -r requirements.txt
```

### 3. Çevre Değişkenleri
`.env` dosyasını düzenle:
```env
BOT_TOKEN=your_bot_token_from_botfather
DEBUG=False
```

### 4. Yerel Çalıştırma
```bash
python bot.py
```

## 🌐 Railway Deployment

### 1. GitHub'a Yükle
```bash
git init
git add .
git commit -m "Initial commit: Love bot"
git push origin main
```

### 2. Railway'de Deploy Et
1. [Railway](https://railway.app) hesabı oluştur
2. "New Project → Deploy from GitHub" seç
3. Bu repository'yi seç
4. Environment Variables'a `.env` içeriğini ekle
5. Railway otomatik olarak `Procfile`'ı okur ve botu başlatır

### 3. Environment Variables (Railway Panel)
```
BOT_TOKEN=your_actual_bot_token
DEBUG=false
```

## 🎯 Geliştirme Rehberi

### Yeni Komut Ekleme
1. `handlers/` klasöründe yeni dosya oluştur
2. `core/messages.py`'ye mesaj içeriklerini ekle
3. `bot.py`'de handler'ı kaydet

### Örnek Handler Yapısı
```python
async def new_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Yeni komut açıklaması"""
    await update.message.reply_text("Merhaba!", parse_mode='Markdown')
```

### Stil Rehberi
- Her handler `async` olmalı
- Mesajlar `core/messages.py`'de tanımlanmalı
- Emoji kullanımını abartma, ama romantik temas ekle
- Error handling ekle
- Type hints kullan

## 💡 Genişletme Fikirleri

### Gelecekteki Özellikler
- **Scheduler Sistemi**: Günlük otomatik "günaydın" mesajları
- **Veritabanı Entegrasyonu**: Kişisel puanlama ve anılar
- **Medya Desteği**: Ses mesajları, fotoğraflar
- **Hatırlatıcılar**: Özel günler ve etkinlikler
- **Chat Memory**: Sohbet geçmişi ve kişiselleştirme

### Dosya Ekleme Önerileri
```
scheduler/
├── daily_messages.py     # Günlük mesajlar
└── special_dates.py      # Özel günler

database/
├── user_preferences.py  # Kullanıcı tercihleri
└── love_history.py      # Aşk geçmişi

assets/
├── photos/              # Fotoğraf arşivi
└── sounds/              # Ses dosyaları
```

## 👥 Geliştirici Notları

Bu bot özel olarak **Oğuz** ve **Tuanna** için tasarlanmıştır. İçerik tamamen kişiselleştirilmiştir ve başka projeler için kullanılmadan önce mesajların güncellenmesi gerekir.

### Kodlama Prensipleri
- **Modülerlik**: Her özellik ayrı dosyada
- **Okunabilirlik**: Self-documenting kod
- **Bakım Kolaylığı**: Copilot-friendly yapı
- **Ölçeklenebilirlik**: Yeni özellikler kolayca eklenebilir

---

**💕 Bu bot sevgiyle kodlanmıştır. Tuanna'ya özel! 💕**
