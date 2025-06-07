#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Telegram Aşk Botu - Ana Dosya
Oğuz tarafından Tuanna için özel olarak geliştirilmiştir.
"""

import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config.settings import BOT_TOKEN

# Handlers
from handlers.start import start_command
from handlers.love_check import love_check_command
from handlers.love_rate import love_rate_command
from handlers.guess_number import guess_number_command, guess_handler
from handlers.role_switch import role_switch_command
from handlers.emoji_story import emoji_story_command
from handlers.outfit_suggestion import outfit_suggestion_command

# Logging ayarları
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def main():
    """Ana bot fonksiyonu"""
    # Application oluştur
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Komut handler'larını ekle
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("seviyormu", love_check_command))
    application.add_handler(CommandHandler("nekadarseviyor", love_rate_command))
    application.add_handler(CommandHandler("sayitahmin", guess_number_command))
    application.add_handler(CommandHandler("roldegistir", role_switch_command))
    application.add_handler(CommandHandler("hikaye", emoji_story_command))
    application.add_handler(CommandHandler("kombin", outfit_suggestion_command))
    
    # Sayı tahmin oyunu için mesaj handler'ı
    application.add_handler(guess_handler)
    
    # Bot başlatılıyor mesajı
    logger.info("🤖 Aşk Botu başlatılıyor...")
    
    # Botu çalıştır
    application.run_polling(allowed_updates=["message"])


if __name__ == '__main__':
    main()
