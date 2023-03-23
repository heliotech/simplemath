# examples.py

filename = __file__.split('/')[-1]

print(f"Running `{filename}`...")
# print(f"{abc = }")

# from examples import simplemathExample
import examples
from examples import simple_demo
import src
from src.simplemath import add

print(f"{filename}: {examples = }")
print(f"{filename}: {simple_demo = }")
print(f"{src = }")
print(f"{add = }")
add(2, 3)

simple_demo.addition()
simple_demo.subtraction()
simple_demo.multiplication()
simple_demo.division()
