from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True


def main():
    """
    Main function to run the coffee machine simulator.
    """
    print("Welcome to the Coffee Machine!")

    while is_on:
        options = menu.get_items()
        choice = input(f"What would you like? {options} ").lower()

        if choice == "off":
            print("Turning off the coffee machine.")
            is_on = False

        elif choice == "report":
            coffee_maker.report()
            money_machine.report()

        else:
            order = menu.find_drink(choice)

            if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)


if __name__ == "__main__":
    main()
