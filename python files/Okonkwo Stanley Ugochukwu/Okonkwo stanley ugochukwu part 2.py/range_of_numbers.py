for number in range(1000, 3000):
	if (number % 2 == 0):
		first_digit = number / 1000 % 10
		if (first_digit % 2 == 0):
			
			second_digit = number / 100 % 10
		if (second_digit % 2 == 0):
			
			third_digit = number / 10 % 10
		if (third_digit % 2 == 0):
	
			fourth_digit = number / 1 % 10
		if (fourth_digit % 2 == 0):
			print(first_digit, second_digit, third_digit, fourth_digit, end= ",")

