from src.entities.Language import Language
from data.texts import (
    START_TEXT_ENG,
    START_TEXT_UKR,
    START_TEXT_RUS,
    INFO_TEXT_ENG,
    INFO_TEXT_UKR,
    INFO_TEXT_RUS,
    CALCULATION_MENU_TEXT_UKR,
    CALCULATION_MENU_TEXT_ENG,
    CALCULATION_MENU_TEXT_RUS,
    SETSPEND_SUCCESS_TEXT_UKR,
    SETSPEND_SUCCESS_TEXT_RUS,
    SETSPEND_SUCCESS_TEXT_ENG,
    NUMBER_TOO_BIG_ERROR_TEXT_ENG,
    NUMBER_TOO_BIG_ERROR_TEXT_UKR,
    NUMBER_TOO_BIG_ERROR_TEXT_RUS,
    SETSPEND_WRONG_ARGS_TEXT_ENG,
    SETSPEND_WRONG_ARGS_TEXT_RUS,
    SETSPEND_WRONG_ARGS_TEXT_UKR,
)


class TelegramTextProviderImpl:
    def __init__(self):
        pass

    def getStartText(self, language):
        if language == Language.ENG.value:
            return START_TEXT_ENG
        elif language == Language.UKR.value:
            return START_TEXT_UKR
        elif language == Language.RUS.value:
            return START_TEXT_RUS
        return START_TEXT_ENG

    def getInfoText(self, language):
        if language == Language.ENG.value:
            return INFO_TEXT_ENG
        elif language == Language.UKR.value:
            return INFO_TEXT_UKR
        elif language == Language.RUS.value:
            return INFO_TEXT_RUS
        return INFO_TEXT_ENG

    def getCalculationMenuText(self, language):
        if language == Language.ENG.value:
            return CALCULATION_MENU_TEXT_ENG
        elif language == Language.UKR.value:
            return CALCULATION_MENU_TEXT_UKR
        elif language == Language.RUS.value:
            return CALCULATION_MENU_TEXT_RUS
        return CALCULATION_MENU_TEXT_ENG

    def getSetspendSuccessText(self, language):
        if language == Language.ENG.value:
            return SETSPEND_SUCCESS_TEXT_ENG
        elif language == Language.UKR.value:
            return SETSPEND_SUCCESS_TEXT_UKR
        elif language == Language.RUS.value:
            return SETSPEND_SUCCESS_TEXT_RUS
        return SETSPEND_SUCCESS_TEXT_ENG

    def getNumberTooBigErrorText(self, language):
        if language == Language.ENG.value:
            return NUMBER_TOO_BIG_ERROR_TEXT_ENG
        elif language == Language.UKR.value:
            return NUMBER_TOO_BIG_ERROR_TEXT_UKR
        elif language == Language.RUS.value:
            return NUMBER_TOO_BIG_ERROR_TEXT_RUS
        return NUMBER_TOO_BIG_ERROR_TEXT_ENG

    def getSetspendWrongArgsText(self, language):
        if language == Language.ENG.value:
            return SETSPEND_WRONG_ARGS_TEXT_ENG
        elif language == Language.UKR.value:
            return SETSPEND_WRONG_ARGS_TEXT_UKR
        elif language == Language.RUS.value:
            return SETSPEND_WRONG_ARGS_TEXT_RUS
        return SETSPEND_WRONG_ARGS_TEXT_ENG
