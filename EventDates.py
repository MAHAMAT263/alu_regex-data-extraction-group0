#!/usr/bin python3

import re

text = input()
Eventdates = r"[a-zA-Z]{3}\s(0?[1-9]|[12][0-9]|3[01]),\s\d{4}\s-\s(0?[1-9]|1[0-2]):(0[0-9]|[1-5][0-9])(AM|PM)"
Dates = re.search(Eventdates, text)
print('Event Dates: ', Dates[0])
