# @date: 11.08.2024
# @author: vladddd46
# @brief: responsible for retrieving and parsing 'cost of living indexes' data
from src.utilities.utils import is_file_exist, save_json_data, read_json_file
from src.utilities.Logger import logger
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta


class ScrapperImpl:

    def __init__(self, url):
        self.m_url = url

    def __get_html(self):
        response = requests.get(self.m_url)
        html_content = ""
        if response.status_code == 200:
            html_content = response.text
        else:
            logger.error(f"Can not get html page | status_code={response.status_cod}")
        return html_content

    def __parse(self, html_content):
        result_json = None
        if html_content != "":
            soup = BeautifulSoup(html_content, "html.parser")
            table = soup.find("table", {"id": "t2"})
            headers = []
            data = []

            # retrieving the indexes data
            for th in table.find_all("th"):
                headers.append(th.text.strip())
            for row in table.find_all("tr")[
                1:
            ]:  # Skip the first row if it contains headers
                cols = row.find_all("td")
                data.append([col.text.strip() for col in cols])
            df = pd.DataFrame(data, columns=headers)
            result_json = df.to_dict(orient="records")
        else:
            logger.error(f"html content is empty")
        return result_json

    def __correct_city_naming_mistakes(self, city):
        result = city
        if city == "Kiev (Kyiv)":
            result = "Kyiv"
        elif city == "Odessa (Odesa)":
            result = "Odesa"
        return result

    def __format_location(self, location):
        splt_location = location.split(",")
        city = self.__correct_city_naming_mistakes(splt_location[0])
        if len(splt_location) == 2:
            result = {
                "country": splt_location[1][1:],
                "city": city,
                "state": "",
            }
        else:
            result = {
                "country": splt_location[2][1:],
                "city": city,
                "state": splt_location[1][1:],
            }
        return result

    def __format(self, unformatted_json):
        res = []

        if unformatted_json != None:
            for elem in unformatted_json:
                tmp = {}
                tmp["location"] = {}

                splt_location = self.__format_location(elem["City"])
                tmp["location"]["country"] = splt_location["country"]
                tmp["location"]["state"] = splt_location["state"]
                tmp["location"]["city"] = splt_location["city"]

                tmp["indexes"] = {}
                tmp["indexes"]["cost_of_living"] = elem["Cost of Living Index"]
                tmp["indexes"]["rent"] = elem["Rent Index"]
                tmp["indexes"]["cost_of_living_plus_rent"] = elem[
                    "Cost of Living Plus Rent Index"
                ]
                tmp["indexes"]["groceries"] = elem["Groceries Index"]
                tmp["indexes"]["restaurant_price"] = elem["Restaurant Price Index"]
                tmp["indexes"]["local_purchasing_power"] = elem[
                    "Local Purchasing Power Index"
                ]
                res.append(tmp)
        else:
            logger.error(f"Formatting failed: unformatted_json is None.")
        return res

    def __rescrap(self):
        formatted_indexes_data_json = None
        try:
            html_page = self.__get_html()
            indexes_data_unformatted_json = self.__parse(html_page)
            indexes_data = self.__format(indexes_data_unformatted_json)
            formatted_indexes_data_json = {
                "date": datetime.now(),
                "content": indexes_data,
            }
        except Exception as e:
            logger.error(f"Exception occured: {e}")
        return formatted_indexes_data_json

    def get_indexes_data(self, path_to_cache_file):
        result = None
        try:
            if is_file_exist(path_to_cache_file) == True:
                result = read_json_file(path_to_cache_file)

            # we should do rescrapping if:
            #  * no cached file
            #  * data is older than 30 days.
            if result == None or (
                result != None and result["date"] + timedelta(days=30) < datetime.now()
            ):
                result = self.__rescrap()
                logger.info(
                    f"Scrapping 'cost of living indexes' data | result is None = {result == None}"
                )

            if result != None:
                save_json_data(
                    path_to_cache_file, result
                )  # save the result for next use
        except Exception as e:
            logger.error(f"Exception occured: {e}")
        return result
