discount_sum = 0.0
while True:
    user_input = input("Do you want to continue? (Yes/No): ")
    if user_input.lower() != "yes":
        break
    quantity = int(input("Enter quantity of the item: "))
    price = float(input("Enter price of the item: "))
    extended_price = quantity * price
    if extended_price > 10000.00:
        discount_percent = 0.25
    else:
        discount_percent = 0.10
    discount_amount = extended_price * discount_percent
    total = extended_price - discount_amount
    print("Extended Price: $", extended_price)
    print("Discount Amount: $", discount_amount)
    print("Total: $", total)
    discount_sum += discount_amount

print("Sum of all the discounts: $", discount_sum)