#!/usr/bin/python3
# -*- coding: utf-8 -*-

# fancy_demo.py

"""
Examples for `simplemath` project
"""

from src.mathfancy import add, sub, mul, div


def addition():
    print("Examples of the application of `add` function\n")
    calculations = ["add(2, 3)", "add(6, 7)", "add(8, 2)"]
    for i, calculation in enumerate(calculations):
        print(f"{i + 1}) {calculation} →")
        eval(calculation)
        print()


def subtraction():
    print("Examples of the application of `sub` function\n")
    mk = 'chr(128008)'
    calculations = [f"sub(5, 2, {mk})", f"sub(9, 7, {mk})", f"sub(6, 3, {mk})"]
    for i, calculation in enumerate(calculations):
        print(f"{i + 1}) {calculation} →")
        eval(calculation)
        print()


def multiplication():
    print("Examples of the application of `mul` function\n")
    mk = 'chr(128021)'
    calculations = [f"mul(3, 2, {mk})", f"mul(4, 3, {mk})", f"mul(6, 3, {mk})"]
    for i, calculation in enumerate(calculations):
        print(f"{i + 1}) {calculation} →")
        eval(calculation)
        print()


def division():
    print("Examples of the application of `div` function\n")
    mk = "'😄'"
    calculations = [f"div(6, 2, {mk})", f"div(9, 3, {mk})",
                    f"div(12, 6, {mk})", f"div(12, 2, {mk})"]
    for i, calculation in enumerate(calculations):
        print(f"{i + 1}) {calculation} →")
        eval(calculation)
        print()
