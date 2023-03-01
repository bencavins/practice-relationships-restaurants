class Restaurant:
    def __init__(self, name):
        self.name = name
        self.reviews = []

    def get_name(self):
        return self.name
    
    def get_reviews(self):
        return self.reviews
    
    def average_rating(self):
        # total = 0
        # for review in self.reviews:
        #     total += review.rating
        # return total / len(self.reviews)
        return sum([review.get_rating() for review in self.reviews]) / len(self.reviews)

    def lowest_review(self):
        lowest_review = self.reviews[0]
        for curr_review in self.reviews:
            if curr_review.rating < lowest_review.rating:
                lowest_review = curr_review
        return lowest_review
    
        # return min(self.reviews, key=lambda review: review.rating)

    def get_customers(self):
        # result = []
        # for review in self.reviews:
        #     result.append(review.customer)
        # return result

        return [review.customer for review in self.reviews]


if __name__ == '__main__':
    from review import Review
    from customer import Customer

    restaurant = Restaurant('whatever')
    customer = Customer('a', 'b')
    r1 = Review(customer, restaurant, 5)
    r2 = Review(customer, restaurant, 1)
    restaurant.reviews = [r1, r2]
    print(restaurant.lowest_review())
