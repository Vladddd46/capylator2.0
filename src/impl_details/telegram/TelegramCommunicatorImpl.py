from src.tech_config import bot

from telebot import types


class TelegramCommunicatorImpl:

    def __init__(self):
        pass

    def send_message(self, chat_id, text, menu=None):
        bot.send_message(chat_id, text, parse_mode="Markdown", reply_markup=menu)
