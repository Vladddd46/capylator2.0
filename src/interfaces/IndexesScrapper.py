# @date: 25.08.2024
# @author: vladddd46
# @brief: interface for getting 'cost of living' indexes
from src.impl_details.ScrapperImpl import ScrapperImpl


class IndexesScrapper:

    # url - webpage with 'cost of living' indexes data.
    # path_to_cache_file - cached data stored in order not to always do reparsing.
    def __init__(self, url, path_to_cache_file):
        self._m_impl = ScrapperImpl(url)
        self._m_path_to_cache_file = path_to_cache_file

    def get_indexes_data_in_json(self):
        result = self._m_impl.get_indexes_data(self._m_path_to_cache_file)
        return result
