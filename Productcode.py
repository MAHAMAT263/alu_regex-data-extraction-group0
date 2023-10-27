#!/usr/bin python3

import re

text = input()
Productcode = r"[a-zA-Z]{3}\d{3}"
Code=re.findall(Productcode, text)
print('Product-code: ', Code[0])
