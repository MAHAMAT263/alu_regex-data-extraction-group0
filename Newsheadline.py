#!/usr/bin python3

import re

text = input()
Newsheadline = r"[a-zA-Z]+:\s*[a-zA-Z]+"
News=re.search(Newsheadline, text)
print('News: ', News[0])
