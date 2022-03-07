from datetime import datetime

disc_rate = 0.10
sales_tax_rate = 0.06

user_subtotal = float(input("Please enter the subtotal: "))

current_date_and_time = datetime.now()
weekday = current_date_and_time.weekday()

if user_subtotal >= 50 and (weekday == 1 or weekday == 2):
    discount = round(user_subtotal * disc_rate, 2)
    print(f"Discount amount: {discount}")
    user_subtotal -= discount

sales_tax = round(user_subtotal * sales_tax_rate , 2)
print(f"Sales tax amount: {sales_tax}")

total = user_subtotal + sales_tax
print(f"Total: {total:.2f}")