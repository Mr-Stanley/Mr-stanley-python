def my_discount(price, discount):
	""" display the discount percentage"""

	discount_price = price * discount / 100
	price = price - discount_price
    
	return print(price)
my_discount(1500, 15)