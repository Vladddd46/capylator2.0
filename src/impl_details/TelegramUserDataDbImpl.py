from src.utilities.utils import is_file_exist, read_json_file, save_json_data


class TelegramUserDataDbImpl:
    def __init__(self, db_path):
        self.db_path = db_path
        if is_file_exist(self.db_path) == False:
            save_json_data(self.db_path, {})

    def __is_user_exists(self, user_id, data):
        return user_id in data.keys()

    def __create_user(self, user_id, language, data):
        data[user_id] = {
            "language": language,
            "current_location": {"country": "Ukraine", "state": "None", "city": "Kyiv"},
            "current_spendings": 1000,
        }

    def get_user_language(self, user_id):
        user_id = str(user_id)
        data = read_json_file(self.db_path)
        if user_id in data.keys():
            return data[user_id]["language"]
        return None

    def is_user_exist(self, user_id):
        user_id = str(user_id)
        data = read_json_file(self.db_path)
        return self.__is_user_exists(user_id, data)

    def chooseLanguage(self, user_id, language):
        user_id = str(user_id)
        data = read_json_file(self.db_path)

        if self.__is_user_exists(user_id, data) == True:
            data[user_id]["language"] = language
        else:
            self.__create_user(user_id, language, data)

        save_json_data(self.db_path, data)
