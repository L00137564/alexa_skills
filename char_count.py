## AUTHOR: Owen Lyons
## DATE: 25/10/17
## PROGRAM DESC: Count squirly brackets, if matched then syntax is ok


import os
import time

print('///////////////////////////////////////////////////////////////////////////////////////////')
print('///////////////////////////////  TEST - BRACE COUNT////////////////////////////////////////')
print('///////////////////////////////////////////////////////////////////////////////////////////')

count_left = 0
count_right = 0
double = '{'+'}'

#file = open('new_skill_name.txt', 'r')
file = open('latest_modified_skill.txt', 'r')

for line in file:
	skill_name = line

new_skill_dir = 'C:\\Users\\x213859\\jenkins\\workspace\\alexa_skills_test\\' + str(skill_name)
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
print('Left brackets: ', count_left)
print('Right brackets: ', count_right)
print('')

####################################################

if count_right == count_left:
	print('Syntax test passed')
else:
	print('Syntax Error')

