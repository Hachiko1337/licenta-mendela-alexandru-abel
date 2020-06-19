import mysql.connector
# from configparser import SafeConfigParser

# config = SafeConfigParser()
# config.read('config.ini')
# host = str(config.read('database', 'host')),
# 	user = str(config.read('database', 'user')),
# 	passwd = str(config.read('database', 'pass')),
# 	database = str(config.read('database', 'database'))

db = mysql.connector.connect(
	host = 'eu-cdbr-west-03.cleardb.net',
	user = 'ba3bdf7e840cd3',
	passwd = 'fd79e89e',
	database = 'heroku_7b09c6cb1c5af53')

mycursor = db.cursor()

mycursor.execute("SELECT * FROM opcodes;")


def get_all_opcode_names():
	result = []
	for x in mycursor:
		result.append(str(x[2]))
	return result


def get_all_gas_values():
	result = []
	for x in mycursor:
		result.append(x[4])
	return result


def get_opcode_price_pair():
	result = dict()
	for item in mycursor:
		result[item[2]] = item[4]
	return result

def get_opcode_description_pair():
	result = dict()
	for item in mycursor:
		result[item[2]] = item[3]
	return result

def get_opcode_hexcode_pair():
	result = dict()
	for item in mycursor:
		result[item[2]] = item[1]
	return result