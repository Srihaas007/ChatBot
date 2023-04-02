# ChatBot
This ChatBot is all about booking food in restaurant
# Define the data
locations = {
    "location1": {
        "restaurants": {
            "restaurant1": ["item1", "item2", "item3", "item4", "item5", "item6"],
            "restaurant2": ["item1", "item2", "item3", "item4", "item5", "item6"],
            "restaurant3": ["item1", "item2", "item3", "item4", "item5", "item6"],
        }
    },
    "location2": {
        "restaurants": {
            "restaurant1": ["item1", "item2", "item3", "item4", "item5", "item6"],
            "restaurant2": ["item1", "item2", "item3", "item4", "item5", "item6"],
            "restaurant3": ["item1", "item2", "item3", "item4", "item5", "item6"],
        }
    },
    "location3": {
        "restaurants": {
            "restaurant1": ["item1", "item2", "item3", "item4", "item5", "item6"],
            "restaurant2": ["item1", "item2", "item3", "item4", "item5", "item6"],
            "restaurant3": ["item1", "item2", "item3", "item4", "item5", "item6"],
        }
    },
    "location4": {
        "restaurants": {
            "restaurant1": ["item1", "item2", "item3", "item4", "item5", "item6"],
            "restaurant2": ["item1", "item2", "item3", "item4", "item5", "item6"],
            "restaurant3": ["item1", "item2", "item3", "item4", "item5", "item6"],
        }
    },
}

# Define helper functions
def display_menu(menu):
    for index, item in enumerate(menu, start=1):
        print(f"{index}. {item}")
    selection = int(input("Enter your choice: "))
    if 1 <= selection <= len(menu):
        print("This is the menu.")
        return menu[selection - 1]
    else:
        print("Invalid choice. Enter 1 to", len(menu))
        return None

def process_payment():
    print("Now let's process the payment.")

# Define the main menu loop
def main_menu():
    while True:
        print("1. Enter location manually")
        print("2. Do it automatically")
        selection = int(input("Enter your choice: "))
        if selection == 1:
            location_selection = input("Enter location (location1 - location4): ")
            if location_selection in locations:
                restaurant_selection = input("Enter restaurant name: ")
                if restaurant_selection in locations[location_selection]["restaurants"]:
                    menu = locations[location_selection]["restaurants"][restaurant_selection]
                    item_selection = display_menu(menu)
                    if item_selection is not None:
                       
