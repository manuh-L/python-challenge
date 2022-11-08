from replit import clear
#HINT: You can call clear() to clear the output in the console.

import art as menu

list_of_bids = []
end = "False"
bid = {}
max_bid =0

def add_bid(name,bid_value):
    bid = {}
    bid["Name"] = name
    bid["bid_value"] = bid_value
    list_of_bids.append(bid)
    

while end is not "True":
    print(menu.logo)
    print("Welcome to the secret auction program")
    name = input("What's your name?\n")
    bid_value = input("What's your bid?\n")
    bid["Name"] = name
    bid["value"] = bid_value
    list_of_bids.append(bid)
#    add_bid(name,bid_value)
    finish = input("Are there any other bidders? Type 'yes' or 'no' \n")
    if finish == "no":
        end = "True"
#    clear()
print(list_of_bids)

for key in list_of_bids:
    

