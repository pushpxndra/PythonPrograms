"""QUESTION 1
The Variable Swap
Given two variables, a = 5 and b = 10,
swap their values so that a becomes 10
and b becomes 5 without using a third
temporary variable.
Concept: Pythonic assignments and tuple unpacking.
"""

a = 5
b = 10
a, b = b, a
print("a =", a)
print("b =", b)