cart = {}
total = 0

print("Online Shopping Cart")
print("Enter item name as 'stop' to finish")

while True:
    item = input("Enter item name: ")

    if item.lower() == "stop":
        break

    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    cart[item] = price * quantity

for item in cart:
    total += cart[item]

print("\n--- BILL ---")
for item, cost in cart.items():
    print(item, ":", cost)

print("Total Amount:", total)

# Discount
if total >= 3000:
    discount = total * 0.15
elif total >= 1500:
    discount = total * 0.10
else:
    discount = 0

print("Discount:", discount)
print("Final Payable:", total - discount)
