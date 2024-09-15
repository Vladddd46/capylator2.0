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

@bot.message_handler(commands=["language"])
def languageCmd(message):
    requests_handler.onLanguageCommand(message)

@bot.message_handler(commands=["indexes"])
def indexesCmd(message):
    requests_handler.onIndexesCommand(message)

@bot.message_handler(regexp=r"/setspend (\d+)")
def setspendCmd(message):
    requests_handler.onSetspendHandler(message)

# should be under @bot.message_handler(regexp=r"/setspend (\d+)")
@bot.message_handler(commands=["setspend"])
def setspendInvalidCmd(message):
    requests_handler.onSetspendHandler(message)

@bot.callback_query_handler(func=lambda call: True)
def inlineButtonCallback(call):
    requests_handler.onInlineButtonClick(call)


bot.polling()
