## AUTHOR: Owen Lyons
## DATE: 25/10/17
## PROGRAM DESC: Get latest modified folder


import os
import glob

### GET LATEST MODIFIED FOLDER 
for dir in glob.glob('C:\\Users\\lyons\\jenkins\\workspace\\alexa_skills_pipeline\\skills\\*'):
  if os.path.isdir(dir):
    print(dir)

## GET LATEST MODIFIED SKILL (.json)
'''
folder = str(dir) + '\\*.json'

list_of_files = glob.glob(folder) 
latest_file = max(list_of_files, key=os.path.getctime)
print (latest_file)

'''

latest_folder = dir.rsplit("\\")[-1]

print('LATEST FOLDER: ', latest_folder)

file = open('latest_modified_skill.txt', 'w')
file.write(str(latest_folder))
file.close()
