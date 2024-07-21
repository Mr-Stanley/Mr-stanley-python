accountbalance = 0
counter = 0
depositvalue = 0   
withdrawalvalue = 0
accountbalance = 0

while depositvalue != 4:
    print("Welcome to Okoko Pos Terminal")
    print("Select a number to continue")
    print('''   1. Deposit.
             2. Withdrawal.
             3. Check Balance.
             4. Terminate session. ''')
    depositvalue = input("Select a number to continue")   
    
if depositvalue == 1:
    depositvalue =(input("Press an amount to Deposit"))
    accountbalance = depositvalue + accountbalance 
    print("Your account balance is : ", accountbalance)

elif depositvalue == 2:
    print("Enter an amount you want to withdraw")
    withdrawvalue = int(input("press an amount to withdraw"))
if (withdrawalvalue > accountbalance):
         print("Insufficient Funds")
if (withdrawalvalue < 0):
         print("Invalid Amount")
elif (withdrawvalue < accountbalance):
       accountbalance = accountbalance - withdrawvalue
       print("Thank you for withdrawing Your new account balance is : ", newaccountbalance)
elif number == 3:
        print(accountbalance)
elif number == 4:
    print("Thank you for using Okoko Pos Terminal see you next time")

   

   
    
    
    
    
    
    