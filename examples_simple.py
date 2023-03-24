# examples.py

filename = __file__.split('/')[-1]

print(f"Running `{filename}`...")
# print(f"{abc = }")

import examples
from examples import demo_simple
import src
from src.simplemath import add

print(f"{filename}: {examples = }")
print(f"{filename}: {demo_simple = }")
print(f"{src = }")
print(f"{add = }")
add(2, 3)

demo_simple.addition()
demo_simple.subtraction()
demo_simple.multiplication()
demo_simple.division()
