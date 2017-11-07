## AUTHOR: Owen Lyons
## DATE: 25/10/17
## PROGRAM DESC: Deploy skill

import os
import time as t

print('///////////////////////////////////////////////////////////////////////////////////////////')
print('///////////////////////////////  DEPLOY SKILL /////////////////////////////////////////////')
print('///////////////////////////////////////////////////////////////////////////////////////////')

# Get latest modified skill name
file = open('latest_modified_skill.txt', 'r')

for line in file:
	skill_name = line
file.close()
print(skill_name)

# Change directory to the latest modified skill
new_skill_dir = 'C:\\Users\\x213859\\jenkins\\workspace\\alexa_skills_test\\' + str(skill_name)
os.chdir(new_skill_dir)

# Print dir for debugginf purposes
cwd = os.getcwd()
print('Current directory is: ', cwd)

# Deploy skill to Alexa Dev Portal
deploy = 'C:\\Users\\x213859\\AppData\\Roaming\\npm\\ask deploy -t skill -p owen'

# Print output to monitor deployment 
deploy_skill = os.popen(deploy).read()
print(deploy_skill)
