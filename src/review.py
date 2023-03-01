class Review:
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
    
    def get_rating(self):
        return self.rating

    def get_restaurant(self):
        return self.restaurant
    
    def get_customer(self):
        return self.customer
    
    def __repr__(self) -> str:
        return f'<Review {self.rating}>'