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

    elif choice == "5":

        print("Thank You For Shopping!")
        break

    else:
        print("Invalid Choice")