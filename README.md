# 💕 Telegram Love Bot

A professional, feature-rich Telegram bot designed to enhance romantic communication between couples. This fully customizable bot includes interactive games, daily affirmations, personalized messages, and romantic features that can be easily tailored for any relationship.

## ✨ Quick Customization

This bot is **completely customizable**! Simply change the names in `config/settings.py` to personalize it for any couple:

```python
OWNER_NAME = "Your_Name"         # Example: "Alex", "John", "Mike"
BELOVED_NAME = "Partner_Name"    # Example: "Sarah", "Emma", "Lisa"
```

After this simple configuration, all messages will automatically use your personalized names throughout the entire bot experience!

## 🌟 Core Features

### 💬 Interactive Commands
- `/start` - Initialize the bot and display command menu
- `/seviyormu` - "Does he/she love me?" - Get instant romantic affirmations
- `/nekadarseviyor` - Love percentage calculator (always 100%! + bonus poetry)
- `/sayitahmin` - Interactive number guessing game (1-10 range, 3 attempts)
- `/roldegistir` - Romantic role-playing scenarios and situations
- `/hikaye` - Collaborative emoji story completion game
- `/kombin` - Daily outfit suggestions with playful jealousy warnings 😤💕

### 🎮 Advanced Features
- **Smart Session Management**: Persistent game states and user tracking
- **Dynamic Content Library**: Hundreds of unique messages, poems, and responses
- **Personalized Experience**: All content adapts to your custom names
- **Interactive UI**: Typing indicators, progress bars, and delayed responses
- **Rich Emoji Integration**: Carefully curated romantic emojis
- **Zero Configuration**: Works out-of-the-box after name customization

## 🏗️ Technical Architecture

### Project Structure
```
telegram-love-bot/
├── bot.py                    # Main application entry point
├── config/
│   └── settings.py          # Configuration & name customization
├── handlers/                # Command handlers (modular design)
│   ├── start.py            # /start command
│   ├── love_check.py       # /seviyormu command
│   ├── love_rate.py        # /nekadarseviyor command
│   ├── guess_number.py     # /sayitahmin game logic
│   ├── role_switch.py      # /roldegistir scenarios
│   ├── emoji_story.py      # /hikaye story game
│   └── outfit_suggestion.py # /kombin suggestions
├── core/
│   ├── messages.py         # Content library (poems, messages, responses)
│   └── utils.py           # Utility functions and helpers
├── .env                    # Environment variables (bot token)
├── requirements.txt        # Python dependencies
├── Procfile               # Railway/Heroku deployment config
└── README.md              # This documentation
```

### Technology Stack
- **Python 3.9+**: Core programming language
- **python-telegram-bot 20.7**: Modern async Telegram bot framework
- **python-dotenv**: Environment variable management
- **asyncio**: Asynchronous programming for smooth UX

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/telegram-love-bot.git
cd telegram-love-bot
```

### 2. Customize Names (IMPORTANT!)
Edit `config/settings.py` and replace the default names:
```python
OWNER_NAME = "Your_Name"         # Replace with your name
BELOVED_NAME = "Partner_Name"    # Replace with your partner's name
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Bot Token
Create a `.env` file with your Telegram bot token:
```env
BOT_TOKEN=your_bot_token_from_botfather
DEBUG=False
```

### 5. Run Locally
```bash
python bot.py
```

## 🌐 Cloud Deployment

### Option 1: Railway Deployment (Recommended)

1. **Prepare Repository**
```bash
git add .
git commit -m "Initial commit: Telegram Love Bot"
git push origin main
```

2. **Deploy on Railway**
   - Visit [Railway.app](https://railway.app) and create account
   - Click "New Project" → "Deploy from GitHub"
   - Select your repository
   - Railway auto-detects `Procfile` and deploys

3. **Set Environment Variables**
   In Railway dashboard, add:
   ```
   BOT_TOKEN=your_actual_bot_token
   DEBUG=false
   ```

### Option 2: Heroku Deployment
```bash
heroku create your-love-bot-name
heroku config:set BOT_TOKEN=your_bot_token
git push heroku main
```

## 🎯 Development Guide

### Adding New Commands

1. **Create Handler**: Add new file in `handlers/` directory
2. **Add Messages**: Include message content in `core/messages.py`
3. **Register Handler**: Import and register in `bot.py`

### Example Handler Template
```python
from telegram import Update
from telegram.ext import ContextTypes
from core.messages import YOUR_MESSAGES
from core.utils import send_typing_message

async def your_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Your command description"""
    await send_typing_message(update, YOUR_MESSAGES["response"])
```

### Code Style Guidelines
- Use async/await for all handlers
- Store all messages in `core/messages.py`
- Add proper error handling
- Include type hints
- Follow Python PEP 8 standards
- Add docstrings for functions

## 💡 Customization & Extensions

### Message Customization
All bot responses are stored in `core/messages.py`. You can:
- Add new romantic messages
- Customize existing responses
- Include your inside jokes
- Add multiple language support

### Feature Extensions
Consider adding:
- **Daily Scheduler**: Automatic good morning/night messages
- **Database Integration**: Store preferences and chat history
- **Media Support**: Photos, voice messages, stickers
- **Special Dates**: Anniversary reminders and celebrations
- **Advanced Games**: More interactive couple activities

### Suggested File Structure for Extensions
```
extensions/
├── scheduler/
│   ├── daily_messages.py    # Automated messages
│   └── special_dates.py     # Anniversary tracking
├── database/
│   ├── user_data.py         # User preferences
│   └── chat_history.py      # Conversation logs
└── media/
    ├── photo_handler.py     # Image processing
    └── voice_handler.py     # Audio messages
```

## 👥 Developer Notes

This bot is designed as a template for creating personalized and interactive experiences. The architecture prioritizes modularity, readability, and ease of maintenance, making it straightforward to extend with new features.

### Coding Principles
- **Modularity**: Each feature is encapsulated in its own module.
- **Readability**: Code is written to be self-documenting where possible.
- **Maintainability**: The structure is designed for easy updates and debugging.
- **Scalability**: New features can be integrated with minimal friction.

---

**💕 Crafted with care to inspire connection. 💕**
