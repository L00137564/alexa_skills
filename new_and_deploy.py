## AUTHOR: Owen Lyons
## DATE: 25/10/17
## PROGRAM DESC: Create new skill

import os
import time as t

print('///////////////////////////////////////////////////////////////////////////////////////////')
print('///////////////////////////////  NEW AND DEPLOY ///////////////////////////////////////////')
print('///////////////////////////////////////////////////////////////////////////////////////////')

skill_name = 'test_skill_505'
ask_new = 'C:\\Users\\x213859\\AppData\\Roaming\\npm\\ask new -n ' + skill_name + ' -p owen'
#ask_new = 'ask new -n ' + skill_name + ' -p owen'

cwd = os.getcwd()

file = open('new_skill_name.txt', 'w')
file.write(skill_name)
file.close()

os.chdir('C:\\Users\\x213859\\jenkins\\workspace\\alexa_skills_test')

output = os.popen(ask_new).read()
print('OUTPUT: ' + str(output))

t.sleep(3)

new_skill_dir = 'C:\\Users\\x213859\\jenkins\\workspace\\alexa_skills_test\\' + str(skill_name)
os.chdir(new_skill_dir)

deploy = 'C:\\Users\\x213859\\AppData\\Roaming\\npm\\ask deploy -t skill -p owen'

print('')
#deploy_skill = os.system(deploy)
deploy_skill = os.popen(deploy).read()

print(deploy_skill)

