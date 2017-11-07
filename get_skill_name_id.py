# Author: Owen Lyons
# Date: 18/10/17
# Desc: alexa skills script

import os
import time as t

# Empty dictionary and lists to be filled
skill_name_list = []
skill_ID_list = []
skill_dict = {}

# Run ASK CLI command, get latest skill list and pipe out to a text file
os.system("ask api  -p owen list-skills > H:\Owen_Lyons\ALEXA\skills\list_skills.txt")
# define target strings
skill_ID = "skillId"
skill_name = "en-US"

file = open("H:\Owen_Lyons\ALEXA\skills\list_skills.txt", "r")
file_out = open("H:\Owen_Lyons\ALEXA\skills\latest_skills_id.txt", "w")

# Loop for target strings and write to file and lists
for line in file:
    if skill_name in line:
        skill_name_list.append(line)
        name =line.replace('"', '')
        file_out.write("SKILL NAME: " + str(name[14:]))

    if skill_ID in line:
        skill_ID_list.append(line)
        ID = line.replace('"', '')
        file_out.write("SKILL ID: " + str(ID[15:]))
        file_out.write("\n")

# Merge lists to create skill_name/skill_ID key/value dictionary
skill_dict = dict(zip(skill_name_list, skill_ID_list))

for k,v in skill_dict.items():
    print("NAME: ", k[17:], "ID: ", v[18:])

file.close()
file_out.close()
    


