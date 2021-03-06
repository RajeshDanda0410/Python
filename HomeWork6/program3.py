import os

startpath=input("Enter Start Path")
filename=input("Enter File Name")

if os.path.exists(startpath):
	for roots,dirs,files in os.walk(startpath , topdown=True):
		
		for i in files:
			if(filename == i):
				print(os.path.join(roots,i))
				break
