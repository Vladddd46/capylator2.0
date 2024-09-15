class Location:

    def __init__(self, country, city, state=None):
        self.country = country
        self.city = city
        self.state = state

    def __eq__(self, other):
        if isinstance(other, Location):
            return (
                self.country == other.country
                and self.city == other.city
                and self.state == other.state
            )
        return False
