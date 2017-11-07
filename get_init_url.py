# Owen Lyons
# Script to get url of 'ask init --no-browser'

import os
import re
import time as t

p = os.popen("echo y | ask init -p owen --no-browser").read()
t.sleep(5)

print(p)

file = open("url_token.txt", "w")
file.write(str(p))
file.close()

file1 = open("url_token.txt", "r")
file2 = open("url_token_string.txt", "w")


url = re.search("(?P<url>https?://[^\s]+)", p).group("url")

file2.write(url)

file1.close()
file2.close()
