'''
Program Name : FileAutomation2.py
Input        : Path and Extensions
Output       : String
Description  : It is used to rename files from .txt to .doc
Author       : Omkar Jadhav
Date         : 8-March-2022
'''


import os
from os import rename
from sys import argv
import pathlib
import pandas

def Search_file(d_path,first_ext,second_ext):
	directory=os.path.exists(d_path)
	if(directory):
		print("Direcory exists")

	print("\r")

	f_list=[]
	for file in os.listdir(d_path):
		f_list.append(file)

	print("\r")
	print("Files present in the Directory are:")
	print(f_list)


	for file in f_list:
		if(file.endswith(first_ext)):
			new_file=os.path.splitext(file)[0]								# split file in two parts name and .extension
			os.rename(file, new_file + '.doc')

	print("---------Files Renamed Successfully------------")
def main():
	print("---------------Automation Script Started---------------------")
	print("---------------Application Name:",argv[0],"------------------")
	d_path=argv[1]
	first_ext=argv[2]
	second_ext=argv[3]

	Search_file(d_path,first_ext,second_ext)

	print("---------------Script Ended Successfully---------------------")

if __name__=="__main__":
	main()