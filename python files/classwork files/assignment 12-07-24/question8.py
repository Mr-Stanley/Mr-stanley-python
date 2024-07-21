counter = 0
number_1 = 0
number_2 = 0
number_3 = 0
number_4 = 0

while counter != 4:
	number = int(input("enter next integer"))
	counter = counter + 1
	if counter ==1:
		number_1 = number
	elif counter ==2:
		number_2 = number
	elif counter ==3:
		number_3 = number
	elif counter ==4:
		number_4 = number
sum = number_1 + number_2 + number_3 + number_4
average = number_1 + number_2 + number_3 + number_4 / counter
product = number_1 * number_2 * number_3 * number_4
if number_1 > number_2 and number_1 > number_3 and number_1 > number_4:
	print(number_1, "is the largest number")
elif number_2 > number_1 and number_2 > number_3 and number_3 > number_4:
	print(number_2, "is the largest number")
elif number_3 > number_1 and number_3 > number_2 and number_3 > number_4:
	print(number_3, "is the largest number")
elif number_4 > number_1 and number_4 > number_2 and number_4 > number_3:
	print(number_4, "is the largest number")

if number_1 < number_2 and number_1 < number_3 and number_1 < number_4:
	print(number_1, "is the Smallest number")
elif number_2 < number_1 and number_2 < number_3 and number_3 < number_4:
	print(number_2, "is the Smallest number")
elif number_3 < number_1 and number_3 < number_2 and number_3 < number_4:
	print(number_3, "is the Smallest number")
elif number_4 < number_1 and number_4 < number_2 and number_4 < number_3:
	print(number_4, "is the Smallest number")

print(sum, "is the sum of the four numbers")
print(average, "is the average of four numbers")
print(product, " is the product of the four numbers")






	
