import datetime
import json

text_json = '''{
    "Demo": "Processing JSON in Python",
    "Instrutor": "Manuh",
    "Duration": 20.0
}'''

print(type(text_json), text_json)

data = json.loads(text_json)

print(type(data),data)

#Instrutor = data['Instrutor']
Instrutor = data.get('Instrutor', 'Unknown')
print(Instrutor,"is your instructor")
#print("{}".format(Instrutor),"is your instructor")

data['Instrutor']= 'Dandy'
data['start_time'] = str(datetime.datetime.now())
new_json = json.dumps(data) #dump to string, change from type dict to string
print(type(new_json), new_json)