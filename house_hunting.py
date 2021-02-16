# Write your code here

# current_savings = 0
# annual_salary = 120000
# monthly_salary = 10000   # annual_salary/12
# portion_saved = 10%
# monthly_amount_saved = monthly_salary*portion_saved
# interest_earned = current_savings*.04/12
# monthly_amount_saved + interest_earned


def months_required():
    months_required = 0
    annual_salary = int(input("What is your salary?"))
    portion_saved = float(input("What would percent you like to save?"))
    total_cost = int(input("Cost of dream house?"))
    portion_down_payment = 0.25
    down_payment = total_cost*portion_down_payment
    r = float(.04)
    current_savings = 0
    while current_savings < down_payment:
        current_savings += ((annual_salary/12) * portion_saved) + (current_savings * (r/12))
        print(current_savings)
        months_required += 1
        print("It will take you", months_required,"months to save for a down payment your house.")


months_required()




