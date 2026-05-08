"""QUESTION 3
List Summation
Given the list numbers = [1, 2, 3, 4, 5], write a for loop that
calculates the total sum of all elements in the list."""

numbers = [1, 2, 3, 4, 5]

t = 0

for num in numbers:
    t = t + num

print("total sum =", t)