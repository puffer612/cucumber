dicts = {"username": "${185}"}
for key,value in dicts.items():
    print(value[2:len(value)-1])

import re
s = """
scene: "uc_login"
"""
content = re.sub('[${}]','',s)

# print(content)