import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

count = 0

@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    global count
    count = 0
    text = '''Привет!!! Я помогу тебе найти настоящего, преданного друга в нашем зоопарке!
    Для этого тебе надо ответить на несколько вопросов.
    Если готов пиши: /хочу_найти_друга'''
    bot.reply_to(message, text)

@bot.message_handler(commands=['хочу_найти_друга'])
def quiz(message: telebot.types.Message):
    questions = ['Напиши свой любимый цвет: /красный, /желтый, /зеленый',
                 'Напиши свое любимое время года: /весна, /лето, /осень',
                 'Напиши свое любимое лакомство: /мороженое, /сладкая_вата, /поп_корн'
                 ]
    for question in questions:
        bot.reply_to(message, question)

@bot.message_handler(commands=['красный', 'весна', 'мороженое'])
def ansv_kr(message: telebot.types.Message):
    global count
    count += 1
    respond_based_on_count(message)

@bot.message_handler(commands=['желтый', 'лето', 'сладкая_вата'])
def ansv_je(message: telebot.types.Message):
    global count
    count +=2
    respond_based_on_count(message)

@bot.message_handler(commands=['зеленый', 'осень', 'поп_корн'])
def ansv_gr(message: telebot.types.Message):
    global count
    count +=3
    respond_based_on_count(message)

def respond_based_on_count(message: telebot.types.Message):
    global count
    if count < 5:
        response_text = '''Тебе подходит АЛЬПАКA - это самый маленький из безгорбых верблюдов,
        внешне альпака немного напоминает овцу, но более стройная, легко сложенная,
        с короткой мордочкой, узкими заострёнными ушами, коротким мохнатым хвостом,
        длинными ногами и длинной шеей.
        Если хочешь с ним подружится переходи по ссылке https://moscowzoo.ru/about/guardianship
        Или звони по телефону 79629713875'''
    elif 5 <= count < 7:
        response_text = '''Тебе подходит АФРИКАНСКАЯ СОНЯ - это мышка у которой длина хвоста от 50 до 135 мм,
        весит соня 18-30 грамм. Шерсть мягкая, цвет от пепельно-серого до тёмно-серого.
        Брюшко белое или сероватое, часто есть вкрапления красно-коричневого цвета.
        На мордочке встречаются белые и чёрные пятнышки.
        Если хочешь с ней подружится переходи по ссылке https://moscowzoo.ru/about/guardianship
        Или звони по телефону 79629713875'''
    else:
        response_text = '''Тебе подходит БОЛИВИЙСКАЯ МИРИКИНА - самая крупная из ночных обезьян.
        Голова округлая с маленькими ушами. Общий тон шерсти на теле – коричнево-серый,
        на животе светлее, на шее и груди окраска рыжая.
        Если хочешь с ней подружится переходи по ссылке https://moscowzoo.ru/about/guardianship
        Или звони по телефону 79629713875'''

    bot.send_message(message.chat.id, response_text)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    print(f"Хороший выбор")

bot.polling(none_stop=True)


