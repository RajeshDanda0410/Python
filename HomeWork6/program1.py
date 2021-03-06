import sys
import os

apath=sys.argv[1]

split=list(os.path.split(apath))

if(os.path.exists(split[0])):
	os.chdir(split[0])
	curnt_folder=os.getcwd()
	ls=os.listdir()
	if split[1] in ls:
		print("True")
		
		while(1):
			ls=os.listdir()
			if split[1] not in ls:
				print("Alert")
				break
		
	else:
		print("False")
else:
	print("Path doesnt exist") 


