from src.impl_details.TelegramCommunicatorImpl import TelegramCommunicatorImpl
from src.impl_details.TelegramTextProviderImpl import TelegramTextProviderImpl
from src.impl_details.TelegramUserDataDbImpl import TelegramUserDataDbImpl
from src.entities.Language import Language
from src.tech_config import bot, TELEGRAM_USER_DATA_PATH
from src.impl_details.TelegramMenuManager import TelegramMenuManager


class TelegramRequestsHandlerImpl:

    def __init__(self):
        self.telegram_communicator = TelegramCommunicatorImpl()
        self.telegram_text_provider = TelegramTextProviderImpl()
        self.telegram_user_database = TelegramUserDataDbImpl(TELEGRAM_USER_DATA_PATH)

    def __send_welcome_text(self, user_id):
        user_language = self.telegram_user_database.get_user_language(user_id)
        text = self.telegram_text_provider.getStartText(user_language)
        menu = None
        self.telegram_communicator.send_message(user_id, text, menu)

    def __choose_language(self, user_id):
        menu = TelegramMenuManager.getChooseLanguageMenu()
        self.telegram_communicator.send_message(user_id, "Choose the language:", menu)

    def onStartCommand(self, message):
        if self.telegram_user_database.is_user_exist(message.chat.id) == False:
            # ask user to choose the language
            self.__choose_language(message.chat.id)
        else:
            # send user start text
            self.__send_welcome_text(message.chat.id)

    def onInfoCommand(self, message):
        user_id = message.chat.id
        user_language = self.telegram_user_database.get_user_language(user_id)
        if user_language == None:
            self.__choose_language(user_id)
        else:
            text = self.telegram_text_provider.getInfoText(user_language)
            self.telegram_communicator.send_message(user_id, text)

    def onCalculateCommand(self, message):
        pass

    def onInlineButtonClick(self, call):
        user_id = call.message.chat.id
        callback_data = call.data
        tag, data = callback_data.split("_", 1)

        if tag == "chooseLanguage":
            user_exists = self.telegram_user_database.is_user_exist(user_id)
            self.telegram_user_database.chooseLanguage(
                user_id, data
            )  # creates a new user with specified language

            if user_exists == True:
                self.telegram_communicator.send_message(user_id, "✅")
            else:
                self.__send_welcome_text(user_id)
