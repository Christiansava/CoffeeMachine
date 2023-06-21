def print_report(existing_money):
    """Prints the report."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${existing_money}")


def check_resources(operation):
    """Checks if there are enough resources to do the order."""
    for item in MENU[operation]["ingredients"]:
        if MENU[operation]["ingredients"][item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return 0
        else:
            return 1


def process_coins(operation):
    """Processes the inserted coins and calculates if the value inserted is enough to do the operation."""
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))

    total_money = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

    operation_price = MENU[operation]["cost"]

    if total_money < operation_price:
        return 0
    else:
        return total_money


def make_coffee(operation):
    """Makes the coffe and reduces the resources."""
    water = MENU[operation]["ingredients"]["water"]
    coffee = MENU[operation]["ingredients"]["coffee"]
    if operation == "latte" or operation == "cappuccino":
        milk = MENU[operation]["ingredients"]["milk"]
    else:
        milk = 0

    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 1) Prompt user asking what he would like to drink.
turn_off = False
money = 0
validate_resources = 0

while not turn_off:
    type_of_operation = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: 2) When typing "off" the machine should turn off.
    if type_of_operation == "off":
        turn_off = True

    # TODO: 3) When typing "report" we should gibe user the report with the quantities of the resources.
    elif type_of_operation == "report":
        print_report(money)

    # TODO: 4) After selecting the drink, check if we have sufficient resource.
    else:
        validate_resources = check_resources(type_of_operation)

        # TODO: 5) Process customer coins.
        # TODO: 6) Check if customer coins are sufficient.
        if validate_resources == 1:
            money_inserted = process_coins(type_of_operation)

            if money_inserted == 0:
                print("Sorry that's not enough money. Money refunded.")
            else:

                # TODO: 7) Make the coffe and reduce resource quantity.
                if money_inserted > 0:
                    offer_change = round(money_inserted - MENU[type_of_operation]["cost"], 2)
                    money += MENU[type_of_operation]["cost"]

                    make_coffee(type_of_operation)

                    print(f"Here is ${offer_change} in change.")
                    print(f"Here is your {type_of_operation} ☕. Enjoy!")
