class RestaurantResource(object):
    def __init__(self, name, description=None, rating=None):
        # apply some validations

        self.name = name
        self.address = address
        self.type = type
        self.budget = budget.upper() if budget is not None else budget
        self.description = description
        self. rating = int(rating) if rating is not None else rating
    