# fzen.py
# format zen tag and append to tags.js file
# USAGE:
# 1. open terminal
# 2. copy code into clipboard
# 3. python3 fzen.py
# 4. enter new tag name
# 5. repeat and check tags.js to verify
# 6. test new tags with codescriber

import os
import pyperclip

# change working directory to path for this file
p = os.path.realpath(__file__)
os.chdir(os.path.dirname(p))

code = pyperclip.paste().split("\n")
tagname = input("Enter tag name: ")
if tagname == "":
    exit()

tagstr = "\"" + tagname + "\": \""

# escape all double quotes
for line in code:
    line = line.replace('"', r'\"')
    tagstr += line + "\\n"
tagstr += "\","  # concat final double quote

print("")
print(tagstr)
print("")

# read in the Zen tags file
with open("tags.js", "r") as fin:
    zenlst = fin.readlines()
zenlst = [i.strip() for i in zenlst]

# add the new tag at end of list
zenlst.remove("}; //")
zenlst.append(tagstr)

# write back the list to the file
with open("tags.js", "w") as fout:
    for line in zenlst:
        fout.write(line + "\n")
    fout.write("}; //\n")

print("\nDone.\n")
