# Name: Hussein Alsaidi
# Date: 4/30/23
# Description: Final Exam: McDonald's Program

## User defined Functions
def displayInventory(inventory):
    print()
    print("{:<25} {}".format("Product", "Price"))
    print("{:<25} {}".format("-" * 25, "-" * 15))
    for item, price in inventory:
        print("{:<25} ${:.2f}".format(item, price))
    input("\nPress [Enter] to return to Main Menu")
## Choice 2
def lookup_menu(inventory):
    item = input("Enter the name of the item you want to look up: ")
    for name, price in inventory:
        if name == item:
            print("Item Found: {} Price: ${:.2f}".format(name, price))
            return
    print("\033[1;31m" + "Item not found" + "\033[0m")
    input("\nPress [Enter] to return to Main Menu")

##Choice 3
def add_item(inventory):
    while True:
        add = input("Please enter menu item name to add: ")
        try:
            price = float(input("Add Item price: "))
            if price < 0.1:
                print("\033[1;31m" + "Price must be 0 or greater"+ "\033[0m")
            else:
                inventory.append([add, price])
                print("Item added successfully")
                break
        except ValueError:
            print("\033[1;31m" + "Invalid input. Please enter a price of 0 or greater" + "\033[0m")



#### EXTRA CREDIT ######



### Choice 4
def purchase_items(inventory, order):
    item = input("Enter the name of the item you want to purchase: ")
    quantity = input("Enter the quantity you want to purchase: ")
    ### if item exists in inventory
    item_found = False
    for item_name, price in inventory:
        if item_name == item:
            item_found = True
            try:
                quantity = int(quantity)
                if quantity < 1:
                    print("\033[1;31m" + "Invalid quantity. Please enter a positive integer." + "\033[0m")
                    break
                else:
                    order.append((item, price, quantity))
                    print("Added {} {}(s) to your cart.".format(quantity, item))
                    break
            except ValueError:
                print("\033[1;31m" + "Invalid quantity. Please enter a valid quantity." + "\033[0m")
                break
    ### If item is not found
    if not item_found:
        print("\033[1;31m" + "Menu item not found. Please try again." + "\033[0m")
    return

### choice 5
def view_cart(order):
    if not order:
        print("Your cart is empty.")
        return
    print("{:<20}{:<10}{:<10}".format("Item", "Quantity", "Price"))
    total = 0
    for item_name, quantity, price in order:
        item_total = quantity * price
        print("{:<20}{:<10}{:<10.2f}".format(item_name, quantity, item_total))
        total += item_total
    print("{:<20}{:<10}{:<10.2f}".format("Total", "", total))


### choice 6
def empty_cart(order):
    confirm = input("Are you sure you want to empty your cart (Y or N)? ")
    if confirm.lower() == "y":
        order.clear()
        print("Cart Emptied.")
    else:
        print("Cart not emptied.")


# Main
inventory = [["Big Mac", 3.99], ["Cheeseburger", 2.00], ["Small French Fries", 1.39]]
menuChoice = 0
order = []

## menu loop
while menuChoice != 4:
    # Display menu options
    print("  McDonald's Menu")
    print("1. Display Menu Items")
    print("2. Look-Up Menu Item")
    print("3. Add Menu Item")
    print("4. Purchase Item")
    print("5. View Cart")
    print("6. Empty Cart")
    print("7. Exit")
    # Get user choice
    try:
        menuChoice = int(input("Enter menu choice: "))
    except ValueError:
        print("\033[1;31m" + "Invalid Choice. Please choose options(1-4):" + "\033[0m")
        continue

    # Perform action based on user choice
    if menuChoice == 1:
        displayInventory(inventory)
    elif menuChoice == 2:
        lookup_menu(inventory)
    elif menuChoice == 3:
        add_item(inventory)
    elif menuChoice == 4:
        purchase_items(inventory, order)
    elif menuChoice == 5:
        view_cart(order)
    elif menuChoice == 6:
        empty_cart(order)
    elif menuChoice == 7:
        print("Goodbye!")
        break
    else:
        print("\033[1;31m" + "Invalid Choice. Please choose options(1-4):" + "\033[0m")




