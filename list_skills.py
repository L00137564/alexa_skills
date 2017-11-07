# Author: Owen Lyons
# Date: 31/10/17
# Program: print skills
###################################################################################################
###################################################################################################
import os
import re

p = os.popen("C:\\Users\\x213859\\AppData\\Roaming\\npm\\ask api list-skills -p owen").read()

#p = os.popen("ask api list-skills -p owen").read()

print(p)

f = open('test.txt', 'w')
f.write(p)
f.close()


#print("ERROR___ERROR___ERROR___ERROR___ERROR___ERROR___ERROR___ERROR___")




