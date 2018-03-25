#!/bin/python

# Good morning. Here's your coding interview problem for today.
# This problem was asked by Jane Street.
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last
# element of that pair.
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:
# def cons(a, b):
#     return lambda f : f(a, b)
# Implement car and cdr.

def cons(a, b):
  return lambda f: f(a, b)

def car(pair):
  return pair(lambda p, q: p) #Adding source: https://stackoverflow.com/a/32293382/4241944

def cdr(pair):
  return pair(lambda p, q: q)

def main():
  assert car(cons(3, 4)) == 3
  assert cdr(cons(3, 4)) == 4

if __name__ == "__main__":
  main()
