# initialised TTr
# prompted the user to enter the radius 
# prompted the user to enter the length of cylinder
# changed type int of user input to float
# calculate for the area and volume using the provided formular
# print out the values


TTr = 3.1416
radius= input('Enter the radius')
lenght_of_cylinder = input('Enter the length of the cylinder')
radius = float(radius)
lenght_of_cylinder = float(lenght_of_cylinder)
area = TTr * radius 
area = area * area
volume = area * lenght_of_cylinder

print("The area of a cylinder is : ", area)
print("The volume of a cylinder is :", volume)