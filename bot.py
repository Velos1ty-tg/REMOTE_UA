import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8765638136:AAGyVvTQFFTHoDQgJWk6qmuqrW_8m35Jf88"  # вставь сюда правильний токен
bot = telebot.TeleBot(TOKEN)

# --- /start ---
@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    
    # Кнопки с эмодзи
    btn1 = KeyboardButton("👷‍♂️ Як почати працювати?")
    btn2 = KeyboardButton("💰 Як нараховується оплата?")
    btn3 = KeyboardButton("🏦 Отримання коштів")
    btn4 = KeyboardButton("🔑 Як отримати доступ?")
    btn5 = KeyboardButton("📲 Звязок")
    
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    markup.add(btn5)
    
    text = (
        "Вас вітає компанія Remote UA 👋\n\n"
        "Ми - команда, яка допомагає людям отримувати стабільний онлайн-дохід через віддалену роботу 💻.\n"
        "Наша система побудована так, щоб ви могли швидко стартувати 🚀, працювати у зручному форматі та отримувати прозору оплату за виконані завдання 💼.\n\n"
        "Маємо 500+ партнерів 🤝 та більше 5000 успішно виконаних проєктів 🏆\n\n"
        "Далі ми коротко пояснимо, як почати роботу, як проходить оплата та що потрібно для отримання доступу 👇"
    )
    
    bot.send_message(message.chat.id, text, reply_markup=markup)

# --- "Як почати працювати?" ---
@bot.message_handler(func=lambda message: message.text == "👷‍♂️ Як почати працювати?")
def start_work(message):
    text = (
        "👋 Щоб почати роботу, будь ласка, надайте наступну інформацію менеджеру 📋:\n\n"
        "• 🕒 Бажаний графік роботи\n"
        "• 📅 Скільки днів на тиждень ви можете працювати\n"
        "• 🧑‍💼 ПІБ (для вашого облікового запису)\n"
        "• 📞 Номер телефону\n"
        "• 💬 (за бажанням) Telegram / інший контакт для зв’язку\n\n"
        "Після цього менеджер перевіряє дані ✅ та допомагає вам отримати доступ до роботи.\n\n"
        "Звязок з менеджером: @bratudovika 📲"
    )
    bot.send_message(message.chat.id, text)

# --- "Як нараховується оплата?" ---
@bot.message_handler(func=lambda message: message.text == "💰 Як нараховується оплата?")
def payment_info(message):
    text = (
        "💵 Оплата нараховується після перевірки виконаного завдання ✅.\n\n"
        "Інструкція проста 📑:\n"
        "ви виконуєте завдання ✍️ → надсилаєте готовий результат (офер / проєкт / лід) 📤 → менеджер або тімлід перевіряє 🔍 → підтверджує (ставить апрув) ✔️ → оплата зараховується на ваш внутрішній баланс 💰.\n\n"
        "Баланс контролюється вашим тімлідом 👨‍💼."
    )
    bot.send_message(message.chat.id, text)

# --- "Отримання коштів" ---
@bot.message_handler(func=lambda message: message.text == "🏦 Отримання коштів")
def get_funds(message):
    text = (
        "💰 Виплати:\n"
        "• мінімальна сума - від 3000 грн 🏦\n"
        "• зарахування - 1 раз на тиждень 📅\n"
        "• способи: банківська карта 💳 / ФОП 🧾 / номер телефону 📲 / криптовалюта ₿\n\n"
        "Виплати здійснюються без затримок після підтвердження балансу✅."
    )
    bot.send_message(message.chat.id, text)

# --- "Як отримати доступ?" ---
@bot.message_handler(func=lambda message: message.text == "🔑 Як отримати доступ?")
def access_info(message):
    text = (
        "🔑 Для отримання доступу Standard необхідно:\n"
        "1️⃣ Написати нашому менеджеру 📲\n"
        "2️⃣ Надати інформацію 📝:\n"
        "• 🧑‍💼 ПІБ\n"
        "• 📞 номер телефону\n"
        "• 🕒 бажаний графік роботи\n"
        "• 📅 кількість днів на тиждень\n\n"
        "Після перевірки даних ✅ менеджер відкриває вам доступ до системи Standard та ви можете починати роботу 🚀.\n\n"
        "Звязок з менеджером: @bratudovika 📲"
    )
    bot.send_message(message.chat.id, text)

# --- "Звязок" ---
@bot.message_handler(func=lambda message: message.text == "📲 Звязок")
def contact_info(message):
    text = (
        "📲 Зв'язатися з менеджером можна за посиланням:\n\n"
        "@bratudovika 📲"
    )
    bot.send_message(message.chat.id, text)

# --- Остальные кнопки ---
@bot.message_handler(func=lambda message: True)
def other_buttons(message):
    bot.send_message(message.chat.id, f"Ви натиснули: {message.text}. Ця кнопка поки не налаштована.")

# --- Запуск ---
print("Бот запущений...")
bot.infinity_polling()
