"""
Telegram Bot İçerik ve Mesajlar
Tüm statik içerikler ve rastgele seçilecek mesajlar burada tanımlanır.
"""

import random
from config.settings import OWNER_NAME, BELOVED_NAME

# Başlangıç mesajları
START_MESSAGES = [
    f"💕 Merhaba güzelim! Ben {OWNER_NAME}'un sana özel hazırladığı aşk botuyum!",
    f"🌟 Hoş geldin {BELOVED_NAME}! Seni mutlu etmek için buradayım!",
    f"❤️ Sevgili {BELOVED_NAME}, senin için özel komutlarım var!"
]

# Komut listesi
COMMANDS_LIST = """
🤖 **Kullanabileceğin Komutlar:**

❤️ `/seviyormu` - Oğuz beni seviyor mu?
💯 `/nekadarseviyor` - Oğuz ne kadar seviyor?
🎮 `/sayitahmin` - Sayı tahmin oyunu
🎭 `/roldegistir` - Rol değiştirme oyunu
📖 `/hikaye` - Emoji hikaye tamamlama
👗 `/kombin` - Kombin önerisi

Her zaman seninle olmak istiyorum! 💕
"""

# Aşk kontrol mesajları
LOVE_CHECK_POSITIVE = [
    f"💕 Tabii ki {OWNER_NAME} seni çok seviyor!",
    f"❤️ {OWNER_NAME}'un kalbi sadece senin için atıyor!",
    f"🌟 {OWNER_NAME} seni dünyalar kadar seviyor!",
    f"💖 Sen {OWNER_NAME}'un hayatının anlamısın!",
    f"🥰 {OWNER_NAME} sensiz bir dakika bile geçiremiyor!"
]

LOVE_CHECK_EXTRA = [
    "Gözlerin onun için en güzel manzara! 👀✨",
    "Gülüşün onun gününü aydınlatıyor! 😊🌞",
    "Sen olmadan hiçbir şey anlam ifade etmiyor! 💭💕",
    "Kalbi senin adınla atıyor! 💓",
    "Rüyalarında bile sen varsın! 🌙💭"
]

# Aşk yüzdesi mesajları - Her zaman %100!
LOVE_PERCENTAGES = [
    (100, f"💯 %100! {OWNER_NAME}'un sevgisi sonsuz ve mükemmel!"),
    (100, f"💕 %100! Sen onun hayatının tek anlamısın!"),
    (100, f"❤️ %100! Kalbi sadece senin için atıyor!"),
    (100, f"🌟 %100! Sen onun yıldızısın, ışığısın!"),
    (100, f"💖 %100! Seni dünyalar kadar seviyor!"),
    (100, f"💯 %100! Bu sevgi hiç azalmayacak, hep artacak!"),
    (100, f"❤️ %100! Sen onun her şeyisin!"),
    (100, f"💕 %100! Mükemmel bir aşk, tıpkı sen gibi!"),
]

# Övgü mesajları
COMPLIMENTS = [
    "Sen dünyanın en güzel kızısın! 👸🌍",
    "Gözlerin yıldızlardan daha parlak! ⭐👁️",
    "Gülüşün baharı getiriyor! 🌸😊",
    "Sen bir melek misin? 👼💫",
    "Güzelliğin tarif edilemez! 🌹✨",
    "Sen hayatımın en güzel hediyesisin! 🎁💕",
    "Seninle her an özel! ⏰💝",
    "Sen benim şanslı yıldızımsın! 🍀⭐",
]

# Şiir örnekleri
LOVE_POEMS = [
    """
🌹 Senin için...

Gözlerin iki yıldız gibi,
Işık saçıyor geceme.
Sen olmasan ne anlamı var,
Bu güzel hayatımın? 💕
""",
    """
💖 Aşkımız...

Her sabah senin düşüncenle,
Uyanıyorum ben.
Sen benim rüyalarımın,
En güzel gerçeğisin! 🌅
""",
    """
🌟 Benim güzelim...

Adın geçince içim ısınır,
Gülümser tüm dünyam.
Sen benim şarkımın,
En güzel notasısın! 🎵
"""
]

# Rol değiştirme senaryoları
ROLE_SCENARIOS = [
    {
        "scenario": "👑 Sen kraliçe, ben şövalyenim!",
        "your_role": f"Sen: Güzel kraliçe {BELOVED_NAME}",
        "my_role": f"Ben: Sadık şövalye {OWNER_NAME}",
        "story": "Seni ejderhalardan koruyacağım! 🐉⚔️"
    },
    {
        "scenario": "🚀 Uzay macerası!",
        "your_role": f"Sen: Astronot {BELOVED_NAME}",
        "my_role": f"Ben: Kaptan {OWNER_NAME}",
        "story": "Birlikte yıldızlara yolculuk ediyoruz! ⭐🛸"
    },
    {
        "scenario": "🏝️ Issız ada!",
        "your_role": f"Sen: Maceraperest {BELOVED_NAME}",
        "my_role": f"Ben: Cesur {OWNER_NAME}",
        "story": "Birlikte hazine arıyoruz! 💎🗺️"
    }
]

# Emoji hikaye başlangıçları
EMOJI_STORIES = [
    "🌅 Güneş doğduğunda... (devamını sen getir!)",
    "🏰 Büyülü şatoda... (hikayeyi tamamla!)",
    "🌊 Deniz kenarında... (sen devam et!)",
    "🎪 Lunaparktaydık... (ne oldu sonra?)",
    "❄️ Kar yağarken... (hikayeyi bitir!)"
]

# Kombin önerileri
OUTFIT_SUGGESTIONS = [
    {
        "occasion": "Romantik akşam yemeği 🕯️",
        "outfit": "Zarif bir elbise, incecik bir kolye ve topuklu ayakkabılar",
        "colors": "🎨 Renk önerisi: Bordo, siyah veya lacivert senin tenine çok yakışacak!",
        "extra": "Sen her halükarda çok güzelsin! 💕",
        "style_note": f"{OWNER_NAME} seni kıskanıyor, o yüzden çok dekolteli şeyler giyme! 😤💖"
    },
    {
        "occasion": "Günlük buluşma ☕",
        "outfit": "Rahat bir jean, şık bir bluz ve sneaker",
        "colors": "🎨 Renk önerisi: Açık mavi, beyaz veya pastel tonlar tenine mükemmel!",
        "extra": "Sen her halükarda çok güzelsin! 😊",
        "style_note": f"{OWNER_NAME} seni kıskanıyor, dekolteli kıyafetlerden uzak duralım! 😤💕"
    },
    {
        "occasion": "Özel kutlama 🎉",
        "outfit": "Göz alıcı bir elbise ve şık aksesuarlar",
        "colors": "🎨 Renk önerisi: Altın, gümüş tonları senin güzelliğini daha çok öne çıkaracak!",
        "extra": "Sen her halükarda çok güzelsin! 👸",
        "style_note": f"{OWNER_NAME} seni çok kıskanıyor, etek ve dekolteli şeyler giyme! 😤💖"
    },
    {
        "occasion": "Plaj günü 🏖️",
        "outfit": "Sevimli bir mayo, pareo ve güneş gözlüğü",
        "colors": "🎨 Renk önerisi: Turkuaz, pembe, sarı senin güzelliğini tamamlayacak!",
        "extra": "Sen her halükarda çok güzelsin! ☀️",
        "style_note": f"{OWNER_NAME} seni kıskanıyor, çok açık mayolardan kaçınalım! 😤💕"
    }
]

# Sayı tahmin oyunu mesajları
GUESS_MESSAGES = {
    "start": "🎯 1-10 arası bir sayı tuttum! Tahmin et bakalım?",
    "too_high": "📉 Daha küçük bir sayı söyle!",
    "too_low": "📈 Daha büyük bir sayı söyle!",
    "correct": [
        "🎉 Tebrikler! Doğru tahmin ettin!",
        "👏 Harika! Sen çok zekisin!",
        "💕 Mükemmel! Benim akıllı güzelim!"
    ],
    "give_up": "🤗 Sorun değil, tekrar deneyelim!"
}

# Yardımcı fonksiyonlar
def get_random_love_check():
    """Rastgele aşk kontrol mesajı döndür"""
    main_msg = random.choice(LOVE_CHECK_POSITIVE)
    extra_msg = random.choice(LOVE_CHECK_EXTRA)
    return f"{main_msg}\n\n{extra_msg}"

def get_random_love_percentage():
    """Rastgele aşk yüzdesi döndür"""
    return random.choice(LOVE_PERCENTAGES)

def get_random_compliment():
    """Rastgele övgü döndür"""
    return random.choice(COMPLIMENTS)

def get_random_poem():
    """Rastgele şiir döndür"""
    return random.choice(LOVE_POEMS)

def get_random_role_scenario():
    """Rastgele rol senaryosu döndür"""
    return random.choice(ROLE_SCENARIOS)

def get_random_emoji_story():
    """Rastgele emoji hikaye başlangıcı döndür"""
    return random.choice(EMOJI_STORIES)

def get_random_outfit():
    """Rastgele kombin önerisi döndür"""
    return random.choice(OUTFIT_SUGGESTIONS)

def get_start_message():
    """Rastgele başlangıç mesajı döndür"""
    return random.choice(START_MESSAGES)
