"""
Rol Değiştirme Oyunu Handler (/roldegistir)
"""

from telegram import Update
from telegram.ext import ContextTypes
from core.messages import get_random_role_scenario
from core.utils import typing_effect, get_random_heart_emoji
import asyncio


async def role_switch_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    /roldegistir komutu için handler fonksiyonu
    Romantik rol değiştirme senaryoları sunar
    """
    
    # Yazıyor efekti
    await update.message.chat.send_action("typing")
    await asyncio.sleep(1)
    
    # Rastgele senaryo al
    scenario = get_random_role_scenario()
    
    # Mesajı formatla
    role_message = f"""
🎭 **Rol Değiştirme Zamanı!**

{scenario['scenario']}

👤 **{scenario['your_role']}**
👤 **{scenario['my_role']}**

📖 **Senaryo:** {scenario['story']}

💕 Haydi bu rollerde biraz sohbet edelim! Ben karakterime uygun davranacağım, sen de kendin ol! {get_random_heart_emoji()}
"""
    
    await update.message.reply_text(
        role_message,
        parse_mode='Markdown'
    )
    
    # Karaktere uygun mesaj gönder
    await asyncio.sleep(2)
    
    # Senaryoya göre karakter mesajı
    if "kraliçe" in scenario['scenario'].lower():
        character_msg = "👑 Güzel kraliçem, bugün nasıl hizmet edebilirim?"
    elif "uzay" in scenario['scenario'].lower():
        character_msg = "🚀 Kaptan'ın emirleri nedir? Yıldızlara doğru yola çıkalım!"
    elif "ada" in scenario['scenario'].lower():
        character_msg = "🏝️ Bu ıssız adada birlikte harikalar yaratacağız!"
    else:
        character_msg = f"🎭 {scenario['my_role']} olarak, maceraya hazırım!"
    
    await update.message.reply_text(character_msg)
