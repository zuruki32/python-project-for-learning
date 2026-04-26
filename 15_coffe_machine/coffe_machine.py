from menu import MENU

def drink_maker(capacity,order,drink_making):  
    new_capacity = MENU[order]["ingredients"]  
    for ing in new_capacity:
        if capacity[ing] >= new_capacity[ing]:
            capacity[ing] -=  new_capacity[ing]
            drink_making = True     
        else:
            print(f"​Sorry there is not enough {ing} ")
            drink_making = False
            return capacity,drink_making
    return capacity,drink_making

def process_coin(capacity,order,drink_making,money):
    total = []
    new_capacity = MENU[order]["ingredients"]  
    total.append(int(input("how many quarters?: "))*0.25)
    total.append(int(input("how many dimes?: "))*0.1)
    total.append(int(input("how many nickles?: "))*0.05)
    total.append(int(input("how many pennies?: "))*0.01)
    if sum(total) < MENU[order]["cost"]:
        drink_making = False
        for ing in new_capacity:
           capacity[ing] +=  new_capacity[ing]   
        print("sorry, thats not enough meney! money refunded.")
        return capacity,drink_making,money
    elif sum(total) > MENU[order]["cost"]:
        print(f"here is {sum(total)- MENU[order]["cost"]}$ change.")
        money += MENU[order]["cost"]
        return capacity,drink_making,money
    else:
        money += MENU[order]["cost"]
        return capacity,drink_making,money

def coffie_machine():
    drink_making = True
    money = 0
    capacity = {
    "water": 300, 
    "milk": 200,
    "coffee": 100
    }

    while True:
        order = input("What would you like? (espresso/latte/cappuccino):").lower()
        if order == "off":
            return
        if order =="report":
            print(f"Water:{capacity['water']}ml\nMilk:{capacity['milk']}ml\nCoffee:{capacity['coffee']}g\nMoney:{money}$")       
        if order =="latte" or order =="espresso" or order =="cappuccino":
            capacity,drink_making = drink_maker(capacity,order,drink_making)
            if drink_making == False:
                continue
            capacity,drink_making,money = process_coin(capacity,order,drink_making,money)
            if drink_making == False:
                continue
            print(f"here is your {order}, enjoy!") 
            continue
        
        
coffie_machine()