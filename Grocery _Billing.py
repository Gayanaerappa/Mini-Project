items = {}
total = 0

print("=== Grocery Billing System ===")
print("Type 'stop' as item name to finish\n")

while True:
    item_name = input("Enter item name: ")

    if item_name.lower() == "stop":
        break

    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    cost = price * quantity
    items[item_name] = cost
    total += cost

print("\n----- BILL -----")
for item, cost in items.items():
    print(item, ":", cost)

print("Total Amount:", total)

# Discount logic
if total >= 3000:
    discount = total * 0.15
elif total >= 1500:
    discount = total * 0.10
elif total >= 1000:
    discount = total * 0.05
else:
    discount = 0

final_amount = total - discount

print("Discount:", discount)
print("Final Amount to Pay:", final_amount)
print("----------------")
print("Thank you! Visit again")
