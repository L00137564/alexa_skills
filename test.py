# Author: Owen Lyons
# Date: 16/10/17
# Program: ask_cli menu
###################################################################################################
###################################################################################################
import os
import re

print("SUCCESS __ SUCCESS __ SUCCESS __ SUCCESS __ SUCCESS __ SUCCESS __ SUCCESS __ SUCCESS __ SUCCESS __ SUCCESS __ SUCCESS __ ")

p = os.popen("echo y|ask init -p owen --no-browser").read()

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


### TOKEN = ANQAtGDxsnjYoBRnhlEk





