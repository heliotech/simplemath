# demo_simple.py

"""
Examples for `simplemath` project
"""

from src.simplemath import add, sub, mul, div


def addition():
    print("Examples of the application of `add` function\n")
    calculations = ["add(2, 3)", "add(6, 7)", "add(8, 2)"]
    for i, calculation in enumerate(calculations):
        print(f"{i + 1}) {calculation} 🠂")
        eval(calculation)
        print()


def subtraction():
    print("Examples of the application of `sub` function\n")
    calculations = ["sub(5, 2)", "sub(9, 7)", "sub(6, 3)"]
    for i, calculation in enumerate(calculations):
        print(f"{i + 1}) {calculation} 🠂")
        eval(calculation)
        print()


def multiplication():
    print("Examples of the application of `mul` function\n")
    calculations = ["mul(3, 2)", "mul(4, 3)", "mul(6, 3)"]
    for i, calculation in enumerate(calculations):
        print(f"{i + 1}) {calculation} 🠂")
        eval(calculation)
        print()


def division():
    print("Examples of the application of `div` function\n")
    calculations = ["div(6, 2)", "div(9, 3)", "div(12, 6)", "div(12, 2)"]
    for i, calculation in enumerate(calculations):
        print(f"{i + 1}) {calculation} 🠂")
        eval(calculation)
        print()
