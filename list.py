import os

fileList = enumerate(sorted(os.listdir("./articles/")))
filename = 'options.html'
page = open(filename,'w')
page.write('<select class="dropdown form-control">\n')
for key,f in fileList:
    page.write('\t<option value="' + f + '">' + f + '</option>\n')
page.write('</select>')
