"""
Emoji Hikaye Komutu Handler (/hikaye)
"""

from telegram import Update
from telegram.ext import ContextTypes
from core.messages import get_random_emoji_story
from core.utils import typing_effect, get_random_star_emoji, get_seasonal_emoji
import asyncio


async def emoji_story_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    /hikaye komutu için handler fonksiyonu
    Emoji hikaye başlangıcı verir, kullanıcının tamamlamasını ister
    """
    
    # Yazıyor efekti
    await update.message.chat.send_action("typing")
    await asyncio.sleep(1)
    
    # Rastgele hikaye başlangıcı al
    story_start = get_random_emoji_story()
    seasonal_emoji = get_seasonal_emoji()
    
    # Ana mesaj
    story_message = f"""
📚 **Emoji Hikaye Zamanı!** {get_random_star_emoji()}

{story_start}

✨ **Şimdi sıra sende!** Hikayeyi nasıl devam ettirmek istiyorsun?

💡 **İpucu:** Emojiler kullanarak daha eğlenceli olur! {seasonal_emoji}

📝 Hikayeni yazabilirsin, ben de devam ettireceğim!
"""
    
    await update.message.reply_text(
        story_message,
        parse_mode='Markdown'
    )
    
    # Teşvik edici mesaj
    await asyncio.sleep(3)
    await update.message.reply_text(
        f"💭 Hayal gücünü konuştur! Sen en yaratıcı hikayeler yazarsın! {get_random_star_emoji()}"
    )
