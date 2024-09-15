from telebot import types
import json


class TelegramMenuManager:
    @staticmethod
    def __createInlineButtonWithTag(btnText, dataForCallback, tag):
        callbackData = str(tag) + "_" + str(dataForCallback)
        # BE CAREFULL: callback_data field has limit of length!
        button = types.InlineKeyboardButton(btnText, callback_data=callbackData)
        return button

    @staticmethod
    def getChooseLanguageMenu():
        inline_menu = types.InlineKeyboardMarkup(row_width=2)
        btn1 = TelegramMenuManager.__createInlineButtonWithTag(
            "English", "English", "chooseLanguage"
        )
        btn2 = TelegramMenuManager.__createInlineButtonWithTag(
            "Українська", "Ukrainian", "chooseLanguage"
        )
        btn3 = TelegramMenuManager.__createInlineButtonWithTag(
            "Русский", "Russian", "chooseLanguage"
        )
        inline_menu.add(btn1)
        inline_menu.add(btn2)
        inline_menu.add(btn3)
        return inline_menu
