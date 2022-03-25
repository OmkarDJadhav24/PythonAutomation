import os
from sys import argv
import pandas as pd
import hashlib


def Find_check(d_path,checksum=1024):
	list=[]
	for file in os.listdir(d_path):
		fd=open(file,"r")
		data=fd.read()
		hasher=hashlib.md5()
		list.append(hasher)
		fd.close()

	return list
		
def Check_sum(d_path):
	data=os.path.exists(d_path)

	if(data):
		print("Path is exists")

	new_list=Find_check(d_path)
	print(new_list)

def main():
	print("Application Name:",argv[0])

	d_path=argv[1]
	Check_sum(d_path)

if __name__=="__main__":
	main()