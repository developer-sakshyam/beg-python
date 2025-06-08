

# foodmenu
menu = {
    'pizza' : 140,
    'burger' : 120,
    'coffee' : 40,
    'salad' : 100,
}

# GREET

print("Welcome to our hotel")
print(" Pizza : 140\n Burger : 120\n Coffee : 40\n Salad : 100")

order_total = 0
item_1 = input("Enter your order:")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your {item_1} has been added to your list")
else:
    print(f"Please enter valid order")

another_order = input("Do you want to add another order?: (Yes/No) ")

if another_order == "Yes":
    item_2 = input(f"Enter your another order: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"your second order {item_2} has been added to your list")
    else:
         print("Please enter valid order")
print("your total amount is", order_total)