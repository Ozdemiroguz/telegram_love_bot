"""
Aşk Kontrol Komutu Handler (/seviyormu)
"""

from telegram import Update
from telegram.ext import ContextTypes
from core.messages import get_random_love_check, get_random_compliment
from core.utils import typing_effect, get_random_heart_emoji, format_love_message
import asyncio


async def love_check_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    /seviyormu komutu için handler fonksiyonu
    Oğuz'un Tuanna'yı ne kadar sevdiğini söyler
    """
    
    # Yazıyor efekti
    await update.message.chat.send_action("typing")
    await asyncio.sleep(1)
    
    # Ana aşk mesajı
    love_message = get_random_love_check()
    
    # Ekstra övgü
    compliment = get_random_compliment()
    
    # Tam mesaj
    full_message = f"{love_message}\n\n💕 **Ek olarak:** {compliment}"
    
    # Mesajı gönder
    await update.message.reply_text(
        full_message,
        parse_mode='Markdown'
    )
    
    # 2 saniye sonra ekstra mesaj
    await asyncio.sleep(2)
    await update.message.reply_text(
        f"{get_random_heart_emoji()} Bu cevap her zaman aynı çünkü sevgimiz değişmez! {get_random_heart_emoji()}"
    )
