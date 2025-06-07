"""
Telegram Bot Ayarları ve Konfigürasyon
"""

import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

# Bot token'ı
BOT_TOKEN = os.getenv('BOT_TOKEN')

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN çevre değişkeni bulunamadı! .env dosyasını kontrol edin.")

# Diğer ayarlar
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
OWNER_NAME = "Oğuz"
BELOVED_NAME = "Tuanna"
