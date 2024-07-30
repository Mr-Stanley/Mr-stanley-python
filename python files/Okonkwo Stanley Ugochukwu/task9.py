name = input("Enter employes name")
number_of_hours = input("Enter the number of hours worked in a week : ")
hourly_pay_rate = input("Enter the hourly pay rates : ")
fedral_tax = input("Enter the fedral withholding rate : ")
state_tax = input("Enter the state tax withholding rate : ")

number_of_hours = float(number_of_hours)
hourly_pay_rate = float(hourly_pay_rate)
fedral_tax = float(fedral_tax)
state_tax = float(state_tax)

gross_pay = number_of_hours * hourly_pay_rate
fedral_percent = fedral_tax * 100
state_percent = state_tax * 100
fedral_withholding = fedral_tax * gross_pay
state_withholding = state_tax * gross_pay
total_deductions = fedral_withholding + state_withholding
net_pay = gross_pay - total_deductions

print("Employers name", name,)
print( " Hours worked : ", number_of_hours, )
print("pay rates is : ", hourly_pay_rate,)
print("Gross pay is : ", gross_pay)
print("Deductions")
print("state withholdings is : ", fedral_percent,"%", fedral_withholding)
print("state withholdings is : ", state_percent, "%", state_withholding)
print("total deductions is : ", total_deductions)
print("net pay : ", net_pay)