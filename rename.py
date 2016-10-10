import os
articleDir 	= './articles/'

fileList 	= sorted(os.listdir(articleDir))

for file_item in fileList:
	if(file_item.find(' ') != -1):
		os.system('mv ' + articleDir + file_item.replace(' ','\ ').replace('(','\(').replace(')','\)') + ' ' + articleDir + file_item.replace(' ','_').replace('(','\(').replace(')','\)') )