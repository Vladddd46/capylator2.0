from src.tech_config import INDEXES_DATA_SRC_PAGE, CACHED_INDEXES_DATA
from src.interfaces.IndexesScrapper import IndexesScrapper
from src.utilities.Logger import logger
from src.entities.LocationCostOfLivingIndexesContainer import (
    LocationCostOfLivingIndexesContainer,
)
from src.entities.LocationCostOfLivingIndexesPair import LocationCostOfLivingIndexesPair
from src.utilities.adapters import json_to_location, json_to_cost_of_living_indexes


def get_cost_of_living_indexes():
    scrapper = IndexesScrapper(INDEXES_DATA_SRC_PAGE, CACHED_INDEXES_DATA)
    data = scrapper.get_indexes_data_in_json()

    indexesDataContainer = LocationCostOfLivingIndexesContainer()
    for i in data["content"]:
        location = json_to_location(i["location"])
        costOfLivingIndexes = json_to_cost_of_living_indexes(i["indexes"])
        pair = LocationCostOfLivingIndexesPair(location, costOfLivingIndexes)
        indexesDataContainer.add(pair)
    return indexesDataContainer


if __name__ == "__main__":
    logger.info("=Program started=")
    indexesDataContainer = get_cost_of_living_indexes()

    logger.info("=Program ended=")
