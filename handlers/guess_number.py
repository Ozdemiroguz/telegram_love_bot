"""
Sayı Tahmin Oyunu Handler (/sayitahmin)
"""

from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters
from core.messages import GUESS_MESSAGES
from core.utils import game_sessions, is_valid_number, get_random_encouragement, format_emoji_number
import random
import asyncio


async def guess_number_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    /sayitahmin komutu için handler fonksiyonu
    Sayı tahmin oyunu başlatır
    """
    user_id = update.effective_user.id
    
    # Eğer zaten aktif oyun varsa
    if game_sessions.is_game_active(user_id, 'guess_number'):
        await update.message.reply_text(
            "🎮 Zaten bir sayı tahmin oyunu oynuyorsun! Devam et bakalım! 🎯"
        )
        return
    
    # Yeni oyun başlat
    secret_number = random.randint(1, 10)
    game_sessions.start_game(user_id, 'guess_number', {
        'secret_number': secret_number,
        'attempts': 0,
        'max_attempts': 3
    })
    
    await update.message.reply_text(
        f"🎯 {GUESS_MESSAGES['start']}\n\n"
        f"💡 3 hakkın var!\n"
        f"📝 Sadece sayı yazman yeterli (1-10 arası)"
    )


async def handle_guess(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Sayı tahminlerini işle
    """
    user_id = update.effective_user.id
    message_text = update.message.text
    
    # Aktif oyun kontrol et
    game = game_sessions.get_game(user_id)
    if not game or game['type'] != 'guess_number':
        return  # Oyun yok, mesajı işleme
    
    # Geçerli sayı kontrol et
    is_valid, guess = is_valid_number(message_text, 1, 10)
    if not is_valid:
        await update.message.reply_text(
            "🤔 Lütfen 1-10 arası bir sayı gir!\n"
            "Örnek: 5"
        )
        return
    
    # Oyun verilerini al
    game_data = game['data']
    secret_number = game_data['secret_number']
    attempts = game_data['attempts'] + 1
    max_attempts = game_data['max_attempts']
    
    # Tahmini kontrol et
    if guess == secret_number:
        # Doğru tahmin!
        game_sessions.end_game(user_id)
        correct_msg = random.choice(GUESS_MESSAGES['correct'])
        await update.message.reply_text(
            f"{correct_msg}\n\n"
            f"🎯 Doğru sayı: {format_emoji_number(secret_number)}\n"
            f"🎪 {attempts}. denemede bildin!\n\n"
            f"🔄 Tekrar oynamak için /sayitahmin yazabilirsin!"
        )
        return
    
    # Yanlış tahmin
    game_data['attempts'] = attempts
    
    if attempts >= max_attempts:
        # Hak bitti
        game_sessions.end_game(user_id)
        await update.message.reply_text(
            f"😅 {GUESS_MESSAGES['give_up']}\n\n"
            f"🎯 Doğru sayı: {format_emoji_number(secret_number)} idi!\n"
            f"🔄 Tekrar denemek için /sayitahmin yazabilirsin!\n\n"
            f"💕 {get_random_encouragement()}"
        )
        return
    
    # İpucu ver
    if guess > secret_number:
        hint_msg = GUESS_MESSAGES['too_high']
    else:
        hint_msg = GUESS_MESSAGES['too_low']
    
    remaining_attempts = max_attempts - attempts
    await update.message.reply_text(
        f"{hint_msg}\n"
        f"🎯 Kalan hakkın: {remaining_attempts}\n"
        f"💪 {get_random_encouragement()}"
    )


# Bu handler'ı bot.py'de ayrı olarak eklemen gerekecek
guess_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_guess)
