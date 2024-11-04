import requests

URL = 'https://rickandmortyapi.com/api/character/'
parameter = ''

response = requests.get(URL)
print(response)
mydata = response.json()
Totapage = mydata['info']['pages']
print(Totapage)

Names = mydata['results'][1]['name']
print(Names)

for dictionary in mydata['results']:
    print(dictionary['name'])
