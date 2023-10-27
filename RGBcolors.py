#!/usr/bin python3

import re

text = input()
RGB_colors =r"rgb\((\d){3},\s*(\d){3},\s*(\d){3}\)"
Color=re.search(RGB_colors, text)
print('Colors: ', Color[0])
