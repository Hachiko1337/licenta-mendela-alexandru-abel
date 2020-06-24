import subprocess, json
import database as db
import re
import text_processing as tp

prices = db.get_opcode_price_pair()

def get_opcodes(path):
	result = subprocess.run('solc --combined-json opcodes "' + path + '"', capture_output=True)
	json_text = result.stdout.decode()
	data = json.loads(json_text)

	opcodes = []
	contract_keys = data['contracts'].keys()
	list_of_contract_opcodes = []
	for key in contract_keys:
		list_of_opcodes = []
		opcodes_string = data['contracts'][key]['opcodes']
		list_of_opcodes = opcodes_string.split(' ')
		list_of_contract_opcodes.append(list_of_opcodes)
	for sublist in list_of_contract_opcodes:
		for item in sublist:
			opcodes.append(item)
	return opcodes


def solc_get_asm(path):
	result = subprocess.run('solc --asm "' + path + '"', capture_output=True)
	complicated_text = []
	text = result.stdout.decode()
	# print(text)
	lines_of_text = text.split('\n')
	for i in range (3, len(lines_of_text)):
		# if ('construction:' in line) or ('external:' in line):
		# 	complicated_text.append(line)
		# if check_for_function(line) or check_for_numbers(line):
		# 	complicated_text.append(line)
		complicated_text.append(lines_of_text[i])
	return complicated_text

def get_gas_estimation(opcodes_list):

	sum = 0

	for x in opcodes_list:
		if x in prices.keys():
			# if '0x' in x:
			# 	sum = sum + int(x, 16)
			# else:
			sum = sum + prices[x]
	return sum



def check_for_function(string_to_check):
	# \w+\((\w+\,*)*\)
	function_string = re.compile(r'\w+\(')
	if re.search(function_string, string_to_check):
		return True
	return False

def check_for_numbers(string_to_check):
	numbers_string = re.compile(r'(\d+|\w+) \+ (\d+|\w+) \= (\d+|\w+)')
	if re.search(numbers_string, string_to_check):
		return True
	return False

def solc_get_gas(path):
	result = subprocess.run('solc --gas "' + path + '"', capture_output=True)
	complicated_text = []
	text = result.stdout.decode()
	lines_of_text = text.split('\n')
	for i in range (3, len(lines_of_text)):
		# if ('construction:' in line) or ('external:' in line):
		# 	complicated_text.append(line)
		# if check_for_function(line) or check_for_numbers(line):
		# 	complicated_text.append(line)
		complicated_text.append(lines_of_text[i])
	return complicated_text

# print(solc_get_gas('E:/University Stuff/Licenta/Test Folder/ballot.sol'))

# regex: function \w+\((\w+\s\w+\,*\s*)*\) public

def detailed_gas_estimation(path):
	gas_text = solc_get_gas(path)
	with open(path, 'r') as file:
		lines = file.readlines()
		program_text = lines
	asm_text = solc_get_asm(path)

	
	# print (gas_text)
	return tp.text_formatter(gas_text, program_text, asm_text).replace('\r', '\n')

# print(detailed_gas_estimation('E:/University Stuff/Licenta/Test Folder/example.sol'))