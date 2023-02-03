import os

path = './'+ str(input())
datanames = os.listdir(path)
for i in datanames:
    print("(" + "'" + path + "/" + i + "'" + "," + " " + "65" + ")" + ",")
