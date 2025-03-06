def add_item(dictionary):
    name = input("What is the name of the item to add to inventory? ")
    quantity = int(input("What is the quantity of the items to add to the inventory? "))
    price = int(input("Enter the price of the item : "))

    if name in dictionary:
        print("Item already exists")
    else:
        dictionary[name] ={"quantity": quantity, "price": price}
        print(f"Added {name}: Quantity: {quantity}, Price: ${price}")


def view_inventory(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")

inventory = {}

while True:
    user_input = int(input("Enter your choice : "))

    if user_input == 1:
        add_item(inventory)

    elif user_input == 2:
        view_inventory(inventory)




