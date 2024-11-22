import requests

head = {
   'Accept' : 'application/json' 
}
response  = requests.get('https://vod-demo.myvidispine.com/API/item/VX-37/metadata?field=vod_title',auth=('VSIDE7W3FSTGI57D3N5G','ysJ/jvfeVWrJQQok+gVFJcL6na9DyP96QlN8BSvD'),headers=head)

mydata = response.json()
print(mydata)

VOD_TITLE = mydata['item'][0]['metadata']['timespan'][0]['group'][0]['field'][0]['value'][0]['value']
print(VOD_TITLE)
