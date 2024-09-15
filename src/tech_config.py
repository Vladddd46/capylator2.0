""" ===indexes scrapper config==="""

# html page, which cis scrapped and parsed in order to get 'cost of living' indexes
INDEXES_DATA_SRC_PAGE = "https://www.numbeo.com/cost-of-living/rankings.jsp"

# where parsed 'cost of living' indexes data is stored.
CACHED_INDEXES_DATA = "data/indexes_data.json"


""" ===telegram bot config=== """
import telebot
from telebot import types
from src.creds import TELEGRAM_API_TOKEN

bot = telebot.TeleBot(TELEGRAM_API_TOKEN)
bot.set_my_commands(
    [
        telebot.types.BotCommand("/settings", "settings"),
        telebot.types.BotCommand("/setloc", "set current location"),
        telebot.types.BotCommand("/setspend", "set spendings"),
        telebot.types.BotCommand("/calculate", "calculate spendings"),
        telebot.types.BotCommand("/start", "main menu"),
    ]
)
TELEGRAM_USER_DATA_PATH = "data/telegramUserDb.json"
