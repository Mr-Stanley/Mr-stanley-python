counter = 0
while counter != 10:
	counter = counter + 1
	print('*' * counter)
counter = counter + 1

print("  ")

counter = 11
while counter != 0:
	counter = counter - 1
	print('*' * counter)
counter = counter - 1
print(" ")
counter = 0
while counter != 10:
	counter = counter + 1
	print(f"{counter * '*' : >10}")
counter = counter + 1
print(" ")
counter = 11
while counter != 0:
	counter = counter - 1
	print(f"{counter * '*' : >10}")
counter = counter - 1
print(" ")
