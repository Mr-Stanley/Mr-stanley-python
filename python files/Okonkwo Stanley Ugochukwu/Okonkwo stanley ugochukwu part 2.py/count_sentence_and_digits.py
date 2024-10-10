no_of_words = 0

no_of_digits = 0


digits = input("Enter words: ")

for characters in digits:
	if characters >= 'a' and characters <= 'z' or characters == " " :
		no_of_words +=1
	if characters >= '1' and characters <= '9':
		no_of_digits +=1
 
print(f"LETTERS {no_of_words} DIGITS {no_of_digits}")