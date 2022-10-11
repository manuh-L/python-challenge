import random
import my_module

random_integer = random.randint(1,1000)
print(random_integer)

print(my_module.pi)

random_float = random.random()
print(random_float)

random_f = random_float * 5
print(random_f) 

# list https://docs.python.org/3/tutorial/datastructures.html

states_usa = ["NY","LA","LV","MI"]
              
print(states_usa[-4])
print(states_usa)

#append end
states_usa.append("ATL")
print(states_usa)

#extend list
states_usa.extend(["PHY","DAL"])
print(states_usa)

#nested list
prov_centro = ["TETE", "Manica","Sofala","Zambezia"]
prov_sul =["Inhambane","Gaza","Maputo"]
prov = [prov_centro,prov_sul]
print(prov)