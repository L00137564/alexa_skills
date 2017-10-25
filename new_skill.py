import os
import time as t

skill_name = 'test_skill_50'
ask_new = 'ask new -n ' + skill_name + ' -p owen'
ask_deploy = 'ask deploy -t skill -p owen'
cwd = os.getcwd()

file = open('new_skill_name.txt', 'w')
file.write(skill_name)
file.close()

os.chdir('C:\\Users\\lyons\\jenkins\\workspace\\alexa_skills_pipeline\\skills')

output = os.popen(ask_new).read()
print('OUTPUT: ', output)

if 'New'in output:
	print('SUCCESS:  ' + skill_name + ' created')
	t.sleep(3)

else:
	print('ERROR__Could not create new skill')