import pickle, os, sys, json

class Tree(object):
    "Generic tree node."
    def __init__(self, name='root', children=None):
        self.name = name
        self.parent = None
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        node.parent = self.name
        self.children.append(node)

def convert_json(obj, parent=None):
    assert isinstance(obj, Tree)
    if parent == None:
        d = [
                { 
                    "name" : obj.name, 
                    "children" : [convert_json(child, parent=obj.name) for child in obj.children] 
                }
            ]
        return json.dumps(d)
    else:
        d = { 
                "name" : obj.name,
                "parent" : parent,
                "children" : [convert_json(child, parent=obj.name) for child in obj.children] 
            }
        return d

"Attachments area"


treeDir = './tree/'
jsonDir = './json/'

#set list with directory names
setList     = [name for name in os.listdir(treeDir) if os.path.isdir(os.path.join(treeDir, name))]
#file list with sorted input articles

for set_item in setList:
    fileList    = sorted(os.listdir(treeDir + set_item))
    for file_item in fileList:
        with open(treeDir + set_item + '/' + file_item,'rb') as f:
            #print f.read()
            json_item = pickle.load(f)
            with open(jsonDir + set_item + '/' + file_item[:-8] + 'json','w+') as jsonFile:
                jsonFile.write(convert_json(json_item))




#test code
"""
a = Tree()
b = Tree('1')
a.add_child(b)
with open('make.txt','wb') as f:
    pickle.dump(a,f)

with open('make.txt','rb') as f:
    x = pickle.load(f)
    print x
"""