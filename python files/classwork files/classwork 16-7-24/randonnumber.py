from random import *
count = 0


random_number = randint(1, 1000)
number = 0
access = str(input("Yes" and "No"))
access == 'Yes'

while number != No :
     count = count + 1
     number = int(input(" Guess a random number between 1-1000 with the fewest guess: "))   
 
if (number > random_number) :
        print(" Too High, play again")
        
if (number < random_number):
        print(" Too low, Try again")
        
        
if (number == random_number) :
        print("Congratulations oil dey your head")
        print("Thank you for guessing correctly")
        print("The number of attempts is ", count)
        access = str(input("Enter 'Yes' to play or 'No' to terminate"))
        if number == 'Yes' :
                number = int(input(" Guess a random number between 1-1000 with the fewest guess: ")) 
                number = random_number(1, 1000)
        else :  break
        
