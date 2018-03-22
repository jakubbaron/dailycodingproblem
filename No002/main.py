#!/bin/python

# Good morning. Here's your coding interview problem for today.
# This problem was asked by Uber.
# Given an array of integers, return a new array such that
# each element at index i of the new array is the product of all
# the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5],
# the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

def dividing(in_array):
  from operator import mul, truediv
  product = reduce(mul, in_array)
  output = [product/i for i in in_array]
  return output

def no_dividing(in_array):
  len_arr = len(in_array)
  left = [1] * len_arr

  for i in range(1, len_arr):
    left[i] = in_array[i-1]*left[i-1]

  right = [1] * len_arr
  for i in range(len_arr - 2, -1, -1):
    right[i] = in_array[i+1] * right[i+1]

  prod = [1] * len_arr
  for i in range(0, len_arr):
    prod[i] = left[i] * right[i]

  return prod

def o_one_space(in_array):
  len_arr = len(in_array)
  temp = 1
  prod = [1] * len_arr
  for i in range(0, len_arr):
    prod[i] = temp
    temp *= in_array[i]

  temp = 1
  for i in range(len_arr - 1, -1, -1):
    prod[i] *= temp
    temp *= in_array[i]

  return prod

def benchmark(method, name, runs, in_array):
  from datetime import datetime
  start_time = datetime.now()
  for i in range(0, runs):
    output = method(in_array)
  time_elapsed = datetime.now() - start_time

  print str(name) + ": Output:" + str(output)
  per_run = (time_elapsed.microseconds/(runs * 1.0))
  print str(name) + ": Per run: " + str(per_run) + "us"


def main():
  in_array = [1, 2, 3, 4, 5]
  runs = 10
  benchmark(dividing, "With Division", runs, in_array)
  benchmark(no_dividing, "Without Division", runs, in_array)
  benchmark(o_one_space, "Without Division one_space", runs, in_array)

if __name__ == "__main__":
  main()
