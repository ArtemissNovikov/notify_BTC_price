from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'1',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  #acc key needed in order to work
  #please proceed to https://coinmarketcap.com/api/ and get your own key
  'X-CMC_PRO_API_KEY': '',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data['data'][0]['quote']['USD'])
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
