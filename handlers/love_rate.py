"""
Aşk Yüzdesi Komutu Handler (/nekadarseviyor)
"""

from telegram import Update
from telegram.ext import ContextTypes
from core.messages import get_random_love_percentage, get_random_poem
from core.utils import create_progress_bar, typing_effect, get_random_heart_emoji
import asyncio
import random


async def love_rate_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    /nekadarseviyor komutu için handler fonksiyonu
    Oğuz'un Tuanna'yı ne kadar sevdiğini yüzde olarak gösterir
    """
    
    # Yazıyor efekti
    await update.message.chat.send_action("typing")
    await asyncio.sleep(1.5)
    
    # Rastgele %100 sevgi mesajı al (hep %100!)
    percentage_data = get_random_love_percentage()
    percentage_value = percentage_data[0]  # Her zaman 100
    percentage_message = percentage_data[1]
    
    # Progress bar oluştur (%100 için)
    progress_bar = create_progress_bar(100)
    
    # Ana mesaj
    main_message = f"""
🔍 **Aşk Ölçer Çalışıyor...**

{progress_bar}

{percentage_message}

{get_random_heart_emoji()} **Sonuç:** Sonsuz sevgi! {get_random_heart_emoji()}
"""
    
    await update.message.reply_text(
        main_message,
        parse_mode='Markdown'
    )
    
    # Bonus şiir gönder
    await asyncio.sleep(2)
    await update.message.chat.send_action("typing")
    await asyncio.sleep(1)
    
    poem = get_random_poem()
    await update.message.reply_text(
        f"📝 **Bonus Şiir:**\n\n{poem}"
    )
