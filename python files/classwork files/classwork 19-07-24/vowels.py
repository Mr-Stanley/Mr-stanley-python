words = str(input("Enter a word to check the vowels and consonant "))
def check_vow(string, vowels)

consonants = 0
vowels = 0
for character in words:
    if character == "a":
        vowels = vowels + 1
    elif character == "e":
        vowels = vowels + 1
    elif character == "i":
        vowels = vowels + 1
    elif character == "o":
        vowels = vowels + 1
    elif character == "u":
        vowels = vowels + 1
    else :
        consonants = consonants + 1
        
print(words, " the count of vowels is", vowels, "and", consonants)







word = input(enter your word)

vowels = ' '
cpnsonant = ' '
 for character.lower() in ['a', 'e', 'i' 'o' 'u']:
     vowels += characterelse:
         cpnsonant += characterprint(f"the number of vowels os {len(set(vowel))}\nthe number of consonant is {lens(set(consonant))}")
