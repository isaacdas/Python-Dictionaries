#Task 1


def add_category(menu, category, item, price):
    if category not in menu:
        menu[category] = ({item: price})
        print(f"{category} added to Menu")
    else:
        menu[category].update({item: price})
        print(f"{item} added to {category}")

def update_category(menu, category, item, price):
    try:
        menu[category][item] = price
        print(item, "updated to $", price)
    except KeyError:
        print(f"Category: {category} or item: {item} must not exist")

def remove_item(menu, category, item):
    try:
        del menu[category][item]
        print(item, "removed from", category)
    except KeyError:
        print(item, "was not deleted from", category) 
    
def display_menu(menu):
    for category, items in menu.items():
        print(category, "-")
        for item, price in items.items():
            print(f"    {item}: ${price}")

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

add_category(restaurant_menu, "Beverages", "Sprite", 2.99)
add_category(restaurant_menu, "Beverages", "Coke", 2.99)
update_category(restaurant_menu, "Main Course", "Steak", 17.99)
remove_item(restaurant_menu, "Starters", "Bruschetta")
display_menu(restaurant_menu)
