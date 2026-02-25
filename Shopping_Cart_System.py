# Shopping Cart System

products = {
    1: {"name": "Laptop", "price": 50000},
    2: {"name": "Mobile", "price": 20000},
    3: {"name": "Headphones", "price": 2000},
    4: {"name": "Keyboard", "price": 1500},
    5: {"name": "Mouse", "price": 800}
}

cart = {}

# Display Products
def view_products():
    print("\n📦 Available Products:")
    for pid, item in products.items():
        print(f"{pid}. {item['name']} - ₹{item['price']}")
    print()


# Add to Cart
def add_to_cart():
    view_products()
    try:
        pid = int(input("Enter product ID to add: "))
        qty = int(input("Enter quantity: "))

        if pid in products:
            if pid in cart:
                cart[pid] += qty
            else:
                cart[pid] = qty
            print("✅ Product added to cart!\n")
        else:
            print("❌ Invalid Product ID\n")
    except ValueError:
        print("⚠️ Please enter valid numbers\n")


# Remove from Cart
def remove_from_cart():
    if not cart:
        print("🛒 Cart is empty!\n")
        return

    view_cart()
    try:
        pid = int(input("Enter product ID to remove: "))
        if pid in cart:
            del cart[pid]
            print("🗑️ Product removed from cart!\n")
        else:
            print("❌ Product not in cart\n")
    except ValueError:
        print("⚠️ Invalid input\n")


# View Cart
def view_cart():
    if not cart:
        print("🛒 Cart is empty!\n")
        return

    print("\n🛍️ Your Cart:")
    total = 0
    for pid, qty in cart.items():
        name = products[pid]["name"]
        price = products[pid]["price"]
        subtotal = price * qty
        total += subtotal
        print(f"{name} | Qty: {qty} | Subtotal: ₹{subtotal}")

    print(f"\n💰 Total Bill: ₹{total}\n")


# Main Menu
def main():
    while True:
        print("====== 🛒 Shopping Cart System ======")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            view_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            remove_from_cart()
        elif choice == "4":
            view_cart()
        elif choice == "5":
            print("👋 Thank you for shopping!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
