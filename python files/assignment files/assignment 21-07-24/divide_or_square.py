def divide_or_square(number):
	if number % 5 == 0:
		result =(number)**0.5
	
	else:
		result = number % 5
	return print(result)

divide_or_square(10)
