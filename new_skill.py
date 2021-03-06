## AUTHOR: Owen Lyons
## DATE: 25/10/17
## PROGRAM DESC: Create new skill

import os
import time as t

print('///////////////////////////////////////////////////////////////////////////////////////////')
print('///////////////////////////////  NEW SKILL ///////////////////////////////////////////')
print('///////////////////////////////////////////////////////////////////////////////////////////')

skill_name = 'test_skill_501'
ask_new = 'C:\\Users\\x213859\\AppData\\Roaming\\npm\\ask new -n ' + skill_name + ' -p owen'

cwd = os.getcwd()

file = open('new_skill_name.txt', 'w')
file.write(skill_name)
file.close()

os.chdir('C:\\Users\\x213859\\jenkins\\workspace\\alexa_skills_test')

output = os.popen(ask_new).read()
print('OUTPUT: ' + str(output))

if 'New'in output:
	print('SUCCESS:  ' + skill_name + ' created')
	t.sleep(3)

else:
	print('ERROR__Could not create new skill')
