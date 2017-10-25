import os
import time

count_left = 0
count_right = 0
double = '{'+'}'

file = open('new_skill_name.txt', 'r')

for line in file:
	skill_name = line


new_skill_dir = 'C:\\Users\\lyons\\jenkins\\workspace\\alexa_skills_pipeline\\skills\\' + str(skill_name)
os.chdir(new_skill_dir)
file.close()

###################################################

skill = open('skill.json', 'r')
for line in skill:
	if '{' in line:
		count_left = count_left + 1

	elif '}' in line:
		count_right = count_right + 1

skill.close()
 ##################################################

skill = open('skill.json', 'r')

for line in skill:
	if double in line:
		count_left = count_left - 1

skill.close()

print('')
print('Skill Name: ', skill_name)
print('Left parenthesis: ', count_left)
print('Right parenthesis: ', count_right)
print('')

####################################################

if count_right == count_left:
	print('Syntax test passed')
else:
	print('Syntax Error')

print('')