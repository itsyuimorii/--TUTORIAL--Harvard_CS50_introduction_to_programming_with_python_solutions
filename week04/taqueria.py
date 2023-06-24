shop_items = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def calculate_total_budget():
    total_budget = 0
    while True:
        try:
            user_input = input("Item: ").strip().title()
            if user_input in shop_items:
                total_budget += shop_items[user_input]
                print(f"${total_budget:.2f}")
            else:
                raise ValueError
        except ValueError:
            print("Invalid item. Please try again.")
        except EOFError:
            print("")
            break

calculate_total_budget()
