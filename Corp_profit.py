print("=== Farmer Crop Profit Calculator ===")

crop_name = input("Enter crop name: ")
area = float(input("Enter land area (in acres): "))
cost_per_acre = float(input("Enter cost per acre: "))
yield_per_acre = float(input("Enter yield per acre (kg): "))
price_per_kg = float(input("Enter market price per kg: "))

# Calculations
total_cost = area * cost_per_acre
total_yield = area * yield_per_acre
total_income = total_yield * price_per_kg
profit = total_income - total_cost

print("\n--- Crop Report ---")
print("Crop Name:", crop_name)
print("Total Cost:", total_cost)
print("Total Yield (kg):", total_yield)
print("Total Income:", total_income)

if profit > 0:
    print("Profit:", profit)
elif profit < 0:
    print("Loss:", abs(profit))
else:
    print("No Profit No Loss")