counter = 0
number_1 = 0
number_2 = 0
number_3 = 0
number_4 = 0
number_5 = 0
number = int(input("Enter an integer"))

while counter != 5:
	counter = counter + 1
	if counter == 1:
		number_1 = number // 10000 % 10
	if counter == 2:
		number_2 = number // 1000 % 10
	if counter ==3:
		number_3 = number // 100 % 10
	if counter ==4:
		number_4 = number // 10 % 10
	if counter ==5:
		number_5 = number // 1 % 10

print(number_1 , number_2 , number_3 , number_4 , number_5)

if number_1 == number_5 and number_2 == number_4:
	print("its a palindrome")
else: 
	print("its not a palindrome")

	

