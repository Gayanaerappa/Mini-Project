items = {}
subtotal = 0

GST_RATE = 0.05   # 5% GST

print("=== Grocery Billing System (GST Included) ===")
print("Type 'stop' to finish adding items\n")

while True:
    name = input("Enter item name: ")

    if name.lower() == "stop":
        break

    price = float(input("Enter price per item: "))
    qty = int(input("Enter quantity: "))

    cost = price * qty
    items[name] = cost
    subtotal += cost

# GST Calculation
gst_amount = subtotal * GST_RATE
total_with_gst = subtotal + gst_amount

# Discount rules
if total_with_gst >= 3000:
    discount = total_with_gst * 0.10
elif total_with_gst >= 1500:
    discount = total_with_gst * 0.05
else:
    discount = 0

final_amount = total_with_gst - discount

# Bill Printing
print("\n--------- BILL ---------")
for item, cost in items.items():
    print(item, ":", cost)

print("------------------------")
print("Subtotal:", subtotal)
print("GST (5%):", gst_amount)
print("Amount with GST:", total_with_gst)
print("Discount:", discount)
print("Final Amount to Pay:", final_amount)
print("------------------------")
print("Thank you! Visit Again ")
