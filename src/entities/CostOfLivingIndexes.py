class CostOfLivingIndexes:
    def __init__(
        self,
        cost_of_living,
        rent,
        cost_of_living_plus_rent,
        groceries,
        restaurant_price,
        local_purchasing_power,
    ):
        self.cost_of_living = float(cost_of_living)
        self.rent = float(rent)
        self.cost_of_living_plus_rent = float(cost_of_living_plus_rent)
        self.groceries = float(groceries)
        self.restaurant_price = float(restaurant_price)
        self.local_purchasing_power = float(local_purchasing_power)

    def __repr__(self):
        return (
            f"CostOfLivingIndexes(cost_of_living={self.cost_of_living}, rent={self.rent}, "
            f"cost_of_living_plus_rent={self.cost_of_living_plus_rent}, groceries={self.groceries}, "
            f"restaurant_price={self.restaurant_price}, local_purchasing_power={self.local_purchasing_power})"
        )
