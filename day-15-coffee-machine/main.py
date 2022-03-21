from data import MENU, resources


def check_resources(coffee):
    for key in coffee['ingredients']:
        if resources[key] < coffee['ingredients'][key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True


machine_bank = 0

is_machine_on = True

while is_machine_on:
    order = input("What would you like? (espresso, latte, cappuccino) ")
    if order == "off":
        is_machine_on = False
    elif order != 'report':
        if check_resources(MENU[order]):
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickles = int(input("How many nickles? "))
            pennies = int(input("How many pennies? "))
            total_cash = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
            coffee_price = MENU[order]["cost"]
            if total_cash >= coffee_price:
                print(f"Here is ${round(total_cash,2)} in change.")

                for key in MENU[order]['ingredients']:
                    resources[key] -= MENU[order]['ingredients'][key]

                print(f"Here is your {order}. Enjoy!")
                machine_bank += total_cash
            else:
                print("Sorry that's not enough money. Money refunded.")
    else:
        for key in resources:
            if key != 'coffee':
                print(f"{key.title()}: {resources[key]}ml")
            else:
                print(f"{key.title()}: {resources[key]}g")
        print(f"Money: ${round(machine_bank,2)}")
