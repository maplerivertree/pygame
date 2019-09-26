import numpy as np

input_list = []
# Choose modes 1) manual entry, 2) excel file intake, 3) test list

mode = input("Choose Mode: file, type, test: ")
output_type = input("Is branded terms alraedy added? (Y/N): ")
if mode == "test":
	input_list = ['ear plug', 'night light', 'glasses', 'security camera with piano glass touch pad']
if mode =="file":
	filepath = 'a.txt'
	with open(filepath) as fp:
		for line in fp:
			input_list.append(line.strip())
if mode =="type":
	r_k = str(1)
	while r_k != '':
		r_k = input("key in raw keyword. click enter with no entry when you are done. = ")
		if r_k != '':
			input_list.append(r_k)
#========================

preped_input_list = [] # add '+' to the words first
def prep(input_list):
	l = len(input_list)
	
	for index in np.arange(1, l+1, 1):
		split_words = str.split(input_list[index-1], ' ')
		l2 = len(split_words)
		for index2 in np.arange(1, l2 +1, 1):
			if split_words[index2-1] != '':
				split_words[index2-1] = '+' + split_words[index2-1]
		
		preped_input_list.append(split_words)
	return preped_input_list
input_list_with_plus = prep(input_list)

print("###################\n################### ")
if output_type == 'N':
	for i in np.arange(1, len(input_list_with_plus)+1, 1):
	    for j in np.arange(1, len(input_list_with_plus[i-1])+1, 1):
	    	print(input_list_with_plus[i-1][j-1], end="")
	    	print(" ", end="")
	    	if j == len(input_list_with_plus[i-1]):
	    		print("+alexa", end="")
	    print(" ")

	for i in np.arange(1, len(input_list_with_plus)+1, 1):
	    for j in np.arange(1, len(input_list_with_plus[i-1])+1, 1):
	    	print(input_list_with_plus[i-1][j-1], end="")
	    	print(" ", end="")
	    	if j == len(input_list_with_plus[i-1]):
	    		print("+echo", end="")
	    print(" ")
	for i in np.arange(1, len(input_list_with_plus)+1, 1):
		for j in np.arange(1, len(input_list_with_plus[i-1])+1, 1):
			print(input_list_with_plus[i-1][j-1], end="")
			print(" ", end="")
			if j == len(input_list_with_plus[i-1]):
				print("+amazon", end="")
		print(" ")
if output_type == "Y":
	for i in np.arange(1, len(input_list_with_plus)+1, 1):
	    for j in np.arange(1, len(input_list_with_plus[i-1])+1, 1):
	    	print(input_list_with_plus[i-1][j-1], end="")
	    	print(" ", end="")
	    print(" ")
print("###################\n################### ")

for i in np.arange(1, len(input_list)+1, 1):
	if output_type == 'N':
		print("[echo " + str(input_list[i-1]) + "]")
		print("[alexa " + str(input_list[i-1]) + "]")
		print("[amazon alexa " + str(input_list[i-1]) + "]")
		print("[amazon echo " + str(input_list[i-1]) + "]")
	if output_type == 'Y':
		print("[" + str(input_list[i-1]) + "]")
print("###################\n################### ")
