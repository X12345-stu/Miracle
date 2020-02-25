import os
path = "C:/Users/Rainey/Desktop/git/unit2/readme.md"
if os.path.isfile(path):
    f = open(path, 'r')
    print(len(f.read()))
    f.close()

