cost_of_car = int(input("Enter the cost of your car : "))
road_tax = 0

if cost_of_car >= 5000000 :
	road_tax = cost_of_car * (25 / 100)
	print("The Road Tax amount is : ", road_tax)
		
if cost_of_car < 5000000 and  cost_of_car >= 3000000:
	road_tax = cost_of_car * (20 / 100)
	print("The Road Tax amount is : ", road_tax)

if cost_of_car < 3000000 and cost_of_car >= 1000000 :
	road_tax = cost_of_car * (15 / 100)
	print("The Road Tax amount is : ", road_tax)
		
if cost_of_car < 1000000 :
	road_tax = cost_of_car * (10 / 100)
	print("The Road Tax amount is : ", road_tax)