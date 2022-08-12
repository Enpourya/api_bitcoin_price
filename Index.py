import requests
def inform_me(price):
  good_price=24000
  if price<=good_price:
    print('Price is good.\nPrice is : %i$'%(price))
response = requests.get('https://apiv2.bitcoinaverage.com/indices/global/ticker/all?crypto=BTC&fiat=USD')
r=response.json()['BTCUSD']['bid']
print ('BITcoin price is : %i $' %(r))
print (inform_me(r))
