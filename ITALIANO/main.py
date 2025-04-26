import telebot
from config import TOKEN, CHANNEL_ID_1, CHANNEL_LINK_1, CHANNEL_ID_2, CHANNEL_LINK_2
from handlers import menu_handlers, callback_handlers
from utils import check_subscription
import logging

# Инициализация логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Инициализация бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    logging.info(f"Пользователь {user_id} запустил бота")  # Логируем запуск

    if check_subscription.check_subscription(user_id):
        markup = menu_handlers.create_main_menu()
        bot.send_message(message.chat.id, "👋Добро пожаловать!\n\n🤙Пристегните ремни, ведь это игра на знание Итальянских животных!", reply_markup=markup)
    else:
        # Создаем inline-кнопки для подписки
        markup = telebot.types.InlineKeyboardMarkup()
        channel_link_1 = telebot.types.InlineKeyboardButton(text="Подписаться на канал 1", url=CHANNEL_LINK_1)
        channel_link_2 = telebot.types.InlineKeyboardButton(text="Подписаться на канал 2", url=CHANNEL_LINK_2)
        check_button = telebot.types.InlineKeyboardButton(text="Проверить подписку", callback_data="check_sub")
        markup.add(channel_link_1)
        markup.add(channel_link_2)
        markup.add(check_button)

        bot.send_message(message.chat.id, "Для использования бота необходимо подписаться на два канала:", reply_markup=markup)

# Обработчик callback-запроса для проверки подписки
@bot.callback_query_handler(func=lambda call: call.data == "check_sub")
def check_subscription_callback(call):
    user_id = call.from_user.id
    if check_subscription.check_subscription(user_id):
        markup = menu_handlers.create_main_menu()
        bot.send_message(call.message.chat.id, "Спасибо за подписку! Добро пожаловать в викторину!", reply_markup=markup)
    else:
        bot.send_message(call.message.chat.id, "Вы не подписались на все каналы. Пожалуйста, подпишитесь и попробуйте снова.")

# Регистрируем handlers
menu_handlers.register_handlers(bot)
callback_handlers.register_handlers(bot)
check_subscription.bot = bot

# Запуск бота
if __name__ == '__main__':
    logging.info("Bot starting...")
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        logging.error(f"Ошибка при запуске бота: {e}")