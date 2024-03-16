# Menu for the machine
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
money = 0
# resources in the machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "earnings": money
}
# report function
def report():
        print(f'Water: {resources["water"]} \n Milk: {resources["milk"]} \nCoffee: {resources["coffee"]} \n Money: ${money}')
#turning off function
def off():
    print("Turning off!")

# starting machine 
print("☕Welcome to the Coffee Machine☕\n\n ")

machine_status = True
more_coffee = True

while machine_status:
    while more_coffee:
        coffee = input("What would you like (espresso/latte/cappuccino): \n")
        if coffee == 'off':
            off()
            break
        elif coffee == 'espresso':
            if (MENU["espresso"]["ingredients"]["water"]) > (resources["water"]):
                print("Sorry there is not enough water.")
            elif (MENU["espresso"]["ingredients"]["coffee"]) > (resources["coffee"]):
                print("Sorry there is not enough coffee")
            else:
                print("insert coins.")
                quarter = input("quarter: $")
                if quarter == 'off':
                    off()
                    break
                elif quarter == 'report':
                    report()
                dimes = input("dimes: $")
                if dimes == 'off':
                    off()
                    break
                elif dimes == 'report':
                    report()
                nickles = input("nickles: $")
                if nickles == 'off':
                    off()
                    break
                elif nickles == 'report':
                    report()
                pennies = input("pennies: $")
                if pennies == 'off':
                    off()
                    break
                elif pennies == 'report':
                    report()
                money = 0.25*quarter + 0.10*dimes + 0.05*nickles + 0.01*pennies
                if MENU["espresso"]["cost"] < MENU["espresso"]["cost"]:
                    print("Sorry that's not enough money. Money refunded.")
                elif  MENU["espresso"]["cost"] >= MENU["espresso"]["cost"]:
                    if  MENU["espresso"]["cost"] > MENU["espresso"]["cost"]:
                        change = round(money - MENU["espresso"]["cost"], 2)
                        print(f"Here is ${change} dollars in change.")
                    money += MENU["espresso"]["cost"]
        #             Make Coffee
                    resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                    resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]

                    print(f"Here is your {coffee}. Enjoy!")
        elif coffee == 'latte':
            if (MENU["latte"]["ingredients"]["water"]) > (resources["water"]):
                print("Sorry there is not enough water.")
            elif (MENU["latte"]["ingredients"]["coffee"]) > (resources["coffee"]):
                print("Sorry there is not enough coffee")
            elif (MENU["latte"]["ingredients"]["milk"]) > (resources["milk"]):
                print("Sorry there is not enough milk")

            else:
                print("insert coins.")
                quarter = input("quarter: $")
                if quarter == 'off':
                    off()
                    break
                elif quarter == 'report':
                    report()
                dimes = input("dimes: $")
                if dimes == 'off':
                    off()
                    break
                elif dimes == 'report':
                    report()
                nickles = input("nickles: $")
                if nickles == 'off':
                    off()
                    break
                elif nickles == 'report':
                    report()
                pennies = input("pennies: $")
                if pennies == 'off':
                    off()
                    break
                elif pennies == 'report':
                    report()
                money = 0.25*quarter + 0.10*dimes + 0.05*nickles + 0.01*pennies
                if MENU["latte"]["cost"] < MENU["latte"]["cost"]:
                    print("Sorry that's not enough money. Money refunded.")
                elif  MENU["latte"]["cost"] >= MENU["latte"]["cost"]:
                    if  MENU["latte"]["cost"] > MENU["latte"]["cost"]:
                        change = round(money - MENU["latte"]["cost"], 2)
                        print(f"Here is ${change} dollars in change.")
                    money += MENU["latte"]["cost"]
        #             Make Coffee
                    resources["water"] -= MENU["latte"]["ingredients"]["water"]
                    resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                    resources["milk"] -= MENU["latte"]["ingredients"]["milk"]

                    print(f"Here is your {coffee}. Enjoy!")
        elif coffee == 'cappuccino':
            if (MENU["cappuccino"]["ingredients"]["water"]) > (resources["water"]):
                print("Sorry there is not enough water.")
            elif (MENU["cappuccino"]["ingredients"]["coffee"]) > (resources["coffee"]):
                print("Sorry there is not enough coffee")
            elif (MENU["cappuccino"]["ingredients"]["milk"]) > (resources["milk"]):
                print("Sorry there is not enough milk")

            else:
                print("insert coins.")
                quarter = input("quarter: $")
                if quarter == 'off':
                    off()
                    break
                elif quarter == 'report':
                    report()
                dimes = input("dimes: $")
                if dimes == 'off':
                    off()
                    break
                elif dimes == 'report':
                    report()
                nickles = input("nickles: $")
                if nickles == 'off':
                    off()
                    break
                elif nickles == 'report':
                    report()
                pennies = input("pennies: $")
                if pennies == 'off':
                    off()
                    break
                elif pennies == 'report':
                    report()
                money = 0.25*quarter + 0.10*dimes + 0.05*nickles + 0.01*pennies
                if MENU["cappuccino"]["cost"] < MENU["cappuccino"]["cost"]:
                    print("Sorry that's not enough money. Money refunded.")
                elif  MENU["cappuccino"]["cost"] >= MENU["cappuccino"]["cost"]:
                    if  MENU["cappuccino"]["cost"] > MENU["cappuccino"]["cost"]:
                        change = round(money - MENU["cappuccino"]["cost"], 2)
                        print(f"Here is ${change} dollars in change.")
                    money += MENU["cappuccino"]["cost"]
        #             Make Coffee
                    resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                    resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                    resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]

                    print(f"Here is your {coffee}. Enjoy!")



        elif coffee == 'report':
            report()
        elif quarter == 'off' or dimes == 'off' or nickles == 'off' or 'pennies' == off:
            break
    if coffee == 'off' or quarter == 'off' or dimes == 'off' or nickles == 'off' or 'pennies' == off:
        break
    else:
        cont = input("Would you like anything else: ")
        if cont == 'off':
            off()
            break
        elif cont == 'yes' or cont == 'Yes':
            more_coffee = True
        elif cont == 'report':
            report()
        elif nickles == 'off':
            break
        else:
            print("Thankyou for ordering. Have a nice day!")
            more_coffee = False
