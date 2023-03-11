from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
money = MoneyMachine()
coffe = CoffeeMaker()
user_input=input(f"What would you like? ({menu.get_items()}):")
if user_input=="off":
    exit()
elif user_input=="report":
    coffe.report()
    money.report()
else:
    drink=menu.find_drink(user_input)
    print(drink.name)
    print(drink.cost)
    print(drink.ingredients) 
    if coffe.is_resource_sufficient(drink):
#        payment=money.process_coins()
        if money.make_payment(drink.cost):
            coffe.make_coffee(drink)

