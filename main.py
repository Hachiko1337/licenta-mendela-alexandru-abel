#!/usr/bin/env python3

from tkinter import *
from tkinter import filedialog
import os
# import database as db
import solc_compiler as sc 
import gas_station_service as gss

def get_minimum_index(list_param):
	minimum = list_param[0]
	for i in range(0, len(list_param)):
		if list_param[i] < minimum:
			minimum = list_param[i]
	return list_param.index(minimum)

directory_path = None
list_of_file_paths = []
checkboxes = []
checkbutton_states = []
files = []
files_in_use = []
gas_estimates = []

def browse_folder():
	global list_of_file_paths
	global checkboxes
	global files

	list_of_file_paths.clear()
	for checkbox in checkboxes:
		checkbox.destroy()
	checkboxes.clear()
	files.clear()


	directory_path = filedialog.askdirectory()
	for file in os.listdir(directory_path):
		if file.endswith('.sol'):
			list_of_file_paths.append(directory_path + '/' + file)
	for file in list_of_file_paths:
		files.append(file.split('/')[-1])
	for i in range(0, len(files)):
		checkbutton_states.append(IntVar())
		checkboxes.append(Checkbutton(topFrame, text=files[i], bg='powder blue', 
			font=('arial', 9, 'bold'), bd=4, variable=checkbutton_states[i]))

	for checkbox in checkboxes:
		checkbox.pack()
	return list_of_file_paths

def adviser():
	global files
	global checkbutton_states
	global checkboxes
	global list_of_file_paths
	global files_in_use
	global gas_estimates

	for i in range(0, len(list_of_file_paths)):
		if checkbutton_states[i].get():
			files_in_use.append(list_of_file_paths[i])



	for path in files_in_use:
		gas_estimates.append(sc.get_gas_estimation(sc.get_opcodes(path)))

	output_panel.config(state=NORMAL)
	output_panel.delete('1.0', END)


	for i in range(0, len(files_in_use)):
		# output_panel.insert(INSERT, 'File ' + files_in_use[i].split('/')[-1] + ' uses ' + str(gas_estimates[i]) + ' gas.\n')
		output_panel.insert(INSERT, 'Detailed gas estimation for ' + files_in_use[i].split('/')[-1] + ':\n')
		output_panel.insert(INSERT, sc.detailed_gas_estimation(files_in_use[i]))
		output_panel.insert(INSERT, '\nA rough estimation of the gas used by file ' +  files_in_use[i].split('/')[-1] + 
			' is ' + str(gas_estimates[i]) + '. We recommend adding about two to three thousand more units to this value as to account for the possibility of underestimation.')
		output_panel.insert(INSERT, '\nThis would cost about ' + str((gss.get_from_gas_price('average') * gas_estimates[i])/10) + ' gwei.')
		output_panel.insert(INSERT, '\n\n')
	# output_panel.insert(INSERT, 'We recommend using the file ' 
	# 	+ files_in_use[get_minimum_index(gas_estimates)].split('/')[-1] 
	# 	+ ' as it uses the least gas.\n')
	# output_panel.insert(INSERT, 'The price for executing this file is ' + str((gss.get_from_gas_price('average')
	# 	 * gas_estimates[get_minimum_index(gas_estimates)])/10) + ' gwei.')


	output_panel.config(state=DISABLED)
	output_panel.pack()

def reset():
	global list_of_file_paths
	global checkboxes
	global output_panel
	global checkbutton_states
	global files_in_use
	global gas_estimates
	global files

	checkbutton_states.clear()
	list_of_file_paths.clear()
	files_in_use.clear()
	gas_estimates.clear()
	files.clear()

	for checkbox in checkboxes:
		checkbox.destroy()
	checkboxes.clear()

	output_panel.config(state=NORMAL)
	output_panel.delete('1.0', END)
	output_panel.config(state=DISABLED)


root = Tk()
root.geometry('700x950')
root.title('Gas Estimator')
root.configure(bg = 'powder blue')

topFrame = Frame(root, bg='powder blue', relief=SUNKEN)
topFrame.pack()
bottomFrame = Frame(root, bg='powder blue', relief=SUNKEN)
bottomFrame.pack(side=BOTTOM)

folderbrowse_button = Button(topFrame, text='Choose folder', fg='black', padx=4, pady=4, bd=6,
font=('arial', 10, 'bold'), command=browse_folder)
folderbrowse_button.pack(pady = 30)

advisor_button = Button(bottomFrame, text='Advise me', fg='black', padx=4, pady=4, bd=6,
font=('arial', 10, 'bold'), command=adviser)
advisor_button.pack(pady = 20)

output_panel = Text(bottomFrame, fg='black', bd=15, insertwidth=2, font=('arial', 12))
output_panel.pack()

reset_button = Button(bottomFrame, text='Reset', fg='red', padx=4, pady=4, bd=6,
font=('arial', 10, 'bold'), command=reset)
reset_button.pack(pady=20)


root.mainloop()