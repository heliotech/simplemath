`simplemath` -- project for learning 4 basic algebraic operations with python
=============================================================================

`simplemath` project presents the visualization of 4 basic algebraic operations. With help of the ascii or UTF characters it assists younger children in learning how to calculate and how to use the python programming language.

The project was build to learn how to:
1. build python packages and upload them them to PyPI,
2. use GitHub.

!TODO: set the number of versions: 3 or 4.

Contents
--------

1. `simplemath.py`

The file `simplemath.py` contains 4 functions, `add`, `sub`, `mul`, `div`, which illustrate basic arithmetical operation, respectivey addition, subtraction, multiplication and division. All the functions represent provided arguments with simple dots, which can be counted, by children, to check their understanding of an operation. The functions are designed for positive, integer arguments and results. Each function can be used in an interactive pyhon session, or `simple_examples.py` can be run to show all the functions in action.

`sub`, `mul` and `div` functions use python fstrings, while `add` applies only simple concatenation. This approach shows better visual effect of the former solution.

WARNING! `simplemath.py` has no error handling, except for `div`, and should be used with caution.

Author
------

khaz pykhaz@o2.pl

Irresponsibility disclaimer
----------------------------

The software is provided 'as is', the author takes no responsibility for any possible problems.