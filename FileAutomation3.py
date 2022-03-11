'''
Program Name : FileAutomation3.py
Input        : Path directory names
Output       : String
Description  : It is used to copy all files from one directory to another directory
Author       : Omkar Jadhav
Date         : 8-March-2022
'''


import os
import pathlib
from sys import argv
import shutil
import datetime
import schedule
import time

def Dir_operation(p_dir,f_dir,s_dir):
	dir=os.path.exists(p_dir)
	if(dir):
		print("Path is Correct")

	time.sleep(9)

	'''
	file_list=[]

	if(os.path.exists(p_dir)):
		for file in os.listdir(f_dir):
			file_list.append(file)

	for file in file_list:
		print(file)
	'''
	shutil.copytree(f_dir,s_dir)

	print("File copied from one directory to another directory")

def main():
	starttime=datetime.datetime.now()
	print("Automation Script Started at time:",starttime)
	print("Application Name:",argv[0])

	p_dir=argv[1]
	f_dir=argv[2]
	s_dir=argv[3]

	Dir_operation(p_dir,f_dir,s_dir)

	endtime=datetime.datetime.now()
	print("Script is ended at time:",endtime)
if __name__=="__main__":
	main()