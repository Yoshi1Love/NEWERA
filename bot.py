import telebot
from telebot import types
import random
import logging

TOKEN = '8766115810:AAH4_ziRGR9kldxMzXbNlFhsDWb-Z2w4HHE'
bot = telebot.TeleBot(TOKEN)

AGENTS = [
    "Jett", "Phoenix", "Raze", "Reyna", "Yoru", "Neon", "Waylay", "Iso", 
    "Skye", "KAY/O", "Fade", "Gekko", "Tejo", "Sova", "Breach", 
    "Brimstone", "Viper", "Omen", "Astra", "Harbor", "Clove", 
    "Killjoy", "Cypher", "Chamber", "Veto", "Deadlock", "Sage"  
]

WEAPONS = [
    "Classic", "Shorty", "Frenzy", "Ghost", "Sheriff", "Bandit",
    
    "Stinger", "Spectre",

    "Bucky", "Judge",
    
    "Bulldog", "Guardian", "Phantom", "Vandal",
    
    "Marshal", "Operator", "Outlaw",

    "Ares", "Odin",
    
    "Melee (Knife)"
]
def create_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_agent = types.KeyboardButton("🎮 Случайный агент")
    btn_weapon = types.KeyboardButton("🔫 Случайное оружие")
    btn_both = types.KeyboardButton("🎲 И то и другое")
    btn_stats = types.KeyboardButton("📊 Статистика")
    markup.add(btn_agent, btn_weapon, btn_both, btn_stats)
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message, 
        "👋 Привет! Я бот для игры VALORANT.\n"
        "Выбери действие:",
        reply_markup=create_keyboard()
    )

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
    🤖 *Команды бота:*
    /start - Запустить бота
    /help - Показать помощь
    /agent - Случайный агент
    /weapon - Случайное оружие
    /both - Случайная связка
    
    Или просто используй кнопки ниже!
    """
    bot.send_message(message.chat.id, help_text, parse_mode="Markdown")

@bot.message_handler(commands=['agent', 'weapon', 'both'])
def handle_commands(message):
    if message.text == '/agent':
        send_random_agent(message.chat.id)
    elif message.text == '/weapon':
        send_random_weapon(message.chat.id)
    elif message.text == '/both':
        send_both(message.chat.id)

def send_random_agent(chat_id):
    random_agent = random.choice(AGENTS)
    bot.send_message(
        chat_id,
        f"🎮 Случайный агент: *{random_agent}*\n\n"
        f"Используй его способности с умом!",
        parse_mode="Markdown"
    )

def send_random_weapon(chat_id):
    random_weapon = random.choice(WEAPONS)
    bot.send_message(
        chat_id,
        f"🔫 Случайное оружие: *{random_weapon}*\n\n"
        f"Стрельба в голову - путь к победе! Если у тебя конечно не нож😊",
        parse_mode="Markdown"
    )

def send_both(chat_id):
    random_agent = random.choice(AGENTS)
    random_weapon = random.choice(WEAPONS)
    bot.send_message(
        chat_id,
        f"🎲 Случайная связка:\n\n"
        f"🎮 Агент: *{random_agent}*\n"
        f"🔫 Оружие: *{random_weapon}*\n\n"
        f"Интересное сочетание! Попробуй!",
        parse_mode="Markdown"
    )

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "🎮 Случайный агент":
        send_random_agent(message.chat.id)
    elif message.text == "🔫 Случайное оружие":
        send_random_weapon(message.chat.id)
    elif message.text == "🎲 И то и другое":
        send_both(message.chat.id)
    elif message.text == "📊 Статистика":
        stats = f"Всего агентов: {len(AGENTS)}\nВсего оружия: {len(WEAPONS)}"
        bot.send_message(message.chat.id, f"📊 *Статистика:*\n{stats}", parse_mode="Markdown")
    else:
        bot.send_message(
            message.chat.id,
            "Используй кнопки или команды /help",
            reply_markup=create_keyboard()
        )

if __name__ == '__main__':
    print("🤖 Бот запущен...")
    bot.infinity_polling()
