## AUTHOR: Owen Lyons
## DATE: 25/10/17
## PROGRAM DESC: Deploy skill


import os
import time as t


#file = open('new_skill_name.txt', 'r')
file = open('latest_modified_skill.txt', 'r')

for line in file:
	skill_name = line
file.close()

print(skill_name)

new_skill_dir = 'C:\\Users\\lyons\\jenkins\\workspace\\alexa_skills_pipeline\\skills\\' + str(skill_name)
os.chdir(new_skill_dir)

cwd = os.getcwd()
print('Current directory is: ', cwd)

deploy = 'C:\\Users\\lyons\\AppData\\Roaming\\npm\\ask deploy -t skill -p owen'


print('')
#deploy_skill = os.system(deploy)
deploy_skill = os.popen(deploy)

if deploy_skill:
	print(skill_name + ' deployed successfully')
else:
	print('ERROR__Skill not deployed')


