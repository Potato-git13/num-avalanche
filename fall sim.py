import os
import random as r
try:
        dirpathstr = "C:/Users/lanve/Desktop/save_num_dir/" 
        os.mkdir(dirpathstr)
except:
        pass

num1 = int(input("1>"))
num2 = int(input("2>"))
dirpath = str(num1) + " x " + str(num2) +  " - "+ str(r.randint(0, 50)) + " sav.save"
try:
        sav = open(dirpathstr + dirpath, "x")
        sav.close()
except FileExistsError:
        print("doot")
save = open(dirpathstr + dirpath, "a")
i = 1
num3 = num1 + num2
while i < 100:
	num3 *= i
	num3 *= num1
	num3 *= num2
	print(str(num3))
	save.write(str(num3)+"\n")
	i += 1
save.close()


