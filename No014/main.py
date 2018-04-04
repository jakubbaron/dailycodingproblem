#!/usr/bin/env python
# Good morning. Here's your coding interview problem for today.
# This problem was asked by Google.
#
# The area of a circle is defined as pi * r ^ 2. Estimate Pi to 3 decimal places
# using a Monte Carlo method.
#
# Hint: The basic equation of a circle is x2 + y2 = r2.

import math
from random import uniform

def single_run():
  x, y = uniform(-1.0, 1.0), uniform(-1.0, 1.0)
  return 4.0 * ((x**2 + y**2) <= 1)

def average(n):
    return sum( single_run() for _ in range(n) ) / n

def monte_carlo(precision):
  current_pi = 0.0
  last_pi = 100.0
  iteration = 0

  while iteration < 10 or math.sqrt(math.fabs(current_pi - last_pi)) >= precision:
    iteration += 1
    last_pi = current_pi
    current_pi = ((current_pi * (iteration - 1)) + single_run()) / iteration
  return iteration, current_pi

def main():
  runs, estimate = monte_carlo(0.001)
  print "Runs: " + str(runs) + " Estimated Pi: " + str(estimate)
  print "Second method, estimated pi: " + str(average(runs))

if __name__ == "__main__":
  main()
