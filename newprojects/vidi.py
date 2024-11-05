import requests

URL = 'https://sammy.myvidispine.com'
Endpoint = '/API/item/VX-204/shape/VX-576'
usernam = 'admin'
password = 'Heineken1!'

Headers = {'Content-Type':'application/xml'}

response = requests.get(URL+Endpoint,headers=Headers,auth=(usernam,password))

if response.status_code == 200:
    try:
        print('data invalid')
    except ValueError:
        print('this is the problem'+response.text)
else:
    print  ('failed with code',response.status_code)
    print ('content',response.text)      

