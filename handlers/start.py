"""
/start Komutu Handler
"""

from telegram import Update
from telegram.ext import ContextTypes
from core.messages import get_start_message, COMMANDS_LIST
from core.utils import get_time_greeting, format_love_message


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    /start komutu için handler fonksiyonu
    """
    user = update.effective_user
    user_name = user.first_name if user.first_name else "Güzelim"
    
    # Kişiselleştirilmiş karşılama
    greeting = get_time_greeting()
    welcome_msg = get_start_message()
    
    # Tam mesaj oluştur
    full_message = f"{greeting}\n\n{welcome_msg}\n\n{COMMANDS_LIST}"
    
    # Sevgi dolu formatla
    formatted_message = format_love_message(full_message, add_hearts=True, add_stars=True)
    
    await update.message.reply_text(
        formatted_message,
        parse_mode='Markdown'
    )
