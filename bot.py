import telebot
from telebot import types
import random

TOKEN = '8766115810:AAH4_ziRGR9kldxMzXbNlFhsDWb-Z2w4HHE'
bot = telebot.TeleBot(TOKEN)

# Просто название агента + забавная фраза
AGENT_MESSAGES = {
    "Jett": "💨 *Jett*\n«Ветра зовут... а я есть хочу, может позже?»",
    "Phoenix": "🔥 *Phoenix*\n«Курица гриль? Нет, я просто воскрес!»",
    "Raze": "💥 *Raze*\n«Где бомба - там и я! А где я - там бабах!»",
    "Reyna": "👑 *Reyna*\n«Смотрите, королева пришла... ну и где мои подданные?»",
    "Yoru": "🌀 *Yoru*\n«Ты меня не видишь? А я тут... или нет?»",
    "Neon": "⚡ *Neon*\n«Быстрее света, медленнее микроволновки»",
    "Waylay": "🌓 *Waylay*\n«Свет мой, зеркальце, скажи... хотя нет, не надо»",
    "Iso": "🎯 *Iso*\n«Цель оправдывает средства... особенно если цель - чайник»",
    
    "Skye": "🌿 *Skye*\n«Мои звери лучше ваших скибиди-туалетов»",
    "KAY/O": "🤖 *KAY/O*\n«Ошибка 404: чувство юмора не найдено»",
    "Fade": "👁️ *Fade*\n«Твои кошмары - мои сериалы»",
    "Gekko": "🦎 *Gekko*\n«Мои питомцы кусаются. И какают. Везде.»",
    "Tejo": "⚙️ *Tejo*\n«Технологии будущего, мозги прошлого»",
    "Sova": "🦉 *Sova*\n«Я вижу тебя... и твои кривые ноги»",
    "Breach": "💢 *Breech*\n«Землетрясение? Нет, это я чихнул»",
    
    "Brimstone": "🔥🔥 *Brimstone*\n«Адский огонь? У меня просто изжога»",
    "Viper": "🐍 *Viper*\n«Токсичный? Я просто честная»",
    "Omen": "🌑 *Omen*\n«Тьма внутри меня... и скидка на свет»",
    "Astra": "✨ *Astra*\n«Звезды сошлись... на мне в игре»",
    "Harbor": "🌊 *Harbor*\n«Волна идет! И уносит моих тиммейтов»",
    "Clove": "🧄 *Clove*\n«Цветочек, но с перчинкой»",
    
    "Killjoy": "🔧 *Killjoy*\n«Моя турель лучше твоего КД»",
    "Cypher": "🕸️ *Cypher*\n«Шпионские игры? Я в прятки даже не умею»",
    "Chamber": "🥂 *Chamber*\n«Шампанское, пули и немного пафоса»",
    "Veto": "🚫 *Veto*\n«Не сегодня, дорогой»",
    "Deadlock": "🔒 *Deadlock*\n«Закрыто на переучет»",
    "Sage": "💚 *Sage*\n«Воскрешу, но чек потом пришлю»"
}

# Просто оружие жирным + смешная фраза
WEAPON_MESSAGES = {
    "Classic": "🔫 *Classic*\nС классики начинали, на классике и закончим... раунд",
    "Shorty": "🔫 *Shorty*\nБах - и в дамках! Главное - подойти поближе",
    "Frenzy": "🔫 *Frenzy*\nДержится прямо, стреляет криво",
    "Ghost": "🔫 *Ghost*\nПиф-паф, ой, а я не слышал",
    "Sheriff": "🔫 *Sheriff*\nКовбой Мальборо одобряет",
    "Bandit": "🔫 *Bandit*\nУкрал, выстрелил, убежал",
    
    "Stinger": "🔹 *Stinger*\nЖужжит как пчела, кусает как комар",
    "Spectre": "🔹 *Spectre*\nПризрачная угроза... пока патроны не кончатся",
    
    "Bucky": "💥 *Bucky*\nДальше трех метров не стреляет, но это уже проблемы врага",
    "Judge": "💥 *Judge*\nСудья пришел, присяжные в шоке",
    
    "Bulldog": "🎯 *Bulldog*\nГавкает громко, кусает больно",
    "Guardian": "🎯 *Guardian*\nТвой личный телохранитель (иногда мажет)",
    "Phantom": "🎯 *Phantom*\nПризрак, который не умеет прятаться",
    "Vandal": "🎯 *Vandal*\nВандал на минималках",
    
    "Marshal": "🔭 *Marshal*\nЦелишься долго, стреляешь мимо",
    "Operator": "🔭 *Operator*\nОдин выстрел - один труп (ну или промах)",
    "Outlaw": "🔭 *Outlaw*\nКовбой из Аватара",
    
    "Ares": "⚙️ *Ares*\nБах-бах-бах... перезарядка... бах",
    "Odin": "⚙️ *Odin*\nОдин в поле не воин, но с Одином можно",
    
    "Melee (Knife)": "🔪 *Melee*\nКогда надоело стрелять и хочется пошуметь"
}

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
    welcome_text = (
        "👋 *Привет, {}!*\n\n"
        "🎮 Я твой личный рандомайзер для VALORANT\n"
        "🔫 Тыкай кнопки - получай агентов и пушки\n\n"
        "👇 *Погнали!*"
    ).format(message.from_user.first_name)
    
    bot.send_message(
        message.chat.id,
        welcome_text,
        parse_mode="Markdown",
        reply_markup=create_keyboard()
    )

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "❓ *Че тут делать?*\n\n"
        "/start - запустить заново\n"
        "/agent - рандомный агент\n"
        "/weapon - рандомная пушка\n"
        "/both - и то и другое\n\n"
        "🖲️ *Или просто жми кнопки*"
    )
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
    agent = random.choice(list(AGENT_MESSAGES.keys()))
    msg = AGENT_MESSAGES[agent]
    
    bot.send_message(
        chat_id,
        f"🎮 *Случайный агент*\n\n{msg}",
        parse_mode="Markdown"
    )

def send_random_weapon(chat_id):
    weapon = random.choice(list(WEAPON_MESSAGES.keys()))
    msg = WEAPON_MESSAGES[weapon]
    
    bot.send_message(
        chat_id,
        f"🔫 *Случайное оружие*\n\n{msg}",
        parse_mode="Markdown"
    )

def send_both(chat_id):
    agent = random.choice(list(AGENT_MESSAGES.keys()))
    weapon = random.choice(list(WEAPON_MESSAGES.keys()))
    
    agent_msg = AGENT_MESSAGES[agent]
    weapon_msg = WEAPON_MESSAGES[weapon]
    
    bot.send_message(
        chat_id,
        f"🎲 *Случайная связка*\n\n{agent_msg}\n\n{weapon_msg}",
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
        stats = (
            f"📊 *Счетчик*\n\n"
            f"🎮 Агентов: {len(AGENT_MESSAGES)}\n"
            f"🔫 Пушек: {len(WEAPON_MESSAGES)}"
        )
        bot.send_message(message.chat.id, stats, parse_mode="Markdown")
    else:
        bot.send_message(
            message.chat.id,
            "❓ Чего? Жми кнопки или /help",
            reply_markup=create_keyboard()
        )

if __name__ == '__main__':
    print("🤖 Бот с юмором запущен...")
    bot.infinity_polling()