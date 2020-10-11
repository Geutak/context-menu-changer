import sys 
  
import os
 
filename = sys.argv[2]
action = sys.argv[1]

a = list(filename)
index = filename.find(".")
a.insert(index," [{}]".format(action))
newfilename=""
for element in a:
    newfilename+=element
os.rename(r'{0}'.format(filename),r'{0}'.format( newfilename))
