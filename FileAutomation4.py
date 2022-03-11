'''
Program Name : FileAutomation4.py
Input        : Path directory name and Extension
Output       : String
Description  : It is used to copy .txt files from one directory to another directory
Author       : Omkar Jadhav
Date         : 8-March-2022
'''


import os
from sys import argv
import pathlib

def Copy_Dir(d_path,f_dir,s_dir,file_ext):
	path=os.path.exists(d_path)
	if(path):
		print("Path Exists")
		

	if(os.path.exists(p_path)):
		for file in os.listdir(f_dir):
			if(file.endswith(file_ext)):
				shutil.copytree(f_dir,s_dir)

	print("Files Copied Successfully")
def main():
	print("Automation Script Started:")
	print("Application Name is:",argv[0])

	d_path=argv[1]
	f_dir=argv[2]
	s_dir=argv[3]
	file_ext=argv[4]

	if(argv[1]=='-u' or argv[1]=='-U'):
		print("Usage:",argv[0])

	Copy_Dir(d_path,f_dir,s_dir,file_ext)

if __name__=="__main__":
	main()