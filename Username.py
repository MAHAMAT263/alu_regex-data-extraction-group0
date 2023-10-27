#!/usr/bin python3

import re

text = input()
SocialUsername = r"@\w+"
Username = re.search(SocialUsername, text)
print('Username :', Username[0])
