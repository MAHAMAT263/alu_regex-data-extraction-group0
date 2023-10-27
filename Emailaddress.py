#!/usr/bin python3

import re

text = input()
Emailaddress = r"\S+@\S+\.\S+"
Email = re.search(Emailaddress, text)
print('Email address: ', Email[0])
