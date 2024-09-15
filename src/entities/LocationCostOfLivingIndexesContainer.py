class LocationCostOfLivingIndexesContainer:

    def __init__(self, init_list=[]):
        self.container = []
        for i in init_list:
            self.container.append(i)

    def add(self, elem):
        self.container.append(elem)

    def get_unique_countries(self):
        # Use a set to ensure uniqueness of country names
        countries = {pair.location.country for pair in self.container}
        return list(countries)

    def get_unique_states_by_country(self, country):
        # Use a set to ensure uniqueness of state names
        states = {
            location.state
            for location in self.container
            if location.country == country and location.state is not None
        }
        return list(states)

    def get_unique_cities_by_country_and_state(self, country, state=None):
        # Use a set to ensure uniqueness of city names
        cities = {
            location.city
            for location in self.container
            if location.country == country and location.state == state
        }
        return list(cities)

    def size(self):
        return len(self.container)

    def get_cost_of_living_indexes_by_location(self, location):
        for elem in self.container:
            if elem.location == location:
                return elem.const_of_living_indexes
        return None
