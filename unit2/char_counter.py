import os
import numpy as np
path = "C:/Users/Rainey/Desktop/git/unit2/readme.md"
if os.path.isfile(path):
    f = open(path, 'r')
    data = f.read()
    print(len(data.split()))
    f.close()
