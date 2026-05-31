# Product Categories (Tuple)
categories = ("Electronics", "Books", "Clothing")

# Product Database (Dictionary)
products = {
    1: {"name": "Laptop", "price": 50000},
    2: {"name": "Mobile", "price": 20000},
    3: {"name": "Python Book", "price": 500},
    4: {"name": "T-Shirt", "price": 800}
}

# Shopping Cart (List)
cart = []

# Discounts (Dictionary)
discounts = {
    "SALE10": {"type": "percent", "value": 10, "min_total": 0},
    "FLAT500": {"type": "flat", "value": 500, "min_total": 5000}
}

def format_price(amount):
    return int(amount) if amount == int(amount) else f"{amount:.2f}"

while True:

    print("\n===== E-Commerce System =====")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("\nAvailable Products")

        for pid, product in products.items():
            print(
                pid,
                product["name"],
                "- ₹",
                product["price"]
            )

    elif choice == "2":

        product_id = int(input("Enter Product ID: "))

        if product_id in products:

            cart.append(products[product_id])

            print(
                products[product_id]["name"],
                "added to cart"
            )

        else:
            print("Invalid Product ID")

    elif choice == "3":

        if len(cart) == 0:
            print("Cart is empty")

        else:

            print("\nItems in Cart:")

            for item in cart:
                print(
                    item["name"],
                    "- ₹",
                    item["price"]
                )

    elif choice == "4":

        if len(cart) == 0:
            print("Cart is empty")

        else:

            total = 0

            print("\nBill Summary")

            for item in cart:

                print(
                    item["name"],
                    "- ₹",
                    item["price"]
                )

                total += item["price"]

            print("-------------------")
            print("Total Amount: ₹", total)

            coupon = input("Enter discount code (or press Enter to skip): ").strip().upper()
            discount = 0
            discount_description = "No discount applied"

            if coupon in discounts:
                offer = discounts[coupon]
                if total >= offer["min_total"]:
                    discount = total * offer["value"] / 100 if offer["type"] == "percent" else offer["value"]
                    discount_description = f"{offer['value']}% off" if offer["type"] == "percent" else f"₹{offer['value']} off"
                else:
                    print(f"Coupon '{coupon}' requires a minimum purchase of ₹{offer['min_total']}.")
            elif coupon:
                print("Invalid discount code.")

            payable = max(total - discount, 0)
            print("Discount:", discount_description)
            if discount > 0:
                print("Discount Amount: ₹", format_price(discount))
            print("Amount Payable: ₹", format_price(payable))


    elif choice == "5":
        print("Thank You For Shopping!")
        break

    else:
        print("Invalid Choice")