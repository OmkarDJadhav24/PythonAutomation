import os
from sys import argv
import pandas as pd
import hashlib


def store_file(list,txt_f):
	fdd=open(txt_f,"x")

	fd=open(txt_f,"w")

	for results in list:
		for subresult in results:
			n_file=str(subresult)
			fd.write(n_file)
			fd.write("\r")

	fd.close()

def find_dups(dict):
	results=list(filter(lambda x:len(x)>1,dict.values()))
	new_list=[]
	if len(results)>0:
		for result in results:
			new_list.append(result)
			print(result)
			
	else:
		print("No duplicate file found")

	return new_list

def find_path(d_path,blocksize=1024):
	dict={}
	path=os.path.exists(d_path)

	if(path):
		print("Path is exists")

	for file in os.listdir(d_path):
		f_path=os.path.join(d_path,file)
		#print(f_path)
		hasher=hashlib.md5()
		fd=open(file,"rb")
		buf=fd.read()
		while len(buf)>0:
			hasher.update(buf)
			buf=fd.read(blocksize)
			fd.close()
		data=hasher.hexdigest()
		if data not in dict:
			dict[data]=[f_path]

		else:
			dict[data].append(f_path)

	return dict

def main():
	print("Application Name:",argv[0])

	d_path=argv[1]

	txt_f=argv[2]

	new=find_path(d_path)

	res=find_dups(new)
	
	store_file(res,txt_f)

if __name__=="__main__":
	main()