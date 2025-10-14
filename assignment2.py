name = input("Enter your family name: ")
income = float(input("Enter your combined monthly income: "))

rent = float(input("How much money you spent for rent or motgage?\n"))
insurence = float(input("How much money you spent for insurence?\n"))
car_payment = float(input("Enter car payment: "))
utilities = float(input("How much money you spent for  utilities: "))

groceries = float(input("How much money you spent for  groceries?\n"))
childcare = float(input("How much money you spent for  childcare?\n"))
family_activities = float(input('How much money you spent for  family activities?\n'))

current_fund = float(input("Enter current vacation fund balance: "))
vacation_cost = float(input("Enter vacation cost  target: "))
months = int(input("Enter months until vacation date: "))


fixed_exp = rent + insurence + car_payment + utilities
variable_exp = groceries + childcare + family_activities

total_expenses = fixed_exp + variable_exp
monthly_savings = income - total_expenses
savings_rate = monthly_savings / income * 100
projected_fund = current_fund + monthly_savings * months
total_needed = vacation_cost - current_fund
monthly_needed = total_needed / months
surplus_shortfall = monthly_savings - monthly_needed
total_shortfall = projected_fund - vacation_cost

emergency_status = savings_rate < 10
needs_improvement = savings_rate >= 10 and savings_rate < 15
stable = savings_rate >= 15 and savings_rate < 25
strong = savings_rate >= 25
vacation_affordable = projected_fund >= vacation_cost

print()
print("#" * 40)
print("         FAMILY BUDGET PLANNER")
print("#" * 40)
print("-" * 40)
print(f"Family name: {name}")
print("-" * 40)
print(f"Total fixed expenses:      {fixed_exp:.2f}sum")
print(f"Total variable expenses:   {variable_exp:.2f}sum")
print(f"Total monthly expenses:    {total_expenses:.2f}sum\n")
print("-" * 40)
print(f"Monthly savings potential: {monthly_savings:.2f}sum")
print(f"Savings rate percentage:   {savings_rate:.2f}%")
print(f"Current vacation fund:     {current_fund:.2f}sum")
print(f"Projected fund at vacation date: {projected_fund:.2f}sum\n")
print("-" * 40)
print(f"Target vacation cost:       {vacation_cost:.2f}sum")
print(f"Total amount needed:        {total_needed:.2f}sum")
print(f"Monthly savings needed:     {monthly_needed:.2f}sum")
print(f"Monthly shortfall/surplus:  {surplus_shortfall:.2f}sum\n")
print("-" * 40)

print(f"All financial health indicators: ")
print(f"Emergency status (< 10%):        {emergency_status}")
print(f"Needs improvement (10% - 14.9%): {needs_improvement}")
print(f"Stable (15% - 24.9%):            {stable}")
print(f"Strong (>= 25%):                 {strong}")
print(f"Vacation affordability status:   {vacation_affordable}")
print(f"Total gap at vacation date:      {total_shortfall:.2f}")
print("-" * 40)
print("#" * 40)
print()