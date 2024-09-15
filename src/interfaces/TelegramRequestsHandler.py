from src.impl_details.TelegramRequestsHandlerImpl import TelegramRequestsHandlerImpl
from src.tech_config import INDEXES_DATA_SRC_PAGE, CACHED_INDEXES_DATA
from src.interfaces.IndexesScrapper import IndexesScrapper


class TelegramRequestsHandler:
    def __init__(self):
        self.requests_handler = TelegramRequestsHandlerImpl()
        self.scrapper = IndexesScrapper(INDEXES_DATA_SRC_PAGE, CACHED_INDEXES_DATA)

    def onStartCommand(self, message):
        self.requests_handler.onStartCommand(message)

    def onInfoCommand(self, message):
        self.requests_handler.onInfoCommand(message)

    def onCalculateCommand(self, message):
        # costOfLivingIndexesData = self.scrapper.get_indexes_data()
        self.requests_handler.onCalculateCommand(message)

    def onInlineButtonClick(self, call):
        self.requests_handler.onInlineButtonClick(call)
