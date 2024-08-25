from src.tech_config import INDEXES_DATA_SRC_PAGE, CACHED_INDEXES_DATA
from src.interfaces.Scrapper import Scrapper
from src.utilities.Logger import logger

if __name__ == "__main__":
	logger.info("=Program started=")
	scrapper = Scrapper(INDEXES_DATA_SRC_PAGE, CACHED_INDEXES_DATA)
	data = scrapper.get_indexes_data_in_json()

	logger.info("=Program ended=")