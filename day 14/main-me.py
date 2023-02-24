import random  as r
import game_data
#from art import logo  # import logo from art.py
import art
#from art import vs

#print(game_data.data)
#print(logo)    # print logo
#print(vs)

#print(game_data.data[1]['name'])
#random_data_1 = r.choice(game_data.data)
#random_data_2 = game_data.data[r.randint(0, len(game_data.data)-1)]

#data = game_data.data

#print(random_data)

run = True

correct_count = 0

#def data_print():
#    pass
#    print(f"Compare A: {random_data_1['name']}, a {random_data_1['description']} from {random_data_1['country']}")
#    print(art.vs)
#    print(f"Compare B: {random_data_2['name']}, a {random_data_2['description']} from {random_data_2['country']}")

def print_data(person,letter):
    print(f"Compare {letter}: {person['name']}, a {person['description']} from {person['country']}")


def random_data():
    return r.choice(game_data.data)

#a=random_data()
#b=random_data()
#print(a)
#print(b)

#data_print()   

#print_data(random_data_1)

random_data_1 = random_data()
random_data_2 = random_data()

while run:
    print("Welcome to the higher lower game")
#    print(logo)
#    print_data()

    print_data(random_data_1,"A")
    print(art.vs)
    print_data(random_data_2,"B")
#    print(f"Compare A: {random_data['name']}, a {random_data['description']} from {random_data['country']}")
#    print(vs)
#    print(f"Compare B: {random_data1['name']}, a {random_data1['description']} from {random_data1['country']}")
    answer=input("Who has more followers? Type 'A' or 'B': ")
    if (answer == "A" and random_data_1['follower_count'] > random_data_2['follower_count']):
        correct_count += 1
        print(f"You are right! Current score: {correct_count}")
        random_data_1 = random_data()
        random_data_2 = random_data()    

    elif(answer == "B" and random_data_1['follower_count'] < random_data_2['follower_count']):
        correct_count += 1
        print(f"You are right! Current score: {correct_count}")
        random_data_1 = random_data()
        random_data_2 = random_data() 
    
    elif(answer == "A" and random_data_1['follower_count'] < random_data_2['follower_count']):
        print(f"Sorry, that's wrong. Final score: {correct_count}")
        run = False
    
    elif(answer == "B" and random_data_1['follower_count'] > random_data_2['follower_count']):
        print(f"Sorry, that's wrong. Final score: {correct_count}")
        run = False
    
    elif(answer == "A" or answer == "B" and random_data_1['follower_count'] == random_data_2['follower_count']):
        random_data_1 = random_data()
        random_data_2 = random_data() 
        
    else:
        print(f"Sorry, that's wrong letter")
 
#    run = False
