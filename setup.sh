#!/bin/bash

# Telegram Aşk Botu - Setup Script
# Bu script botu Railway'e deploy etmek için hazırlar

echo "🤖 Telegram Aşk Botu - Setup Script"
echo "===================================="

# 1. Git repository kontrolü
if [ ! -d ".git" ]; then
    echo "📁 Git repository oluşturuluyor..."
    git init
    git add .
    git commit -m "Initial commit: Love bot for Tuanna ❤️"
    echo "✅ Git repository oluşturuldu!"
else
    echo "✅ Git repository mevcut"
fi

# 2. .env dosyası kontrolü
if [ ! -f ".env" ] || ! grep -q "BOT_TOKEN=" .env || grep -q "your_bot_token_here" .env; then
    echo ""
    echo "⚠️  BOT_TOKEN ayarlanmamış!"
    echo ""
    echo "🔧 Lütfen şu adımları takip edin:"
    echo "1. Telegram'da @BotFather'a git"
    echo "2. /newbot komutuyla yeni bot oluştur"
    echo "3. Bot token'ını kopyala"
    echo "4. .env dosyasında 'your_bot_token_here' yerine token'ını yapıştır"
    echo ""
    echo "Örnek .env içeriği:"
    echo "BOT_TOKEN=1234567890:ABCdefGHijklMNOpqrSTUvwxyz"
    echo "DEBUG=False"
    echo ""
else
    echo "✅ BOT_TOKEN ayarlanmış"
fi

# 3. Virtual environment kontrolü
if [ ! -d "venv" ]; then
    echo "🐍 Virtual environment oluşturuluyor..."
    python3 -m venv venv
    echo "✅ Virtual environment oluşturuldu!"
else
    echo "✅ Virtual environment mevcut"
fi

# 4. Dependencies kurulumu
echo "📦 Dependencies kuruluyor..."
source venv/bin/activate
pip install -r requirements.txt > /dev/null 2>&1
echo "✅ Dependencies kuruldu!"

# 5. Test
echo "🧪 Bot test ediliyor..."
if python -c "from core.messages import get_random_love_check; print('✅ Bot çalışıyor!')" > /dev/null 2>&1; then
    echo "✅ Bot testleri başarılı!"
else
    echo "❌ Bot testleri başarısız!"
    exit 1
fi

echo ""
echo "🚀 RAILWAY DEPLOYMENT ADIMLARı:"
echo "================================"
echo "1. GitHub'a yükle (eğer henüz yapmadıysan):"
echo "   git remote add origin YOUR_GITHUB_REPO"
echo "   git push -u origin main"
echo ""
echo "2. Railway'e git: https://railway.app"
echo "3. 'New Project → Deploy from GitHub' seç"
echo "4. Bu repository'yi seç"
echo "5. Environment Variables'a şunları ekle:"
echo "   BOT_TOKEN=your_actual_token"
echo "   DEBUG=false"
echo ""
echo "6. Deploy'u başlat!"
echo ""
echo "💕 Bot hazır! Tuanna'ya aşkla kodlandı! 💕"
