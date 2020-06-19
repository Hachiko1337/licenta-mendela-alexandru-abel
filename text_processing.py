# import database as db

# prices = db.get_opcode_price_pair()

def check_indentation(string1, string2):
	if len(string1) - len(string1.lstrip(' ')) == len(string2) - len(string2.lstrip(' ')):
		return True
	if len(string1) - len(string1.lstrip(' ')) < len(string2) - len(string2.lstrip(' ')):
		return True
	return False

def check_for_loop(list_of_strings):
	for line in list_of_strings:
		if 'for (' in line or 'while (' in line:
			return True
	return False

def capture_function_body(function_string, list_of_lines):
	code = []
	for i in range(0, len(list_of_lines)):
		if function_string in list_of_lines[i]:
			start_pos = i + 1
			i += 1
			while check_indentation(list_of_lines[start_pos], list_of_lines[i]) or list_of_lines[i] == '\n':
				code.append(list_of_lines[i])
				i +=1
	return code

def pretty_printer(list_of_strings):
	normal_string = ''
	for i in range(0, len(list_of_strings)-1):
		if 'loop' in list_of_strings[i+1]:
			list_of_strings[i].replace('infinite', 'rest_of_function + k * gas_used_in_loop')
		if 'backjump' in list_of_strings[i+1]:
			list_of_strings[i].replace('infinite', 'rest_of_function + gas_used_in_backjump')
		normal_string += list_of_strings[i]
	return normal_string



def text_formatter(gas_text, program_text, asm_text):
	copy = []
	
	list_of_infinite_functions = []

	for line in gas_text:
		if 'infinite' in line and '):' in line:
			list_of_infinite_functions.append(' '.join((line.split('(')[0].lstrip(' ').split())))

	for line in gas_text:
		copy.append(line)
		if 'infinite' in line and '+' in line and check_for_loop(capture_function_body('constructor(', program_text)):
			copy.append('\tFound loop in constructor.\n\n')
		if 'infinite' in line and '+' in line and not check_for_loop(capture_function_body('constructor(', program_text)):
			copy.append('\tFound backjump in constructor.\n\n')
		if 'infinite' in line and '):' in line and check_for_loop(capture_function_body('function ' + line.split('(')[0].lstrip(' ') + '(', program_text)):
			copy.append('\tFound loop in function.\n\n')
		if 'infinite' in line and '):' in line and not check_for_loop(capture_function_body('function ' + line.split('(')[0].lstrip(' ') + '(', program_text)):
			copy.append('\tFound backjump in function.\n\n')

	
	return pretty_printer(copy)