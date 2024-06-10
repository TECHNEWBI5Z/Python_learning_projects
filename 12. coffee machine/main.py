# Menu dictionary containing details of each drink, including ingredients and cost
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

# Initial profit set to 0
profit = 0

# Resources dictionary representing the available ingredients
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """
    Check if the machine has enough resources to make the ordered drink.
    Returns True if resources are sufficient, otherwise returns False.
    """
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    """
    Prompt the user to insert coins and calculate the total amount.
    Returns the total amount of money inserted by the user.
    """
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """
    Check if the money received is sufficient to buy the drink.
    Returns True if payment is accepted, otherwise returns False.
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """
    Deduct the required ingredients from the resources and make the coffee.
    Prints a message when the coffee is ready.
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

# Variable to control the machine's operation
is_on = True

# Main loop to run the coffee machine
while is_on:
    # Prompt the user for their choice of drink
    choice = input("​What would you like? (espresso/latte/cappuccino/report):​ ").lower()
    
    if choice == "off":
        # Turn off the coffee machine
        is_on = False
    elif choice == "report":
        # Print a report of the current resources and profit
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        # Prepare the selected drink if resources are sufficient
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
