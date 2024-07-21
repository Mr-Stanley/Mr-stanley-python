#question = int(input("What is your problem ?"))

question1 = bool(input("Have you had this problem before ?"))
if question1 != "yes" or "No":
	print("Invalid response")
elif question1 == "yes":
	print("Well, you have it again")

elif question1 == "No": 
	print("Well, you have it now")