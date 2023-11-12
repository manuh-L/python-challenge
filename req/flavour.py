import requests
import json
import collections


#url
#consumer_services_api.talkpython.fm
#https://consumer_services_api.talkpython.fm/


url = 'https://consumer_services_api.talkpython.fm/api/flavours'

Flavour = collections.namedtuple("flavour", 'id name')
#Topping = collections.namedtuple("topping", 'id name')

rep= requests.get(url, verify=False)
#trans = rep.text
#print(trans)
data = json.loads(rep.text)
#print(type(data), data)

#c = int(0)
#get the list of flavours
#flavour = data.get('flavour')
#for f in flavour:
#    if f == 'chocolate':
#        print(c,f)
#    c=+1

class Increment:
    def __init__(self):
        self.counter = 0

    def next(self):
        self.counter += 1
        return self.counter - 1


def get_flavour():
    rep= requests.get(url, verify=False)
    trans = rep.text
    data = json.loads(rep.text)
    flavour = data.get('flavour')
    i = Increment()
#    print(type(data),trans)
#    print(flavour)
    return [
       Flavour(i.next(),f)
       for f in flavour
        
    ]



def get_all():
    rep= requests.get(url, verify=False)
    trans = rep.text
    data = json.loads(rep.text)
#    flavour = data.get('flavour')
#    topping = data.get('topping')
#    frosting = data.get('frosting')
#    i = Increment()
#    print(type(data),trans)
#    print(frosting)
#    print(topping)
#    print(data)
#    repo_data = resp.json()
#    clone = data.get('topping', 'ERROR: NO DATA')
    
    print(json.dumps(data,indent=True))

def get_flavours():
    resp = requests.get(url,verify=False)
    dat = json.loads(resp.text)
    if resp.status_code != 200:
        print("Error: {} {}".format(resp.status_code,resp.text))
#    print(resp.json())

    return [
#        fmt(flavour=data.get('flavour'))
#        for f in resp.json()
        #,topping=data.get('topping'),frosting=data.get('frosting'))
#        fmt(flavour= , topping=resp.json().get('topping'), frosting=resp.json().get('frosting'))
        #for f in             
    ]

def add_flavour():
#    f = input("insert the new flavour: \n")
    existing_data = {
    "flavour": ["red velvet", "chocolate", "vanilla", "carrot", "rainbow"],
    "topping": ["sprinkles", "bacon", "Happy Birthday", "sugar carrots"],
    "frosting": ["cream cheese", "chocolate", "vanilla", "maple"]
    }

    new_data = {
    "flavour": "banana",
    "topping": "nuts",
    "frosting": "strawberry"
    }

    for key, value in new_data.items():
        existing_data[key].append(value)

    new_f = { "flavour": ["Banana"] } 
              #dict(flavour=f)
    flavour_json = json.dumps(new_f)
    json_data = json.dumps(existing_data)

    headers = {"Content-Type": "application/json",
                "Accept": "application/json"
    }

    r = requests.post(url,data=json_data, headers=headers,verify=False)

    if r.status_code != 201:
        print("Error adding a new flavour: {} {}".format(r.status_code, r.text))
        print(r.json())
        return 

    print("New Flavour added: ")
    print(r.json())




if __name__== '__main__':

#    print(get_flavour())
    print(get_all())
    add_flavour()

#print(type(flavour),flavour)


#    for key, value in new_f.items():
#        existing_data[key].append(value)