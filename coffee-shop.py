
# variables
total_cost = 0

menu_items = {
    "Macchiato": 5.35,
    "Espresso": 2.95,
    "Americano": 3.45,
    "3 Beignets": 4.90,
    "6 Beignets": 9.80,
    "12 Beignets": 19.60
}

print("""
    Welcome to the Coffee Shop, what would your like?
    Macchiato: $5.35
    Espresso: $2.95
    Americano: $3.45
    3 Beignets: $4.90
    6 Beignets: $9.80
    12 Beignets: $19.60
      
      """)

item1 = input("Type in the name of the item you want to order and hit Enter:")

if item1 in menu_items:
    total_cost += menu_items[item1]
    print(f"You ordered {item1}. Your total order is ${total_cost}.")

else:
    print("Invalid item, enter the name of an item in the menu...")

another_item = input("Would you like to order another item? (Yes/No): ").lower()

if another_item == "yes":
    item2 = input("Type in the name of the 2nd item you want to order and hit Enter:")
    if item2 in menu_items:
        total_cost += menu_items[item2]
        print(f"You ordered {item2}. Your total order is ${total_cost}.")

    else:
        print("Invalid item, enter the name of an item in the menu...")

print(f"Your Total order is ${total_cost}. Thanks you, come again!")





