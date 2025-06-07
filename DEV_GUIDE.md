# 📘 Telegram Aşk Botu – Developer Guide (Yalnızca Yapı ve Mantık)

## 🌟 Amaç

Bu bot, Oğuz tarafından sevgilisi Tuanna için özel olarak geliştirilecektir.
Amaç; Tuanna'ya sevgi dolu, etkileşimli, eğlenceli ve romantik bir deneyim yaşatmaktır.
Bot, aşağıdaki gibi birden fazla "mod" içerecektir:

* Aşk dolu sabit mesajlar
* Rastgele övgüler
* Mini oyunlar
* Emoji hikaye tamamlatma
* Kombin önerileri
* Şiir üretimi

Bot, modüler bir yapıda inşa edilecek ve Railway'e deploy edilecektir.

---

## 🧱‍🏫 Proje Yapısı

```
lovebot/
├── bot.py                  # Ana başlangıç noktası (entry point)
├── config/
│   └── settings.py         # Token ve ortam değişkeni yükleyici
├── handlers/
│   ├── start.py            # /start komutu
│   ├── love_check.py       # "Oğuz beni seviyor mu?" modu
│   ├── love_rate.py        # "Oğuz ne kadar seviyor?" modu
│   ├── guess_number.py     # Sayı tahmini mini oyunu
│   ├── role_switch.py      # Rol değiştirme oyunu
│   └── emoji_story.py      # Emoji hikaye tamamlama
├── core/
│   ├── messages.py         # Sabit mesajlar ve içerik üreticiler
│   └── utils.py            # Ortak yardımcı fonksiyonlar
├── .env                    # Gizli bilgiler (token)
├── requirements.txt        # Gerekli kütüphaneler
├── Procfile                # Railway çalıştırıcı
└── README.md               # Proje açıklaması
```

---

## ⚙️ Modül Açıklamaları

### `bot.py`

* `Application` başlatılır.
* Tüm `handlers/` içindeki komutlar ve fonksiyonlar buraya bağlanır.
* `run_polling()` ile çalışır.

### `config/settings.py`

* `.env` dosyasından token ve ayarlar okunur.
* `os.getenv()` içerir.

### `handlers/` (Komut Modülleri)

Her `.py` dosyası bir komut içerir ve şu kuralları takip eder:

* `async def command(update, context):` fonksiyonu vardır.
* İçeriği sabit mesaj veya `core/` içindeki içerik üreticilerden gelir.
* `CommandHandler` ile `bot.py`'ye bağlanır.

#### Örnekler:

* `love_check.py` → `/seviyormu`
* `love_rate.py` → `/nekadarseviyor`
* `guess_number.py` → `/sayitahmin`
* `role_switch.py` → `/roldegistir`
* `emoji_story.py` → `/hikaye`
* `outfit_suggestion.py` → `/kombin`

### `core/messages.py`

* Sabit içerikler burada tutulur.
* Rastgele övgüler, şiirler, sevgi yüzdeleri bu dosyadan çekilir.

### `core/utils.py`

* Mini yardımcılar: emoji formatlama, random seçim gibi
* Ortak işlemler burada merkezi olarak yazılır.

---

## 🌐 Railway İçin Dosyalar

### `.env`

```env
BOT_TOKEN=your_botfather_token_here
```

### `Procfile`

```
web: python bot.py
```

---

## 🧪 Geliştirme ve Test Akışı

1. Yeni bir özellik eklemek istiyorsan:

   * Yeni komutu `handlers/` içinde oluştur.
   * İlgili mesajları `core/messages.py`'ye ekle.
   * Komutu `bot.py` içinde handler olarak bağla.

2. Yeni komut için:

   * `CommandHandler("komut", function)` tanımı yapılır.
   * Mod ismine uygun klasör yapısı korunur.

---

## 🚀 Deployment (Railway)

1. GitHub’a bu dosya yapısını yükle.
2. Railway üzerinden “New Project → Deploy from GitHub” adımlarını takip et.
3. `.env` içeriğini Railway panelinden manuel olarak gir.
4. Railway otomatik olarak `Procfile`ı okuyarak botu başlatır.

---

## ✅ Geliştirme İlkeleri (Copilot için uygun yapı)

* Modüler küçük, net ve test edilebilir olmalı.
* İçerik üreticileri ayrı dosyada tutulmalı (Copilot hızlı tamamlar).
* Her mesaj fonksiyonu async olmalı.
* Sadece `handlers/` içindeki fonksiyonlar komutla çağrılmalı.
* `core/` içerisindeki metinler kolayca genişletilebilir olmalı (Copilot’un öneri kalitesi artar).

---

## 🧠 Bonus: Genişletilebilir Fikirler

* `scheduler/` klasörü ekleyerek günlük mesaj saatleri belirlenebilir.
* `database/` klasörü ekleyerek sqlite ile kişiye özel puanlama tutulabilir.
* `assets/` klasörü ile ses, fotoğraf vs. medya desteği eklenebilir.
