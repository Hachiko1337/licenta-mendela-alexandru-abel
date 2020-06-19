import urllib.request, json, requests


req_url1 = 'https://ethgasstation.info/api/ethgasAPI.json'
req_url2 = 'https://ethgasstation.info/api/predictTable.json'


r1 = requests.get(req_url1)
r2 = requests.get(req_url2)


''' ----Gas Price---- '''
''' Possible values for string are: fast, fastest, safeLow, average, block_time, blockNum, speed
safeLowWait, avgWait, fastWait, fastestWait '''

def get_from_gas_price(string):
	return r1.json()[string]


''' ----End Gas Price---- '''



# print (r1.json())
# print(r2.json()[0]['gasprice'])



''' ----Prediction Table---- '''
''' Possible values for string are: gasprice, hashpower_accepting, hashpower_accepting2, tx_atabove, age
pct_remaining5m, pct_mined_5m, total_seen_5m, average, safelow, nomine, avgdiff, intercept, hpa_coef
avgdiff_coef, tx_atabove_coef, int2, hpa_coef2, sum, expectedWait, unsafe, expectedTime '''

def get_from_prediction_table(string):
	return r2.json()[0][string]


''' ----End Prediction Table---- '''