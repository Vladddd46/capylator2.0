from telebot import types
import json
from src.entities.Language import Language
from data.buttonsLocalization import CALCULATION_BUTTONS_UKR, CALCULATION_BUTTONS_RUS, CALCULATION_BUTTONS_ENG

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

    @staticmethod
    def getCalculationMenu(language):
        inline_menu = types.InlineKeyboardMarkup(row_width=2)

        if language == Language.UKR.value:
            button_names = CALCULATION_BUTTONS_UKR
        elif language == Language.RUS.value:
            button_names = CALCULATION_BUTTONS_RUS
        else:
            button_names = CALCULATION_BUTTONS_ENG

        button1 = TelegramMenuManager.__createInlineButtonWithTag(
            button_names["all"], "all", "predict"
        )
        button2 = TelegramMenuManager.__createInlineButtonWithTag(
            button_names["specified"], "specified", "predict"
        )
        button3 = TelegramMenuManager.__createInlineButtonWithTag(
            button_names["under"], "<", "predict"
        )
        button4 = TelegramMenuManager.__createInlineButtonWithTag(
            button_names["over"], ">", "predict"
        )
        inline_menu.add(button1)
        inline_menu.add(button2)
        inline_menu.add(button3)
        inline_menu.add(button4)
        return inline_menu