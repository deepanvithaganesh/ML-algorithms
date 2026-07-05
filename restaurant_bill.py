print("========= RESTAURANT MENU =========")
print("1. Pizza       - ₹250")
print("2. Burger      - ₹120")
print("3. Pasta       - ₹180")
print("4. Sandwich    - ₹100")
print("5. Cold Drink  - ₹50")

n = int(input("\nEnter the number of different items you want to order: "))

total_bill = 0

for i in range(1, n + 1):

    print("\nItem", i)

    choice = int(input("Enter item number: "))
    quantity = int(input("Enter quantity: "))

    if choice == 1:
        item = "Pizza"
        price = 250

    elif choice == 2:
        item = "Burger"
        price = 120

    elif choice == 3:
        item = "Pasta"
        price = 180

    elif choice == 4:
        item = "Sandwich"
        price = 100

    elif choice == 5:
        item = "Cold Drink"
        price = 50

    else:
        print("Invalid Item")
        continue

    item_total = price * quantity
    total_bill += item_total

    print(item, "x", quantity, "= ₹", item_total)

# Discount
discount = 0

if total_bill > 1000:
    discount = total_bill * 0.10

bill_after_discount = total_bill - discount

# GST
gst = bill_after_discount * 0.05

final_bill = bill_after_discount + gst

print("\n========== FINAL BILL ==========")
print("Subtotal      : ₹", total_bill)
print("Discount      : ₹", discount)
print("GST (5%)      : ₹", gst)
print("-------------------------------")
print("Final Amount  : ₹", final_bill)
print("Thank You! Visit Again.")