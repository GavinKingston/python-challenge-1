import os
import platform

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
# Requirement: An order list is initialized.
order =[]

# Clear the screen for a cleaner user experience
clear_screen()

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous loop
place_order = True
while place_order:
    
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        
        # Clear the screen for a cleaner user experience
        clear_screen()

        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():

                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1

            # 2. Ask customer to input menu item number
            # Requirement: User is prompted for their menu item selection and it's saved as a variable menu_selection
            menu_selection = ""
            validItem = False
            while not menu_selection.isdigit() or not validItem:
                menu_selection = input("Type the item number you would like to order.")
                
                # 3. Check if the customer typed a number
                # Requirement: User input menu_selection is checked as a number and an error is printed if it is not.
                if not menu_selection.isdigit():
                    print("You didn't type a number.")
                
                # 4. Check if the menu selection is in the menu items
                # Requirement: An if-else statement is used to check if menu_selection is in the menu_items keys, and an error is printed if it isn't. 
                if menu_selection.isdigit() and int(menu_selection) not in menu_items.keys():
                    print(f"{menu_selection} was not a valid item option.")
                else:
                    validItem = True

            # Requirement: menu_selection is converted to an integer.
            menu_selection = int(menu_selection)
            
            # Store the item name as a variable
            # Requirement: The item name of the customer's selection is extracted from the menu_items dictionary and stored as a variable.
            menu_selection_name = menu_items[menu_selection]["Item name"]

            # Requirement: The customer is prompted for a quantity of their item selection and the value defaults to 1 if the customer does not input a valid number. 
            quantity = input(f"How many {menu_selection_name} would you like to order? ")

            # Requirement: Check if the quantity is a number, default to 1 if not
            if not quantity.isdigit():
                quantity = 1
            else:
                quantity = int(quantity)

            # Requirement: The customer's selected item, price, and quantity are appended to the order list in dictionary format. 
            order.append({
                "Item name": menu_selection_name,
                "Price": menu_items[menu_selection]["Price"],
                "Quantity": quantity
            })

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
        # Requirement: A match-case statement is used to check if the customer would like to keep ordering, and performs the correct actions for y, n, and default cases.
        # Requirement: The match-case statement converts the use input to lowercase or uppercase before checking the case.
        match keep_ordering.lower():
            # Keep ordering
            case "y" | "yes":
                clear_screen()
                break
            # Complete the order
            case "n" | "no":
                # Since the customer decided to stop ordering, thank them for
                # their order
                clear_screen()
                print("Thank you for your order.")
                place_order = False
                break 
            case _:
                # Tell the customer to try again
                print("Invalid Input - Would you like to keep ordering? please type (Y)es or (N)o")

# Clear the screen for a cleaner user experience
clear_screen()

# Print out the customer's order
print("This is what we are preparing for you.\n")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
# Requirement: A for loop is used to loop through the order list.
for item in order:
    # 7. Store the dictionary items as variables
    # Requirement: The value of each key in each order dictionary is saved as a variable.
    item_name, item_price, item_quantity = item.values()

    # 8. Calculate the number of spaces for formatted printing
    # 9. Create space strings
    # Requirement: The number of formatting spaces are correctly calculated.
    # Requirement: Space strings are created using string multiplication.
    item_spaces = (25 - len(item_name)) * " "
    price_spaces = (5 - len(str(item_price))) * " "
    quantity_spaces = (9 - len(str(item_quantity))) * " "

    # 10. Print the item name, price, and quantity
    # Requirement: The customer's order is printed with the item name, price, and quantity.
    print(f"{item_name}{item_spaces} | ${item_price}{price_spaces} | {item_quantity}{quantity_spaces}")

# 11. Calculate the cost of the order using list comprehension
# Requirement: List comprehension is used to calculate the total price of the order.
total_cost = sum([item["Price"] * item["Quantity"] for item in order])

# Requirement: The total price of the order is printed to the screen.
print("-"*46)
print(f"Total cost: ${total_cost}")
print("\n"*3)
