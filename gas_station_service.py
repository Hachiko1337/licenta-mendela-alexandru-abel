import urllib.request, json, requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

req_url1 = 'https://ethgasstation.info/api/ethgasAPI.json'
req_url2 = 'https://ethgasstation.info/api/predictTable.json'


# money_text = requests.get('https://markets.businessinsider.com/currencies/eth-usd').text
# r1 = requests.get(req_url1)
# r2 = requests.get(req_url2)


''' ----Gas Price---- '''
''' Possible values for string are: fast, fastest, safeLow, average, block_time, blockNum, speed
safeLowWait, avgWait, fastWait, fastestWait '''

def get_from_gas_price(string):
	r1 = requests.get(req_url1)
	return r1.json()[string]


''' ----End Gas Price---- '''



# print (r1.json())
# print(r2.json()[0]['gasprice'])



''' ----Prediction Table---- '''
''' Possible values for string are: gasprice, hashpower_accepting, hashpower_accepting2, tx_atabove, age
pct_remaining5m, pct_mined_5m, total_seen_5m, average, safelow, nomine, avgdiff, intercept, hpa_coef
avgdiff_coef, tx_atabove_coef, int2, hpa_coef2, sum, expectedWait, unsafe, expectedTime '''

def get_from_prediction_table(string):
	r2 = requests.get(req_url2)
	return r2.json()[0][string]


''' ----End Prediction Table---- '''

# def decode(s, encoding='utf-8', erorrs='ignore'):
# 	return s.decode(encoding=encoding, errors=errors)

def get_price_in_dollars(amount):
	money_text = requests.get('https://markets.businessinsider.com/currencies/eth-usd').text
	soup = BeautifulSoup(money_text, 'html.parser')
	return amount * float(re.findall(r'\d+.\d+', str(soup.find_all('span', {'class', 'push-data'})[0]))[1])
