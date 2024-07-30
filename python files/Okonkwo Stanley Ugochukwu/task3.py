# initialised one foot to one meters to be 0.454
# prompt user to enter the value in pounds that they want to convert
# change the int value to float
# multiply the pounds value by the value of one pounds to kilograms value value of 0.454
# print the result


one_pounds_to_kilograms = 0.454
pounds_value = input('Enter the pounds value : ')

pounds_value = float(pounds_value)

kilograms_value = pounds_value * one_pounds_to_kilograms

print("The value of", pounds_value,"pounds", "in kilograms is", kilograms_value, 2, "kilograms")