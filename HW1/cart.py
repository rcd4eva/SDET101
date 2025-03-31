# Dictory of items and their prices
inventory = {
   1: ("apple", 0.99),
   2: ("banana", 0.50),
   3: ("bread", 2.50),
   4: ("milk", 1.50),
   5: ("eggs", 3.00)
}

# shopping cart as dictonary
cart = {}

print(inventory[1][0])

def display_inventory():
    print("\n---- Inventory Items ----")
    print("ID: Item - Price")
    for key, value in inventory.items():
        print(f"{key}: {value[0]} - ${value[1]}")

def display_cart():
    print("\n---- Cart Items ----")
    print("ID:  Item  -  Price  - Quantity - Item Total")
    total = 0
    for key, value in cart.items():
        print(f"{key:>2}: {inventory[key][0]:^6} -  ${inventory[key][1]}   - {value:^8} - ${inventory[key][1] * value}")



while True:
    print("");
    print("---- Shopping Menu ----\n")
    print("0: Show intems in inventory")
    print("1: Add item to cart")
    print("2: Remove item from cart")
    print("3: View cart")
    print("4: View total cost")
    print("5: Exit")
    choice = input("\nPlease Select your choice: ")

    match choice:
        case "0":
            display_inventory()
        case "1":
            display_inventory()
            item = int(input("Enter item ID to add to cart: "))
            if item in inventory:
                print(f"You selected {inventory[item][0]} at ${inventory[item][1]}")
                qty = int(input("Please enter the quantity: "))
                if item in cart:
                    cart[item] += qty
                else:
                    cart[item] = qty
                print(f"{qty} {inventory[item][0]} added to cart for ${inventory[item][1] * qty}")
            else:
                print("Item not in inventory")
        case "2":
            display_cart()
            item = int(input("Enter item ID to remove from cart: "))
            if item in inventory:
                if item in cart:
                    qty = int(input(f"Please enter the quantity to remove (max {cart[item]}): "))
                    if qty > cart[item]:
                        print("Invalid quantity, please try again")
                    else:
                        cart[item] -= qty
                        if cart[item] == 0:
                            del cart[item]
                            print(f"{inventory[item][0]} removed from cart")
                else:
                    print("Item not in cart")
            else:
                print("Item not in inventory")
        case "3":
            display_cart()
        case "4":
            total = 0
            for key, value in cart.items():
                total += inventory[key][1] * value
            print(f"\nFinal cost: ${total}")
        case "5":
            break
        case _:
            print("Invalid choice")

print("Thank you for shopping with us!")
    

    
