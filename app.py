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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False




def make_coffee(drink_name,ingredients):
    for ingredient in ingredients:
        resources[ingredient] = resources[ingredient] - ingredients[ingredient]
    print( f"Here is your drink {drink_name} coffee!")

def is_any_resource(ingredients):
    for ingredient in resources:
        if resources[ingredient] < ingredients[ingredient]:
            print(f'Sorry there is no enough {ingredient}')
            return False

        return True

is_on = True
while is_on:
    user_demand= input('What would you like?(espresso/latte/cappuccino): ').lower()

    if user_demand == 'off':
        is_on = False
    elif user_demand == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_demand]
        if is_any_resource(drink['ingredients']):
            payment = process_coins()
            if transaction_successful(payment, drink['cost']):
                make_coffee(user_demand,drink["ingredients"])






