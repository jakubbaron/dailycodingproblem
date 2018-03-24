#!/bin/python

# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
#
# For example, the input `[3, 4, -1, 1]` should give `2`. The input `[1, 2, 0]` should give `3`.
#
# You can modify the input array in-place.

def swap(arr, id_i, id_j):
  temp = arr[id_i]
  arr[id_i] = arr[id_j]
  arr[id_j] = temp

def segregate(arr):
  j = 0
  for i in range(0, len(arr)):
    if arr[i] <= 0:
      swap(arr, i, j)
      j += 1
  return j

def find_missing_positive_integer(in_arr):
  split = segregate(in_arr)
  new_size = len(in_arr) - split

  for i in range(split, len(in_arr)):
    j = i - split
    el = abs(in_arr[j]) - 1
    if el  < new_size and in_arr[el] > 0:
      in_arr[el] = -in_arr[el]

  for i in range(split, len(in_arr)):
    j = i - split
    if in_arr[j] > 0:
      return j + 1
  return new_size + 1


def benchmark(method, name, runs, in_array, expected):
  import time
  current_micro_time = lambda: int(round(time.time() * 1000000))

  start_time = current_micro_time()
  for i in range(0, runs):
    copy_array = in_array[:]
    output = method(copy_array)
  time_elapsed = current_micro_time() - start_time

  print str(name) + ": Output:" + str(output)
  per_run = (time_elapsed/(runs * 1.0))
  print str(name) + ": Per run: " + str(per_run) + "us"

  assert output == expected

def main():
  runs = 1
  in_array = [3, 4, -1, 1]
  expected = 2
  benchmark(find_missing_positive_integer, "Find missing positive integer", runs, in_array, expected)

  in_array = [1, 2, 0]
  expected = 3
  benchmark(find_missing_positive_integer, "Find missing positive integer", runs, in_array, expected)

  in_array = [-1, -2, -3, -4, -5, -6, -7, -8]
  expected = 1
  benchmark(find_missing_positive_integer, "Find missing positive integer", runs, in_array, expected)

  in_array = [0] * 100
  expected = 1
  benchmark(find_missing_positive_integer, "Find missing positive integer", runs, in_array, expected)

if __name__ == "__main__":
  main()
