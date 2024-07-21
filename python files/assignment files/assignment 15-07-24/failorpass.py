passmark = 0
fail = 0

for number in range(15):

	score = int(input('Enter a score: '))
	if score >= 45 and score < 101:
		passmark += 1
	elif score < 45:
		fail += 1
print(" number of pass students :", passmark)
print(" number of fail students :", fail)