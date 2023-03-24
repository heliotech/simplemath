#!/usr/bin/python3

# simpleMath.py

"""
A part of the Simplemath Project

Simple version of 4 basic algebraic operations in python.

Symbols:
    subtraction -> – (regular - vs. –)
    multiplication \u00D7 -> ×
    division \u00F7 -> ÷

"""

ftitle = __file__.split('/')[-1].split('.')[0]


def printEval(code):
    print(code + " :→")
    eval(code)
    print()


def add(a, b):
    """ Addition """

    print("Addition:")
    print("•"*a, "(", a, ") +", "•"*b, "(", b, ") =", "•"*(a + b),
          "(", (a + b), ")")


def sub(a, b):
    print("Subtraction:")
    # print("•"*a, "–", "•"*b, "=", "•"*(a - b))
    print(f"{'•'*a} ({a}) – {'•'*b} ({b}) = {'•'*(a - b)} ({(a - b)}) ")


def mul(a, b):
    print("Multiplication:")
    print(f"{'•'*a} ({a}) × {'•'*b} ({b}) = {'•'*(a*b)} ({a + b})")


def div(a, b):
    print("Division:")
    print("(valid only for integer arguments and the result!)")
    assert isinstance(a, int) and isinstance(b, int) and (a//b == a/b)
    # print("•"*a, "÷", "•"*b, "=", "•"*(a//b))
    print(f"{'•'*a} ({a}) ÷ {'•'*b} ({b}) = {'•'*(a//b)} ({a//b})")


def simpleMath_demo():
    print(ftitle)
    printEval("add(2, 3)")
    printEval("sub(5, 2)")
    printEval("mul(3, 4)")
    printEval("div(8, 2)")
    # printEval("div(8, 2.5)")


if __name__ == '__main__':
    simpleMath_demo()
