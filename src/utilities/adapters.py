from src.entities.Location import Location
from src.entities.CostOfLivingIndexes import CostOfLivingIndexes


def json_to_location(json_data):
    return Location(
        country=json_data["country"],
        city=json_data["city"],
        state=json_data.get("state", None),
    )


def json_to_cost_of_living_indexes(json_data):
    return CostOfLivingIndexes(
        cost_of_living=json_data["cost_of_living"],
        rent=json_data["rent"],
        cost_of_living_plus_rent=json_data["cost_of_living_plus_rent"],
        groceries=json_data["groceries"],
        restaurant_price=json_data["restaurant_price"],
        local_purchasing_power=json_data["local_purchasing_power"],
    )
