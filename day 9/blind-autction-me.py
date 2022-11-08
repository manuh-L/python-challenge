from replit import clear
#HINT: You can call clear() to clear the output in the console.

import art as menu

list_of_bids = []
end = "False"
bid = {}
#max_bid =0
get_bid = 0

def add_bid(name,bid_value):
    bid = {}
    bid[name] = bid_value

def winner():
    n =""
    max_bid = 0
    for key in bid:
        get_bid = int(bid[key])
        if max_bid < get_bid:
            max_bid = get_bid
            n = key
    return print(f"Winner name {n}, bid values is ${max_bid}")


while end is not "True":
    print(menu.logo)
    print("Welcome to the secret auction program")
    name = input("What's your name?\n")
    bid_value = input("What's your bid?\n")
    bid[name] = bid_value

    add_bid(name,bid_value)
    finish = input("Are there any other bidders? Type 'yes' or 'no' \n")
    if finish == "no":
        end = "True"
    clear()


#print("Highest bid is", bid.get(n))
#print("The highest bit is ", max_bid)
#print("wins", bid[n])
#print(f"Winner name {n}, bid values is ${max_bid}")
winner()