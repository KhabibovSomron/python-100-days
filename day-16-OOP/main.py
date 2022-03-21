from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_machine_on = True

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_machine_on:
    order = input(f"What would you like? ({menu.get_items()}): ")
    if order == "off":
        is_machine_on = False
    elif order != "report":
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    else:
        coffee_maker.report()
        money_machine.report()
