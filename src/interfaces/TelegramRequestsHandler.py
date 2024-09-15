from src.impl_details.TelegramRequestsHandlerImpl import TelegramRequestsHandlerImpl


class TelegramRequestsHandler:
    def __init__(self):
        self.requests_handler = TelegramRequestsHandlerImpl()

    def onStartCommand(self, message):
        self.requests_handler.onStartCommand(message)

    def onInfoCommand(self, message):
        self.requests_handler.onInfoCommand(message)

    def onCalculateCommand(self, message):
        self.requests_handler.onCalculateCommand(message)

    def onInlineButtonClick(self, call):
        self.requests_handler.onInlineButtonClick(call)
