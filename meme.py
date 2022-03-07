import os
import random
import math
import time
random.seed()
speed = int(input("Gimme speed\n"))
s = input("Gimme stringa\n")
tmp = ""
dim = pow(10,len(s))
count = 0
os.system("clear")
for c in  s:
    tmp += c
    if tmp == s:
        break
    for x in range(int(len(s)*speed)):
        os.system("clear")
        print(tmp + str(int(random.randint(dim/10,dim-1)/10)))
    dim /= 10
os.system("clear")
print(s)