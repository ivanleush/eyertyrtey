import telebot
import random
from config import TOKEN
import logging

bot = telebot.TeleBot(TOKEN)

questions = [
    {
        "photo": "https://static.wikia.nocookie.net/brainrotnew/images/5/5c/1743822682391-732.jpg/revision/latest/scale-to-width-down/1000?cb=20250405031425",  # Замените на URL своей фотографии
        "question": "А этого знаешь?",
        "options": ["Meterito Bearito", "Медведо Гулянто", "МедведоПенисинни", "Бомбини Гусини"],
        "correct_answer": "Meterito Bearito"
    },
    {
        "photo": "https://avatars.mds.yandex.net/i?id=cb3e804c2f94f10167165829b93abab4cc3554a9-7085252-images-thumbs&n=13",  # Замените на URL своей фотографии
        "question": "Этого точно не знаешь",
        "options": ["Ишак", "Ecco Cavallo Vira", "Ecco Cavallo Virtuoso", "Лох какой-то"],
        "correct_answer": "Ecco Cavallo Virtuoso"
    },
    {
        "photo": "https://avatars.mds.yandex.net/i?id=2a000001965dce205f6bca1177d9bf156d9f-1371038-fast-images&n=13",  # Замените на URL своей фотографии
        "question": "Кто изображен на фотографии?",
        "options": ["Бомбардиро Крокдило", "Тралалео Тралала", "Трипи Тропи", "Бобрито Бандито"],
        "correct_answer": "Тралалео Тралала"
    },
    {
        "photo": "https://static.life.ru/ip/unsafe/rs:fit:1200:/q:95/sh:0.5/czM6Ly9saWZlLXN0YXRpYy9wdWJsaWNhdGlvbnMvMjAyNS80LzIxLzI3Nzc3OTEzMTc3MC43Njc5LndlYnA=",  # Замените на URL своей фотографии
        "question": "Что это означает?",
        "options": ["Крокодилдо", "Крокодил", "Бомбардиро Крокодило", "Бомбини Гусини"],
        "correct_answer": "Бомбардиро Крокодило"
    },
    {
        "photo": "https://static.life.ru/ip/unsafe/rs:fit:1200:/q:95/sh:0.5/czM6Ly9saWZlLXN0YXRpYy9wdWJsaWNhdGlvbnMvMjAyNS80LzIxLzEwMjE2MDIwNzM2MzYuODE2LndlYnA=",  # Замените на URL своей фотографии
        "question": "Кто изображен на фотографии",
        "options": ["Кот", "Которыба", "Трипи Тропи", "Бомбини Гусини"],
        "correct_answer": "Трипи Тропи"
    },
    {
        "photo": "https://static.life.ru/ip/unsafe/rs:fit:1200:/q:95/sh:0.5/czM6Ly9saWZlLXN0YXRpYy9wdWJsaWNhdGlvbnMvMjAyNS80LzIxLzExOTQ1NDYyMDU2NDguMTY0LndlYnA=",  # Замените на URL своей фотографии
        "question": "Кто изображен на фотографии?",
        "options": ["Бобр курва", "Бобрито Бандито", "Трипи Тропи", "Бандит бобр"],
        "correct_answer": "Бобрито Бандито"
    },
    {
        "photo": "https://avatars.mds.yandex.net/i?id=2a000001965b45b0a5ac92c2638c1dc303c0-1714228-fast-images&n=13",  # Замените на URL своей фотографии
        "question": "А этого знаешь?",
        "options": ["Гусяра", "Крокодилда", "Бомбардиро Крокодило", "Бомбини Гусини"],
        "correct_answer": "Бомбини Гусини"
    },
    {
        "photo": "https://static.life.ru/ip/unsafe/rs:fit:1200:/q:95/sh:0.5/czM6Ly9saWZlLXN0YXRpYy9wdWJsaWNhdGlvbnMvMjAyNS80LzIxLzg4NTIyNzE5NzQ2Mi4yNjI3LndlYnA=",  # Замените на URL своей фотографии
        "question": "Этого точно не знаешь",
        "options": ["Пингвин", "Бомбини Гусини", "Пингвино Кондиционеро", "Лох какой-то"],
        "correct_answer": "Пингвино Кондиционеро"
    },
    {
        "photo": "https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_680810330e3c6354c47f6271_68081e53562f220a1139b5da/scale_1200",  # Замените на URL своей фотографии
        "question": "Кто изображен на фотографии?",
        "options": ["Лирили Ларила", "Тралалео Тралала", "Трипи Тропи", "Слон"],
        "correct_answer": "Лирили Ларила"
    },
    {
        "photo": "https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_680810330e3c6354c47f6271_68081ec79d7614002a3fafdc/scale_1200",  # Замените на URL своей фотографии
        "question": "Что это означает?",
        "options": ["Пенсил", "Тунг Тунг Тунг Саур", "Ля полицияяя", "Бомбини Гусини"],
        "correct_answer": "Тунг Тунг Тунг Саур"
    },
    {
        "photo": "https://avatars.mds.yandex.net/i?id=2a000001964dfd88e054aa77451f42a77bda-935487-fast-images&n=13",  # Замените на URL своей фотографии
        "question": "Кто изображен на фотографии",
        "options": ["Чашка", "Балерина Капучино", "Красоточка", "Крокодилда"],
        "correct_answer": "Балерина Капучино"
    },
    {
        "photo": "https://static.wikia.nocookie.net/brainrotnew/images/0/0d/Ta_ta_ta_ta_Sahur.png/revision/latest?cb=20250415133614",  # Замените на URL своей фотографии
        "question": "Кто изображен на фотографии?",
        "options": ["Та та та та лира", "Бобрито Бандито", "Ta ta ta ta Sahur", "Пенисилда"],
        "correct_answer": "Ta ta ta ta Sahur"
    },
    {
        "photo": "https://static.wikia.nocookie.net/meme/images/4/48/Chimpanzini_bannanini.jpg/revision/latest?cb=20250426012015",  # Замените на URL своей фотографии
        "question": "Знаешь кто это?",
        "options": ["Шимпанзини Бананини", "Бобрито Бандито", "Бонан", "БонананоМакака"],
        "correct_answer": "Шимпанзини Бананини"
    },
    {
        "photo": "https://static.wikia.nocookie.net/italianrot/images/1/1f/Screenshot_2025-03-25_at_21.38.51.png/revision/latest/scale-to-width-down/1000?cb=20250325203942",  # Замените на URL своей фотографии
        "question": "Знаешь кто это?",
        "options": ["Лулилоли", "Бурбалони Лулилоли", "Пенисини Кокосини", "Кокосини Капибари"],
        "correct_answer": "Бурбалони Лулилоли"
    },
    {
        "photo": "https://static.wikia.nocookie.net/brainrotnew/images/9/9d/BallerinoLololo.jpg/revision/latest?cb=20250416061058",  # Замените на URL своей фотографии
        "question": "Знаешь кто это?",
        "options": ["Красавчик", "Балерини капучини", "Балерино Лололо", "Пенисилда"],
        "correct_answer": "Балерино Лололо"
    },
    {
        "photo": "https://static.wikia.nocookie.net/brainrotnew/images/5/5e/File_00000000cda0624392b7bf21d2864411.png/revision/latest/scale-to-width-down/1000?cb=20250423195245",  # Замените на URL своей фотографии
        "question": "Знаешь кто это?",
        "options": ["Абаюдна🤙", "Горилили Бомбини", "Бомбардили Горилили", "Пенисилда"],
        "correct_answer": "Бомбардили Горилили"
    },
    {
        "photo": "https://static.wikia.nocookie.net/brainrotnew/images/3/36/Crocodildo_Penisini.png/revision/latest/scale-to-width-down/1000?cb=20250415115331",  # Замените на URL своей фотографии
        "question": "Знаешь кто это?",
        "options": ["Анасини Крокодили", "Бобрито Бандито", "Ta ta ta ta Sahur", "Крокодило Пенисини"],
        "correct_answer": "Крокодило Пенисини"
    },
    {
        "photo": "https://static.wikia.nocookie.net/brainrotnew/images/3/33/%D0%9A%D1%80%D0%BE%D0%BA%D0%BE%D0%B4%D0%B8%D0%BB%D0%BE_%D0%B0%D0%BD%D0%B0%D0%BD%D0%B0%D1%81%D0%B8%D0%BD%D0%B8.jpg/revision/latest?cb=20250419175355",  # Замените на URL своей фотографии
        "question": "Знаешь кто это?",
        "options": ["Крокодило Ананас", "Крокодило Дибило", "Крокодилдо Пенисини", "Пенисилда"],
        "correct_answer": "Крокодило Ананасини"
    },
    {
        "photo": "https://static.wikia.nocookie.net/brainrotnew/images/f/f1/Tric_Trac_Baraboom.png/revision/latest?cb=20250408104726",  # Замените на URL своей фотографии
        "question": "Знаешь кто это?",
        "options": ["Не знаю", "Трик трак барабум", "Трики Траки", "Пенисилда"],
        "correct_answer": "Трик трак барабум"
    },
    {
        "photo": "https://static.wikia.nocookie.net/brainrotnew/images/f/ff/Baby_Mama_T-rex.png/revision/latest/scale-to-width-down/1000?cb=20250408172331",  # Замените на URL своей фотографии
        "question": "Знаешь кто это?",
        "options": ["Та та та та лира", "Т-рексо пинки", "Дракон какой-то", "Бейби Мама т-рекс"],
        "correct_answer": "Бейби Мама т-рекс"
    },
]

asked_question_indices = set()  # Множество для хранения индексов заданных вопросов
current_question = None  # Переменная для хранения текущего вопроса

def get_new_question(chat_id):
    global current_question, asked_question_indices

    if len(asked_question_indices) == len(questions):
        # Все вопросы заданы, очищаем множество
        asked_question_indices.clear()
        logging.info("Все вопросы заданы, начинаем цикл заново.")

    available_question_indices = set(range(len(questions))) - asked_question_indices

    if not available_question_indices:
        bot.send_message(chat_id, "Вопросы закончились.  Начнем сначала!")
        return  # Вопросов больше нет

    try:
        question_index = random.choice(list(available_question_indices))
        current_question = questions[question_index]
        asked_question_indices.add(question_index)  # Добавляем индекс в множество заданных

        photo = current_question["photo"]
        question = current_question["question"]
        options = current_question["options"]
        correct_answer = current_question["correct_answer"]

        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        random.shuffle(options)  # перемешать
        buttons = [telebot.types.InlineKeyboardButton(text=option, callback_data=option) for option in options]
        markup.add(*buttons)
        bot.send_photo(chat_id, photo=photo, caption=question, reply_markup=markup)

    except Exception as e:
        logging.error(f"Ошибка при отправке вопроса пользователю: {e}")
        bot.send_message(chat_id, "Произошла ошибка при получении вопроса. Попробуйте позже.")
