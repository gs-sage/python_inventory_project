def add_item(dictionary):
    name = input("What is the name of the item to add to inventory? ").lower()
    quantity = int(input("What is the quantity of the items to add to the inventory? "))
    price = int(input("Enter the price of the item : "))

    if name in dictionary:
        print("Item already exists")
    else:
        dictionary[name] ={"quantity": quantity, "price": price}
        print(f"Added {name}: Quantity: {quantity}, Price: ${price}")


def view_inventory(dictionary):
    print("What do you want to view?")
    print("1. Full inventory")
    print("2. Only quantities")
    print("3. Only Price")

    choices = int(input("Enter your choice (1/2/3) : "))

    if choices == 1:
        for key, value in dictionary.items():
            print(f"{key}: {value}")
    elif choices == 2:
        for key, value in dictionary.items():
            print(f"{key}: Quantity: {value['quantity']}")
    elif choices == 3:
        for key, value in dictionary.items():
            print(f"{key}: Price: {value['price']}")


def update_item(dictionary):
    updating_item = input("Enter the item to update: ")

    if updating_item in dictionary:
        print("What are you updating? ")
        user_choice = input("Enter quantity or price: ").lower()

        while user_choice not in ['quantity', 'price']:
            print("Invalid choice, please enter again.")
            user_choice = input("Enter quantity or price: ").lower()
        while True:
            try:
                if user_choice == 'quantity':
                    new_quantity = int(input("Enter new quantity of item: "))
                    dictionary[updating_item]['quantity'] = new_quantity
                    print(f"Quantity for item: {updating_item}, updated to {new_quantity} ")
                elif user_choice == 'price':
                    new_price = int(input("Enter new price of item: "))
                    dictionary[updating_item]['price'] = new_price
                    print(f"Price for item: {updating_item}, updated to {new_price}")
                break # break if everything works

            except ValueError:
                print("Invalid input. Please enter a valid number.")

    else:
        print(f"The item {updating_item} is not in our inventory.")


def remove_item(dictionary):
    delete_item = input("What item would you like to remove? ").lower()

    if delete_item in dictionary:
        dictionary.pop(delete_item)
        print(f"Item {delete_item} has been removed from inventory.")
    else:
        print(f"Item {delete_item} doesn't exist in inventory.")



inventory = {}

while True:
    print("****************Inventory System*******************")
    print("Here are your options:")
    print("1. Add item to inventory")
    print("2. View inventory")
    print("3. Update inventory items")
    print("4. Remove item from inventory")
    print("5. Exit inventory system")
    print("\n")

    user_input = int(input("Enter your choice : "))

    if user_input == 1:
        add_item(inventory)
        print("\n")

    elif user_input == 2:
        view_inventory(inventory)
        print("\n")

    elif user_input == 3:
        update_item(inventory)
        print("\n")

    elif user_input == 4:
        remove_item(inventory)

    elif user_input == 5:
        print("Exiting inventory, goodbye")
        break




