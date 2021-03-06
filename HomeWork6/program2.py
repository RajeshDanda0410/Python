import json, os
import shutil


PARENT = "quotes"

with open("quotes.json", 'r') as quotesFile:
	data = json.load(quotesFile)

if os.path.exists(PARENT):
	shutil.rmtree(PARENT)

os.mkdir(PARENT) 
os.chdir(PARENT) 
print(" Parent directory ", PARENT)

for node in data:
	correctedAuthor = node["author"] if node["author"] is not None else "Unknown"
	dirName = correctedAuthor.replace(" ", "_")
	os.mkdir(dirName) if not os.path.exists(dirName) else print("{} exists".format(dirName))
	os.chdir(dirName)
	ls=os.listdir()
	if not ls:
		out = open("quote.txt", "w")
		out.write(node["text"])
		out.write("\n\n")
		out.close()
	else:
		f="qoute_"+str(len(ls)+1)+".txt"
		out = open(f, "w")
		out.write(node["text"])
		out.write("\n\n")
		out.close()	
	
	os.chdir("..") 
