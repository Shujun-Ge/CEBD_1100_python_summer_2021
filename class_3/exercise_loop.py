# Exercise about 'if'

customer_type = input("Please enter your customer type")
invoice_total = float(input("Please enter the total invoice"))
discount_percent = 0

if customer_type == "W":
    if invoice_total < 500:
        discount_percent = 0.4
    else:
        discount_percent = 0.5
else:
    pass

if customer_type == "R":
    if invoice_total < 100:
        discount_percent = 0
    elif 100 <= invoice_total < 250:
        discount_percent = 0.1
    else:
        discount_percent = 0.2
else:
    pass

