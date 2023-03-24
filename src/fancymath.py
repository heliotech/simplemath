#!/usr/bin/python3
# -*- coding: utf-8 -*-

# fancymath.py

"""
A part of the Simplemath Project

Fancy version of `simplemath.py`, 4 basic algebraic operations in python.
The arguments and results are presented with UTF icons.
Each number is represented with the help of dedicated function, `showNumber`

Symbols:
    subtraction chr(8211) -> – (regular - vs. –)
    multiplication \u00D7 -> ×
    division \u00F7 -> ÷

"""
# from numpy import sign
from math import copysign

from mutils import DbgInfo

DBG = True
dbgi = DbgInfo(DBG=DBG)
printd = dbgi.printd_()

ftitle = __file__.split('/')[-1].split('.')[0]

# Markers:
mrkDot = "•"
mrkCat = chr(128008)  # 🐈
mrkDog = chr(128021)  # 🐕
mrkSnake = chr(128013)  # 🐍


def sign(value):
    """ Adaptation of `copysign` function """

    return copysign(1, value)


def printEval(code):
    """ Prints and evaluates `code` """

    print(code + " 🠂")
    eval(code)
    print()


def representNumber(num, marker=mrkDot, sep=" ", part=5,
                    DBG=False):
    """ Getting graphical representation of a number.

    Args:
        num: int - number to be graphically represented,
        marker: str - char for a marker,
        sep: str - number parts (sections) separator,
        part: int - length of the number part (section),
        pos: int - position of the number in the calculaiton, def. -1;
            0 for the first position.
    """

    if float(num).is_integer():
        num = int(num)
    errMsg = ""
    parts = abs(num)//part
    sgn = "" if sign(num) >= 0 else "(-)"
    try:
        if parts > 0:
            mainPart = sep.join(marker*part for i in range(parts))
            remainder = abs(num) - part*parts
        else:
            mainPart = marker*abs(num)
            remainder = 0
        remainderGraph = marker*remainder if remainder else ""
        remainderGraph = (sep + remainderGraph if remainder > 0
                          else remainderGraph)
    except TypeError:
        errMsg = ("A problem occured:\n"
                  "only integer numbers can be represented, "
                  f"but it happened to be {num}\n")
        return "(?)", errMsg
    numGraph = mainPart + remainderGraph
    printd(f"{part = }, {parts = }, {num = :>3}, {remainder = }", DBG=False)
    printd(f"{num = }, {len(mainPart) = }, {remainder = },\n"
           f"{len(remainderGraph) = } <= {remainderGraph}\n"
           f"{numGraph = }",
           src="representNumber", DBG=DBG)

    newLine0 = "" if len(numGraph) < 21 else "\n"  # 'last' new line

    return f"{newLine0}{sgn}{numGraph}", errMsg


def add(a, b, marker="•"):
    res = a + b
    res = round(res, 2) if len(str(abs(res) - int(abs(res)))) > 4 else res
    aGraph = representNumber(a, marker=marker)[0]
    bGraph = representNumber(b, marker=marker)[0]
    resGraph, err = representNumber(res, marker=marker)
    print("Multiplication: "
          f"{aGraph} ({a}) + {bGraph} ({b}) = {resGraph} ({res})\n{err}")


def sub(a, b, marker="•"):
    res = a - b
    res = round(res, 2) if len(str(abs(res) - int(abs(res)))) > 4 else res
    aGraph = representNumber(a, marker=marker)[0]
    bGraph = representNumber(b, marker=marker)[0]
    resGraph, err = representNumber(res, marker=marker)
    print("Subtraction: "
          f"{aGraph} ({a}) – {bGraph} ({b}) = {resGraph} ({res})\n{err}")


def mul(a, b, marker="•"):
    res = a*b
    res = round(res, 2) if len(str(abs(res) - int(abs(res)))) > 4 else res
    aGraph = representNumber(a, marker=marker)[0]
    bGraph = representNumber(b, marker=marker)[0]
    resGraph, err = representNumber(res, marker=marker)
    print("Multiplication: "
          f"{aGraph} ({a}) \u00D7 {bGraph} ({b}) = {resGraph} ({res})\n{err}")


def div(a, b, marker="•"):
    res = a/b
    print("")
    a = int(a) if float(a).is_integer() else a
    b = int(b) if float(b).is_integer() else b
    assert (isinstance(a, int) and isinstance(b, int) and
            (a//b == res))
    res = round(res, 2) if len(str(abs(res) - int(abs(res)))) > 4 else res
    aGraph = representNumber(a, marker=marker)[0]
    bGraph = representNumber(b, marker=marker)[0]
    resGraph, err = representNumber(res, marker=marker)
    print("Division:\n(valid only for integer arguments and the result!)\n"
          f"{aGraph} ({a}) \u00F7 {bGraph} ({b}) = {resGraph} ({int(res)})"
          f"\n{err}")


def main():
    nrs = [3, 7, 11., 11]
    bes = [2, 3, 4, 5]
    mrkrs = [mrkDot, mrkCat, mrkDog, mrkSnake]
    for i, nr in enumerate(nrs):
        marker = mrkrs[i]
        nrGraph, errMsg = representNumber(nr, marker)
        print(f"{i}) {nr}: {nrGraph = }\n{errMsg = }")
    print(mrkDot, type(mrkDot))
    print(mrkDog, type(mrkDog))
    for i, (a, b) in enumerate(zip(nrs, bes)):
        mul(a, b, mrkrs[i])
    add(3, 5.3, marker)
    sub(12, 3, marker)
    div(14., 2, marker)

if __name__ == '__main__':
    main()
