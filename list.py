import os


filename 	= 'options.html'
setname 	= 'sets.html'
articleDir 	= './articles/'
imageDir 	= './images/'

#file list with sorted input articles
fileList 	= sorted(os.listdir(articleDir), cmp = None, key=lambda x : int(x[3:-4]))
#set list with directory names
setList 	= [name for name in os.listdir(imageDir) if os.path.isdir(os.path.join(imageDir, name))]
setList.sort()

with open(filename,'w') as page:
	page.write('<select class="dropdown form-control">\n')
	for f in fileList:
	    page.write('\t<option value="' + f + '">' + f + '</option>\n')
	page.write('</select>')
	page.close()

with open(setname,'w') as page:
	page.write('<select class="set form-control">\n')
	for f in setList:
	    page.write('\t<option value="' + f + '">' + f + '</option>\n')
	page.write('</select>')
	page.close()

