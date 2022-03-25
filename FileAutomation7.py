from sys import argv
import os
import hashlib

def delete_dups(dict):
	results=list(filter(lambda x:len(x),dict.values()))

	icnt=0
	for result in results:
		for subresult in result:
			icnt=icnt+1
			if(icnt>=2):
				print(subresult)
				os.remove(subresult)

	print("Duplicate values are deleted")

def check_dups(dict,txt_f):
	new_list=list(filter(lambda x:len(x)>1,dict.values()))

	data=open(txt_f,"x")
	fd=open(txt_f,"w")

	for result in new_list:
		for subresult in result:
			fd.write(subresult)
			fd.write("\r")
			print(subresult)

	fd.close()

def find_dups(d_path,checksum=1024):
	dict={}
	path=os.path.exists(d_path)

	if(path):
		print("Path is exists")

	for file in os.listdir(d_path):
		fd=open(file,"rb")
		f_path=os.path.join(d_path,file)
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
	print("Application Name:",argv[0])

	d_path=argv[1]
	txt_f=argv[2]
	result=find_dups(d_path)

	check_dups(result,txt_f)

	delete_dups(result)

if __name__=="__main__":
	main()