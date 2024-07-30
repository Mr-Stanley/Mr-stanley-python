# prompt user to enter sets of digits
# change integer value to float
# seperate the digits
# sum the seperated numbers
# change the float values back to integers
# print the sum


digits = input("Enter digits value : ")
digits = float(digits)

first_number = digits // 100
second_number = digits // 10 % 10
third_number = digits // 1 % 10


sum_of_numbers = first_number + second_number + third_number
sum_of_numbers = int(sum_of_numbers)
print("The sum of entered digits is : ", sum_of_numbers)