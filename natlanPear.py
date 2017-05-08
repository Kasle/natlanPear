##Aleksander Mercik (Kasle)
##May 08, 2017
##natlanPEAR

import os
import numpy as np


exit_flag = False


print ('initializing natlanPear.')

while not exit_flag:

	request_type = input('init setup (l, r, e): ')

	if (request_type == 'l'):
		print('initializing learning mode.')
	elif (request_type == 'r'):
		print('initializing response mode.')
	elif(request_type == 'e'):
		exit_flag = True
	else:
		print('invalid setup type.')
		continue
		
	if not exit_flag:
		break
		
if exit_flag:
	exit(0)
	
if (request_type == 'l'):
	#learning mode
	print('l')
	
elif(request_type == 'r'):
	#response mode
	print('r')
	
input()