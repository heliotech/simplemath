#!/usr/bin/python3
# -*- coding: utf-8 -*-

# fancy_examples.py

filename = __file__.split('/')[-1]

print(f"Running `{filename}`...")
# print(f"{abc = }")

import examples
from examples import demo_fancy
import src
from src.simplemath import add

print(f"{filename}: {examples = }")
print(f"{filename}: {demo_fancy = }")
print(f"{src = }")
print(f"{add = }")
add(2, 3)

demo_fancy.addition()
demo_fancy.subtraction()
demo_fancy.multiplication()
demo_fancy.division()
