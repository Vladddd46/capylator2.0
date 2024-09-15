class CostOfLivingCalculatorImpl:

    @staticmethod
    def calculate(
        current_location_spending,
        current_location_index,
        expected_location_index,
    ):
        cost_difference = expected_location_index / current_location_index
        new_spending = current_location_spending * cost_difference
        return new_spending
