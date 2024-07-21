number = int(input("Enter first number: "))
number1 = int(input("Enter second number: "))
number2 = int(input("Enter third number: "))

sum = number + number1 + number2
print("The sum of", number, number1, number2, "is", sum)

average = number + number1 + number2 / 3
print("The average of", number, number1, number2, "is", average)

product =  number * number1 * number2
print("The product of", number, number1, number2, "is", product)

if number > number1 and number > number2:
    print(number, "is the largest number")
elif number1 > number and number1 > number2:
    print(number1, "is the largest number")
else:print(number2, "is the largest number")

if number < number1 and number < number2:
    print(number, "is the smallest number")
elif number1 < number and number1 < number2:
    print(number1, " is the smallest number")
else: print(number2, "is the smallesr number")