"""
Kombin Önerisi Handler (/kombin)
"""

from telegram import Update
from telegram.ext import ContextTypes
from core.messages import get_random_outfit
from core.utils import typing_effect, get_random_heart_emoji, get_time_greeting
from config.settings import OWNER_NAME
import asyncio
import random


async def outfit_suggestion_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    /kombin komutu için handler fonksiyonu
    Günün durumuna uygun kombin önerisi verir
    """
    
    # Yazıyor efekti
    await update.message.chat.send_action("typing")
    await asyncio.sleep(1.5)
    
    # Rastgele kombin al
    outfit = get_random_outfit()
    
    # Kombin mesajını formatla
    outfit_message = f"""
👗 **Bugün İçin Kombin Önerisi!**

🎯 **Durum:** {outfit['occasion']}

👚 **Kıyafet:** {outfit['outfit']}

{outfit['colors']}

✨ **Tavsiye:** {outfit['extra']}

💕 **Stil Notu:** {outfit['style_note']}

{get_random_heart_emoji()} **Sonuç:** Sen her durumda mükemmelsin! {get_random_heart_emoji()}
"""
    
    await update.message.reply_text(
        outfit_message,
        parse_mode='Markdown'
    )
    
    # Ekstra motivasyon mesajı
    await asyncio.sleep(2)
    
    motivation_messages = [
        f"💃 {OWNER_NAME} seni kıskanıyor, dekolteli şeyler giyme!",
        f"👸 {OWNER_NAME} çok kıskanç, o yüzden kapalı giy!",
        f"✨ {OWNER_NAME} seni çok seviyor ama kıskanıyor da!",
        f"🌟 {OWNER_NAME}'un kıskançlığı seni korusun!",
        f"💕 {OWNER_NAME} kıskanıyor, dekolteli kıyafetlerden uzak dur!"
    ]
    
    motivation = random.choice(motivation_messages)
    await update.message.reply_text(motivation)
    
    # Günün selamlamasını ekle
    await asyncio.sleep(1)
    greeting = get_time_greeting()
    await update.message.reply_text(f"{greeting} Bugün de mükemmel görüneceksin! 💖")
