import sys 
import os

def uninstall():
    uninstall_list = ["reg.reg","bat_file.bat","setup.py","test.py"]
    for i in range(4):
        os.remove(uninstall_list[i])
    bat_file.write(bat_contenu)


if sys.argv[0] == "-uninstall":
    uninstall()

filename = sys.argv[2]
action = sys.argv[1]

a = list(filename)
index = filename.find(".")
a.insert(index," [{}]".format(action))
newfilename=""
for element in a:
    newfilename+=element
os.rename(r'{0}'.format(filename),r'{0}'.format( newfilename))
