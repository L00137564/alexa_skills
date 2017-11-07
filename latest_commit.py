## AUTHOR: Owen Lyons
## DATE: 25/10/17
## PROGRAM DESC: Get latest modified folder / skill

import os

svn_log = 'C:\\Users\\x213859\\AppData\\Local\\TortoiseSVN\\logfile.txt'
list = []

for line in reversed(open(svn_log).readlines()):
    line = line.rstrip()
    if 'Modified' in line:
      list.append(line)

print(list[0])

l = list[0]
latest_file = l.rsplit("\\")[-1]
latest_folder = l.rsplit("\\")[-2]

print(latest_file)
print(latest_folder)

file = open('latest_modified_skill.txt', 'w')
file.write(str(latest_folder))
file.close()
  
