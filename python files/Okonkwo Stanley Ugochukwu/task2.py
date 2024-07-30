# initialised one foot to one meters to be 0.305
# prompt user to enter the value in feet that they want to convert
# change the int value to float
# multiply the feet value by the value of one feet to meters value of 0.305
# print the result


one_foot_to_meters = 0.305
feet_value = input('Enter the feet value : ')

feet_value = float(feet_value)

meters_value = feet_value * one_foot_to_meters

print("The value of", feet_value,"feets", "in meters is", meters_value, "meters")