miles_driven = 0
gallons_used = 0
counter = 0
miles_per_gallon = 0

while gallons_used != -1:
	gallons_used = float(input("Enter gallons used: "))
	miles_driven = int(input("Enter Miles driven: "))
if gallons_used == -1:
		miles_per_gallon = miles_driven / gallons_used
print(miles_per_gallon)