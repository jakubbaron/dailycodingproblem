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

def brute_force:w(arr):
  l = len(arr)
  max_pair = (None, None)
  max_sum = None
  for i in range(0, l):
    for j in range(0, l):
      if j not in [i - 1, i, i + 1]:
        s = arr[i] + arr[j]
        if s > max_sum: #everything is greater than None
          max_sum = s
          max_pair = (arr[i], arr[j])
  return max_pair

def check_equal(pair1, pair2):
  first1, second1 = pair1
  first2, second2 = pair2
  return (first1 == first2 and second1 == second2) or (first1 == second2 and second1 == first2)

def main():
  assert check_equal((4,8), (8,4))
  assert check_equal((5,5), (5,5))

  arr = [2, 4, 6 ,8]
  expected_pair = (4, 8)
  assert check_equal(brute_force(arr), expected_pair)

  arr = [5, 1, 1, 5]
  expected_pair = (5, 5)
  assert check_equal(brute_force(arr), expected_pair)

if __name__ == "__main__":
    main()
