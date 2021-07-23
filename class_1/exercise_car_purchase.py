# Exercise - Calculate months and days from year difference


current_year = 2021     # We should be using the "Date" function here normally.
print("input the year your purchase your car:")
purchase_year = int(input())


year_difference = (current_year - purchase_year)
number_months = year_difference * 12

print(number_months)
