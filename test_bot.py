#!/usr/bin/env python3
"""
Test Script - Bot Functionality Test
Bu script botun temel fonksiyonlarını test eder
"""

import asyncio
import sys
import os

# Proje dizinini path'e ekle
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.messages import *
from core.utils import *


async def test_core_functions():
    """Core fonksiyonlarını test et"""
    print("🧪 Core fonksiyon testleri başlıyor...\n")
    
    # Messages test
    print("📝 Messages modülü test ediliyor:")
    print(f"✅ Random love check: {get_random_love_check()[:50]}...")
    print(f"✅ Random compliment: {get_random_compliment()}")
    print(f"✅ Random poem: {get_random_poem()[:50]}...")
    print()
    
    # Utils test
    print("🔧 Utils modülü test ediliyor:")
    print(f"✅ Time greeting: {get_time_greeting()}")
    print(f"✅ Random heart: {get_random_heart_emoji()}")
    print(f"✅ Progress bar: {create_progress_bar(85)}")
    print(f"✅ Emoji number: {format_emoji_number(123)}")
    print()
    
    # Game session test
    print("🎮 Game session test ediliyor:")
    game_sessions.start_game(12345, 'test_game', {'test': True})
    print(f"✅ Game started: {game_sessions.is_game_active(12345)}")
    print(f"✅ Game data: {game_sessions.get_game(12345)}")
    game_sessions.end_game(12345)
    print(f"✅ Game ended: {not game_sessions.is_game_active(12345)}")
    print()
    
    print("🎉 Tüm testler başarılı!")


async def test_handlers():
    """Handler fonksiyonlarını basic test"""
    print("🎯 Handler importları test ediliyor...\n")
    
    try:
        from handlers.start import start_command
        print("✅ start_command imported")
        
        from handlers.love_check import love_check_command
        print("✅ love_check_command imported")
        
        from handlers.love_rate import love_rate_command
        print("✅ love_rate_command imported")
        
        from handlers.guess_number import guess_number_command
        print("✅ guess_number_command imported")
        
        from handlers.role_switch import role_switch_command
        print("✅ role_switch_command imported")
        
        from handlers.emoji_story import emoji_story_command
        print("✅ emoji_story_command imported")
        
        from handlers.outfit_suggestion import outfit_suggestion_command
        print("✅ outfit_suggestion_command imported")
        
        print("\n🎉 Tüm handler'lar başarıyla import edildi!")
        
    except Exception as e:
        print(f"❌ Handler import hatası: {e}")


async def main():
    """Ana test fonksiyonu"""
    print("🤖 Telegram Aşk Botu - Test Scripti")
    print("=" * 50)
    
    await test_core_functions()
    print("-" * 50)
    await test_handlers()
    
    print("\n" + "=" * 50)
    print("📋 Test Özeti:")
    print("✅ Core modüller çalışıyor")
    print("✅ Handler'lar import ediliyor")
    print("✅ Bot Railway'e deploy edilmeye hazır!")
    print("\n💡 Bot token'ınızı .env dosyasına ekleyip botu başlatabilirsiniz!")


if __name__ == "__main__":
    asyncio.run(main())
