#!/usr/bin python3

import re

text = input()
Ingredient_list=r"([a-zA-Z]+,)+[a-zA-Z]+"
Ingredients=re.search(Ingredient_list, text)
print('Ingredients: ', Ingredients[0])
