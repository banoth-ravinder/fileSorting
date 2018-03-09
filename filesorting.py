import os
import re
import fnmatch

path=raw_input()
files= os.listdir(path)

for file in files:
	fileName, fileExtenstion = os.path.splitext(file)
	fileExtenstion=fileExtenstion[1:]
	if len(fileExtenstion)>0 :
		print("step1")
		for search in files:
			print(search)
			if fnmatch.fnmatch(search,fileExtenstion) :
				print(search)
				print("step2")
		# tempPath= path+"/"+fileExtenstion
		# print(tempPath)
	# if not os.path.isdir(tempPath)
	# 	os.makedirs(tempPath)
	# 	os.chdir(tempPath)

	

	# print(fileName)
	# print(fileExtenstion)

# print(files)


