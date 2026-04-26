from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def coffe_machine():
    order = CoffeeMaker()
    menu = Menu()
    machine = MoneyMachine()
    while True:
        inp = input(f"What would you like? {menu.get_items()}:").lower()
        if inp == "off":
            return
        if inp == "report":
            order.report()
            machine.report()
        elif inp in ["latte","espresso","cappuccino"]:
            item = menu.find_drink(inp)
            if order.is_resource_sufficient(item):
                if machine.make_payment(item.cost):
                   order.make_coffee(item)
                else:
                    continue
                
            else:
                continue
            
coffe_machine()
