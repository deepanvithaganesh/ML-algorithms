print("========= RESTAURANT MENU =========")
menu=("Pizza", "Burger", "Pasta", "Sandwich", "Cold Drink")
cost = {"Pizza": 250, "Burger": 120, "Pasta": 180, "Sandwich": 100, "Cold Drink": 50}
order_list=[]
order_set=set()
n = int(input("\nEnter the number of different items you want to order: "))

total_bill = 0

for i in range(1, n + 1):

    print("\nItem", i)

    choice = int(input("Enter item number: "))
    quantity = int(input("Enter quantity: "))

    if choice == 6:
        print("Exiting the order process.")
        break
    else:
        if choice < 1 or choice > 5:
            print("Invalid choice. Please select a valid item number.")
            continue


        item = menu[choice - 1]
        total = cost[item] * quantity
        print(f"{item} x {quantity} = ₹{total}")
        order_list.append((item, quantity))
        order_set.add(item)
        total_bill += total

# Discount
discount = 0

if total_bill > 1000:
    discount = total_bill * 0.10

bill_after_discount = total_bill - discount

# GST
gst = bill_after_discount * 0.05

final_bill = bill_after_discount + gst

print("\n========== FINAL BILL ==========")
print("List of items      :", order_list)
print("Orders Placed     :", order_set)
print("Total Bill       : ₹", total_bill)
print("GST (5%)      : ₹", gst)
print("Discount (10%) : ₹", discount)
print("-------------------------------")
print("Final Amount  : ₹", final_bill)
print("Thank You! Visit Again.")