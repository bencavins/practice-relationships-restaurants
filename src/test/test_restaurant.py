from restaurant import Restaurant
from customer import Customer
from review import Review


def test_restaurant_init_name():
    """
    Should be able to initialize a restaurant with a name
    """
    restaurant = Restaurant("Monk's Cafe")
    assert restaurant.name == "Monk's Cafe"

def test_restaurant_get_name():
    """
    get_name() should return the restaurant's name
    """
    restaurant = Restaurant("Monk's Cafe")
    restaurant.get_name() == "Monk's Cafe"

def test_restaurant_get_reviews():
    """
    get_reviews() should return the list of reviews
    for the restaurant
    """
    restaurant = Restaurant("Monk's Cafe")
    customer = Customer('Jane', 'Doe')
    review = Review(customer, restaurant, 5)
    restaurant.reviews = [review]
    assert restaurant.get_reviews() == [review]


def test_restaurant_lowest_review():
    restaurant = Restaurant("Monk's Cafe")
    customer = Customer('Jane', 'Doe')
    review1 = Review(customer, restaurant, 5)
    review2 = Review(customer, restaurant, 1)
    restaurant.reviews = [review1, review2]
    assert restaurant.lowest_review() == review2

def test_restaurant_average_rating():
    restaurant = Restaurant("Monk's Cafe")
    customer = Customer('Jane', 'Doe')
    review1 = Review(customer, restaurant, 5)
    review2 = Review(customer, restaurant, 1)
    restaurant.reviews = [review1, review2]
    assert restaurant.average_rating() == 3