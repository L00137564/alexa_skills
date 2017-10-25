import os
import time as t


file = open('new_skill_name.txt', 'r')

for line in file:
	skill_name = line

print(skill_name)

new_skill_dir = 'C:\\Users\\lyons\\jenkins\\workspace\\alexa_skills_pipeline\\skills\\' + str(skill_name)
os.chdir(new_skill_dir)

cwd = os.getcwd()
print(cwd)

deploy = 'ask deploy -t skill -p owen'

print('')
deploy = os.system(deploy)

print(skill_name + ' deployed successfully')
