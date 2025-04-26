import telebot
from config import TOKEN, CHANNEL_ID_1, CHANNEL_ID_2
import logging

bot = telebot.TeleBot(TOKEN)

def check_subscription(user_id):
    try:
        member1 = bot.get_chat_member(CHANNEL_ID_1, user_id)
        member2 = bot.get_chat_member(CHANNEL_ID_2, user_id)

        # Проверяем статус подписки для обоих каналов
        is_subscribed = (
            member1.status in ["member", "administrator", "creator"] and
            member2.status in ["member", "administrator", "creator"]
        )
        return is_subscribed
    except telebot.apihelper.ApiTelegramException as e:
        logging.error(f"Ошибка при проверке подписки пользователя {user_id}: {e}")
        return False
def register_handlers(bot_instance):
    global bot
    bot = bot_instance