#!/usr/bin/env python

# Good morning. Here's your coding interview problem for today.
# This problem was asked by Airbnb.
#
# Given a list of integers, write a function that returns the
# largest sum of non-adjacent numbers. Numbers can be 0 or negative.
#
# For example, [2, 4, 6, 8] should return 12, since we pick 4 and 8.
# [5, 1, 1, 5] should return 10, since we pick 5 and 5.
#
# Follow-up: Can you do this in O(N) time and constant space?

def largest_non_consecutive_sum(arr):
  l = len(arr)
  incl = arr[0]
  excl = 0
  for i in range(1, l):
    temp = incl
    incl = max(excl + arr[i], incl)
    excl = temp

  return incl

def main():
  arr = [2, 4, 6 ,8]
  print "Sum: " + str(largest_non_consecutive_sum(arr))
  assert (largest_non_consecutive_sum(arr) == 12)

  arr = [5, 1, 1, 5]
  print "Sum: " + str(largest_non_consecutive_sum(arr))
  assert (largest_non_consecutive_sum(arr) == 10)

  arr = [1, 2, -5, 3, -5, -5, -5, -5]
  print "Sum: " + str(largest_non_consecutive_sum(arr))
  assert (largest_non_consecutive_sum(arr) == 5)

  arr = [4, 1, 1, 4, 2, 1]
  print "Sum: " + str(largest_non_consecutive_sum(arr))
  assert (largest_non_consecutive_sum(arr) == 9)

if __name__ == "__main__":
    main()
