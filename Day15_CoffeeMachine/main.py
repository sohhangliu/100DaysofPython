"""
Coffee Machine Simulator

Simulate a coffee machine that offers various types of coffee.
Users can select their desired coffee, check resources, and make purchases.

Soh Hang Liu
2023/08/23
"""

# Menu of available coffees with their ingredients and costs
MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    }
}

# Available resources in the coffee machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def print_resources():
    """
    Print the current resources in the coffee machine.
    """
    print(f'Resources available:')
    print(f'  Water: {resources["water"]}ml')
    print(f'  Milk: {resources["milk"]}ml')
    print(f'  Coffee: {resources["coffee"]}g')
    print(f'  Money: ${resources["money"]}')


def are_resources_sufficient(ingredients):
    """
    Check if there are enough resources to make the selected coffee.

    Args:
        ingredients (dict): The required ingredients for the selected coffee.

    Returns:
        bool: True if resources are sufficient, False otherwise.
    """
    for ingredient, required_amount in ingredients.items():
        if resources[ingredient] < required_amount:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    num_quarters = int(input("How many quarters?: "))
    num_dimes = int(input("How many dimes?: "))
    num_nickles = int(input("How many nickles?: "))
    num_pennies = int(input("How many pennies?: "))
    total_sum = (0.25 * num_quarters) + (0.10 * num_dimes) + (0.05 * num_nickles) + (0.01 * num_pennies)
    return total_sum

def main():
    """
    Main function to run the coffee machine simulator.
    """
    print("Welcome to the Coffee Machine!")

    while True:
        user_prompt = input("What would you like? (espresso/latte/cappuccino) ").lower()

        if user_prompt == "off":
            print("Turning off the coffee machine.")
            break

        if user_prompt == "report":
            print_resources()

        if user_prompt in MENU:
            selected_coffee = MENU[user_prompt]
            required_ingredients = selected_coffee["ingredients"]

            if are_resources_sufficient(required_ingredients):
                input_money = process_coins()

                if input_money < selected_coffee["cost"]:
                    print("Sorry that's not enough money. Money refunded.")
                    break

                elif input_money == selected_coffee["cost"]:
                    resources["money"] += input_money
                    print(f"Here is your {user_prompt} ☕️. Enjoy!")

                elif input_money > selected_coffee["cost"]:
                    change = input_money - selected_coffee["cost"]
                    resources["money"] += (input_money - change)
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {user_prompt} ☕️. Enjoy!")

if __name__ == "__main__":
    main()
