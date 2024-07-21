counter = 1
factors = 1
number =int(input("Enter an integer"))
while counter <= number :
	
	number -= 1
	print((number+1),"", end="")

	factors *=number+1
print('\n',factors)




	#sum = counter * counter
	#counter = counter + 1
	#print(sum)