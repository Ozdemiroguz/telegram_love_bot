"""
Yardımcı Fonksiyonlar ve Ortak Araçlar
"""

import random
import asyncio
from datetime import datetime


def format_emoji_number(number):
    """Sayıyı emoji formatında döndür"""
    emoji_map = {
        '0': '0️⃣', '1': '1️⃣', '2': '2️⃣', '3': '3️⃣', '4': '4️⃣',
        '5': '5️⃣', '6': '6️⃣', '7': '7️⃣', '8': '8️⃣', '9': '9️⃣'
    }
    return ''.join(emoji_map.get(digit, digit) for digit in str(number))


def get_random_heart_emoji():
    """Rastgele kalp emojisi döndür"""
    hearts = ["💕", "❤️", "💖", "💝", "💘", "💗", "💓", "💞", "💟", "♥️", "🧡", "💛", "💚", "💙", "💜", "🤍", "🖤", "🤎"]
    return random.choice(hearts)


def get_random_star_emoji():
    """Rastgele yıldız emojisi döndür"""
    stars = ["⭐", "🌟", "✨", "💫", "⭐", "🌠"]
    return random.choice(stars)


def get_time_greeting():
    """Saate göre selamlama döndür"""
    hour = datetime.now().hour
    
    if 5 <= hour < 12:
        return "🌅 Günaydın güzelim!"
    elif 12 <= hour < 17:
        return "☀️ İyi öğlenler tatlım!"
    elif 17 <= hour < 21:
        return "🌆 İyi akşamlar canım!"
    else:
        return "🌙 İyi geceler aşkım!"


def create_progress_bar(percentage, length=10):
    """Yüzde değeri için progress bar oluştur"""
    filled_length = int(length * percentage // 100)
    bar = '█' * filled_length + '░' * (length - filled_length)
    return f"`{bar}` {percentage}%"


async def typing_effect(update, text, delay=0.5):
    """Yazıyor efekti simülasyonu"""
    try:
        # Telegram'da "typing" göstergesi
        await update.message.chat.send_action("typing")
        await asyncio.sleep(delay)
        await update.message.reply_text(text, parse_mode='Markdown')
    except:
        # Hata durumunda normal mesaj gönder
        await update.message.reply_text(text, parse_mode='Markdown')


def is_valid_number(text, min_val=1, max_val=10):
    """Geçerli sayı kontrolü"""
    try:
        num = int(text)
        return min_val <= num <= max_val, num
    except ValueError:
        return False, None


def get_random_encouragement():
    """Rastgele cesaret verici mesaj"""
    encouragements = [
        "Sen harikasın! 🌟",
        "Mükemmel gidiyorsun! 💪",
        "Devam et güzelim! 💕",
        "Sen başarabilirsin! 🎯",
        "Harika bir iş çıkarıyorsun! 👏"
    ]
    return random.choice(encouragements)


def format_love_message(base_message, add_hearts=True, add_stars=False):
    """Sevgi mesajını formatla"""
    formatted = base_message
    
    if add_hearts:
        formatted = f"{get_random_heart_emoji()} {formatted} {get_random_heart_emoji()}"
    
    if add_stars:
        formatted = f"{get_random_star_emoji()} {formatted} {get_random_star_emoji()}"
    
    return formatted


def get_seasonal_emoji():
    """Mevsime göre emoji döndür"""
    month = datetime.now().month
    
    if month in [12, 1, 2]:  # Kış
        return "❄️"
    elif month in [3, 4, 5]:  # İlkbahar
        return "🌸"
    elif month in [6, 7, 8]:  # Yaz
        return "☀️"
    else:  # Sonbahar
        return "🍂"


class GameSession:
    """Oyun oturumu yönetimi için basit sınıf"""
    def __init__(self):
        self.active_games = {}
    
    def start_game(self, user_id, game_type, data):
        """Oyun başlat"""
        self.active_games[user_id] = {
            'type': game_type,
            'data': data,
            'started_at': datetime.now()
        }
    
    def get_game(self, user_id):
        """Oyun bilgisini al"""
        return self.active_games.get(user_id)
    
    def end_game(self, user_id):
        """Oyunu sonlandır"""
        if user_id in self.active_games:
            del self.active_games[user_id]
    
    def is_game_active(self, user_id, game_type=None):
        """Oyun aktif mi kontrol et"""
        game = self.get_game(user_id)
        if not game:
            return False
        if game_type:
            return game['type'] == game_type
        return True


# Global oyun oturum yöneticisi
game_sessions = GameSession()
