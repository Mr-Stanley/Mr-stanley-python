final_account_value = 5000
number_of_months = 36
monthly_intrest_rates = final_account_value / number_of_months
initial_deposit_amount = final_account_value / (1 + monthly_intrest_rates) ** 36
print(initial_deposit_amount)


