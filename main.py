from src.tech_config import INDEXES_DATA_SRC_PAGE, CACHED_INDEXES_DATA
from src.interfaces.Scrapper import Scrapper


if __name__ == "__main__":
	scrapper = Scrapper(INDEXES_DATA_SRC_PAGE, CACHED_INDEXES_DATA)
	data = scrapper.get_indexes_data_in_json()
	
	print(data)