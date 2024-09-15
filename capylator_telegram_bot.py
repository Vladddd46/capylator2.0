import re
from src.tech_config import bot
from src.interfaces.TelegramRequestsHandler import TelegramRequestsHandler

requests_handler = TelegramRequestsHandler()

@bot.message_handler(commands=["start"])
def startCmd(message):
    requests_handler.onStartCommand(message)

@bot.message_handler(commands=["info"])
def infoCmd(message):
    requests_handler.onInfoCommand(message)


@bot.message_handler(commands=["calculate"])
def calculateCmd(message):
    requests_handler.onCalculateCommand(message)

@bot.callback_query_handler(func=lambda call: True)
def inlineButtonCallback(call):
    requests_handler.onInlineButtonClick(call)

bot.polling()
