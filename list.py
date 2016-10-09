import os


filename 	= 'options.html'
setname 	= 'sets.html'
articleDir 	= './articles/'
treeDir 	= './json/'

#file list with sorted input articles
fileList 	= sorted(os.listdir(articleDir))
#set list with directory names
setList 	= [name for name in os.listdir(treeDir) if os.path.isdir(os.path.join(treeDir, name))]
setList.sort()

with open(filename,'w') as page:
	page.write('<select class="dropdown form-control">\n')
	for f in fileList:
	    page.write('\t<option value="' + f[:-4] + '">' + f[:-4].replace('_',' ') + '</option>\n')
	page.write('</select>')
	page.close()

with open(setname,'w') as page:
	page.write('<select class="set form-control">\n')
	for f in setList:
	    page.write('\t<option value="' + f + '">' + f + '</option>\n')
	page.write('</select>')
	page.close()

