from src.impl_details.telegram.TelegramCommunicatorImpl import TelegramCommunicatorImpl
from src.impl_details.telegram.TelegramTextProviderImpl import TelegramTextProviderImpl
from src.impl_details.telegram.TelegramUserDataDbImpl import TelegramUserDataDbImpl
from src.entities.Language import Language
from src.tech_config import bot, TELEGRAM_USER_DATA_PATH
from src.impl_details.telegram.TelegramMenuManager import TelegramMenuManager
import re


class TelegramRequestsHandlerImpl:

    def __init__(self):
        self.telegram_communicator = TelegramCommunicatorImpl()
        self.telegram_text_provider = TelegramTextProviderImpl()
        self.telegram_user_database = TelegramUserDataDbImpl(TELEGRAM_USER_DATA_PATH)

    def __send_welcome_text(self, user_id):
        user_language = self.telegram_user_database.get_user_language(user_id)
        text = self.telegram_text_provider.getStartText(user_language)
        self.telegram_communicator.send_message(user_id, text)

    def __choose_language_dialog(self, user_id):
        menu = TelegramMenuManager.getChooseLanguageMenu()
        self.telegram_communicator.send_message(user_id, "Choose the language:", menu)

    def onSetspendHandler(self, message):
        match = re.match(r"/setspend (\d+)", message.text)
        user_id = message.chat.id
        user_language = self.telegram_user_database.get_user_language(user_id)
        if user_language == None:
            self.__choose_language_dialog(user_id)
            return
        text = ""

        if match:
            new_spendings = match.group(1)
            if len(new_spendings) > 20:
                text = self.telegram_text_provider.getNumberTooBigErrorText(
                    user_language
                )
            else:
                new_spendings = float(new_spendings)
                if new_spendings < 0:
                    new_spendings *= -1
                self.telegram_user_database.set_user_spendings(user_id, new_spendings)
                text = (
                    self.telegram_text_provider.getSetspendSuccessText(user_language)
                    + f" {new_spendings}"
                )
        else:
            text = self.telegram_text_provider.getSetspendWrongArgsText(user_language)
        self.telegram_communicator.send_message(user_id, text)

    def onLanguageCommand(self, message):
        self.__choose_language_dialog(message.chat.id)

    def onStartCommand(self, message):
        if self.telegram_user_database.is_user_exist(message.chat.id) == False:
            # ask user to choose the language
            self.__choose_language_dialog(message.chat.id)
        else:
            # send user start text
            self.__send_welcome_text(message.chat.id)

    def onInfoCommand(self, message):
        user_id = message.chat.id
        user_language = self.telegram_user_database.get_user_language(user_id)
        if user_language == None:
            self.__choose_language_dialog(user_id)
        else:
            text = self.telegram_text_provider.getInfoText(user_language)
            self.telegram_communicator.send_message(user_id, text)

    def onCalculateCommand(self, message):
        user_id = message.chat.id
        user_language = self.telegram_user_database.get_user_language(user_id)
        if user_language == None:
            self.__choose_language_dialog(user_id)
        else:
            menu = TelegramMenuManager.getCalculationMenu(user_language)
            text = self.telegram_text_provider.getCalculationMenuText(user_language)
            self.telegram_communicator.send_message(user_id, text, menu)

    def onIndexesCommand(self, message):
        user_id = message.chat.id
        user_language = self.telegram_user_database.get_user_language(user_id)
        if user_language == None:
            self.__choose_language_dialog(user_id)
        else:
            pass

    def __chooseLanguageInlineRequest(self, user_id, data):
        user_exists = self.telegram_user_database.is_user_exist(user_id)
        self.telegram_user_database.chooseLanguage(
            user_id, data
        )  # creates a new user with specified language

        if user_exists == True:
            # means, that user exists but made an intent to change language
            self.telegram_communicator.send_message(user_id, "✅")
        else:
            # new user creation - send welcome text
            self.__send_welcome_text(user_id)

    def __predict_spendings(self, user_id, data):
        if data == "all":
            print("for all")
        elif data == "specified":
            print("for specified")
        elif data == ">":
            print(">")
        elif data == "<":
            print("<")

    def onInlineButtonClick(self, call):
        user_id = call.message.chat.id
        callback_data = call.data
        tag, data = callback_data.split("_", 1)

        if tag == "chooseLanguage":
            self.__chooseLanguageInlineRequest(user_id, data)
        elif tag == "predict":
            self.__predict_spendings(user_id, data)
