# @date: 11.08.2024
# @author: vladddd46
# @brief: responsible for retrieving and parsing 'cost of living indexes' data
from src.utils import is_file_exist, save_json_data, read_json_file
import requests
from bs4 import BeautifulSoup
import pandas as pd


class ScrapperImpl:

    def __init__(self, url):
        self.m_url = url

    def __get_html(self):
        response = requests.get(self.m_url)

        html_content = ""
        if response.status_code == 200:
            html_content = response.text
        else:
            # TODO: write into log, that request failed.
            pass
        return html_content

    def __parse(self, html_content):
        result_json = ""
        if html_content != "":
            soup = BeautifulSoup(html_content, "html.parser")
            table = soup.find("table", {"id": "t2"})
            headers = []
            data = []

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
            pass  # TODO: print log that html content is empty
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
        return res

    def __rescrap(self):
        formatted_indexes_data_json = ""
        try:
            html_page = self.__get_html()
            indexes_data_unformatted_json = self.__parse(html_page)
            formatted_indexes_data_json = self.__format(indexes_data_unformatted_json)
        except Exception as e:
            # TODO: write log here
            print("Exception: ", e)
        return formatted_indexes_data_json

    def get_indexes_data(self, path_to_cache_file):
        if is_file_exist(path_to_cache_file) == False:
            result = (
                self.__rescrap()
            )  # if no file with indexes data, then we scrap and parse the webpage
            if result != "":
                save_json_data(path_to_cache_file, result)  # save the result for next use
        else:
            result = read_json_file(path_to_cache_file)
        return result
