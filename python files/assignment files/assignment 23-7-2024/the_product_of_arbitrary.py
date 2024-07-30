def  the_product_of_arbitrary(*numbers):
	product = 1
	for num in numbers:
    		product*= num
	return product
print(the_product_of_arbitrary(1, 3, 5, 7, 9))