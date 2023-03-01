from customer import Customer
from restaurant import Restaurant
from review import Review


def test_customer_init_first_and_last_name():
    """
    Should be able to initialize a customer with a first and last name
    """
    customer = Customer('Jane', 'Doe')
    assert customer.first_name == 'Jane'
    assert customer.last_name == 'Doe'

def test_customer_get_first_name():
    """
    get_first_name() should return the customer's first name
    """
    customer = Customer('Jane', 'Doe')
    assert customer.get_first_name() == 'Jane'

def test_customer_get_last_name():
    """
    get_last_name() should return the customer's last name
    """
    customer = Customer('Jane', 'Doe')
    assert customer.get_last_name() == 'Doe'

def test_customer_get_full_name():
    """
    get_full_name() should return the customer's full name
    """
    customer = Customer('Jane', 'Doe')
    assert customer.get_full_name() == 'Jane Doe'

def test_customer_get_reviews():
    """
    get_reviews() should return the list of reviews
    written by the customer
    """
    customer = Customer('Jane', 'Doe')
    restaurant = Restaurant('Applebees')
    review = Review(customer, restaurant, 4)
    customer.reviews = [review]
    assert customer.get_reviews() == [review]

def test_customer_add_review():
    """
    add_review(restaurant, rating) should create a new
    Review object and add it to both the customer
    and the given restaurant
    """
    customer = Customer('Jane', 'Doe')
    restaurant = Restaurant('Applebees')
    customer.add_review(restaurant, 5)
    assert customer.reviews[0].rating == 5

def test_customer_review_count():
    """
    review_count() should return the count of reviews
    made by this customer
    """
    customer = Customer('Jane', 'Doe')
    restaurant = Restaurant('Applebees')
    review = Review(customer, restaurant, 5)
    customer.reviews = [review]
    assert customer.review_count() == 1

def test_customer_get_restaurants():
    customer = Customer('Jane', 'Doe')
    restaurant = Restaurant('Applebees')
    review = Review(customer, restaurant, 5)
    customer.reviews = [review]
    assert customer.get_restaurants() == [restaurant]
