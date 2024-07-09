
import csv
f=open("color.csv","r")
a=csv.reader(f,delimiter=",")
for l in a :
    print(l)
f.close()
import os
os.remove("C:/Users/saido/OneDrive/Bureau/test.txt")