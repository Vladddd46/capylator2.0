from src.entities.Language import Language
from data.texts import (
    START_TEXT_ENG,
    START_TEXT_UKR,
    START_TEXT_RUS,
    INFO_TEXT_ENG,
    INFO_TEXT_UKR,
    INFO_TEXT_RUS,
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
