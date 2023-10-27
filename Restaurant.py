#!/usr/bin python3

import re

text = input()

restaurant_name= r"([a-zA-Z]+-[a-zA-Z]+)"
restau = re.findall(restaurant_name, text)
print('Restaurant-name: ', restau[0])
