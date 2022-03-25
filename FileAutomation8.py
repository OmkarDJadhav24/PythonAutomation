import os
from sys import argv
import hashlib
import datetime

def Delete_dups(dict):
	results=list(filter(lambda x:len(x)>1,dict.values()))

	icnt=0
	for result in results:
		for subresult in result:
			icnt=icnt+1
			if(icnt>=2):
				os.remove(subresult)

	print("Duplicate files are deleted")

def Display_dups(dict,txt_f):
	data=open(txt_f,"x")
	fd=open(txt_f,"w")

	results=list(filter(lambda x:len(x)>1,dict.values()))

	for result in results:
		for subresult in result:
			fd.write(subresult)
			fd.write("\r")

	fd.close()

def find_dups(d_path,checksum=1024):
	dict={}
	path=os.path.exists(d_path)

	if(path):
		print("Path is exists")

	for file in os.listdir(d_path):
		f_path=os.path.join(d_path,file)
		fd=open(file,"rb")
		hasher=hashlib.md5()
		data=fd.read(checksum)

		while(len(data)>0):
			hasher.update(data)
			data=fd.read(checksum)

		fd.close()
		hex=hasher.hexdigest()
		if hex in dict:
			dict[hex].append(f_path)
		else:
			dict[hex]=[f_path]

	return dict

def main():
	starttime=datetime.datetime.now()
	print("Starttime:",starttime)

	print("Application Name:",argv[0])

	d_path=argv[1]
	txt_f=argv[2]

	result=find_dups(d_path)
	Display_dups(result,txt_f)

	Delete_dups(result)

	endtime=datetime.datetime.now()
	print("Endtime:",endtime)
	print("Time required for execution is:",endtime-starttime)

if __name__=="__main__":
	main()