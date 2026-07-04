print("=== Menu ===")
print("1. Pizza - $10")
print("2. Burger - $5")
print("3. Salad - $7")
print("4. Soda - $2")
print("5. Ice Cream - $3")
item_total_cost_overall = 0
n = int(input("Enter the number of items you want to order: "))
for i in range(1, n+1):
    choice=int(input("Enter the item number you want to order: "))
    quantity=int(input("Enter the quantity: "))
    if choice==1:
        price=100
        print("You ordered", quantity, "Pizza(s) for $", price)
    elif choice==2:
        price=50
        print("You ordered", quantity, "Burger(s) for $", price)
    elif choice==3:
        price=27         
        print("You ordered", quantity, "Salad(s) for $", price)
    elif choice==4:
        price=2 
        print("You ordered", quantity, "Soda(s) for $", price)
    elif choice==5:
        price=30
        print("You ordered", quantity, "Ice Cream(s) for $", price)
    else:
        print("Invalid choice")
        price = 0

item_total_cost = price * quantity
item_total_cost_overall+= item_total_cost
if item_total_cost_overall <= 1000:
    discount = item_total_cost_overall * 0.1
    item_total_cost_overall -= discount
    print("You got a discount of $", discount)
else:
    print("No discount applied")
print("Total cost: $", item_total_cost_overall)

