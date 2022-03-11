'''
Program Name : FileAutomation1.py
Input        : Path and Extension
Output       : String
Description  : It is used to Display all text files in perticular directory
Author       : Omkar Jadhav
Date         : 8-March-2022
'''


from sys import argv
import os
import pathlib
import glob

def Display(d_path,ext_input):
	path=os.path.exists(d_path)

	if(path):
		print("The Direcoty is exist")

	
	files=os.listdir(d_path)
	
	new_file=tuple(files)
	print(new_file)
	
	for file in new_file:
		if(file.endswith(".txt")):
			print(file)

def main():
	print("---------------------Automation Script Started-------------------")
	print("Application Name:",argv[0])
	d_path=argv[1]
	ext_input=[2]

	Display(d_path,ext_input)


if __name__=="__main__":
	main()