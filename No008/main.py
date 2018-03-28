#!/usr/bin/env python

# Good morning. Here's your coding interview problem for today.
# This problem was asked by Google.
#
# A unival tree (which stands for "universal value") is a tree
# where all nodes under it have the same value.
#
# Given the root to a binary tree, count the number of unival subtrees.
#
# For example, the following tree has 5 unival subtrees:
#
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

class Tree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert_right(self, value):
    self.right = Tree(value)
  def insert_left(self, value):
    self.left = Tree(value)

  def walk(self):
    if self.left is not None:
      self.left.walk()
    print str(self.value)
    if self.right is not None:
      self.right.walk()

def is_unival(root, value):
  if root is None:
    return True
  if value != root.value:
    return False
  return is_unival(root.left, value) and is_unival(root.right, value)

def count_univals(root):
  if root is None:
    return 0
  left = count_univals(root.left)
  right = count_univals(root.right)
  this_tree = is_unival(root, root.value)
  return left + right + this_tree

def count_on(root):
  count, _ = faster_helper(root)
  return count

# https://www.dailycodingproblem.com/blog/unival-trees/
def faster_helper(root):
  if root is None:
    return 0, True
  left_count, is_left_unival = faster_helper(root.left)
  right_count, is_right_unival = faster_helper(root.right)
  total_count = left_count + right_count

  if is_left_unival and is_right_unival:
    if root.left is not None and root.value != root.left.value:
      return total_count, False
    if root.right is not None and root.value != root.right.value:
      return total_count, False
    return total_count + 1, True
  return total_count, False

def main():
  nums = Tree(0)
  nums.insert_left(1)
  nums.insert_right(0)
  nums.right.insert_right(0)
  nums.right.insert_left(1)
  nums.right.left.insert_left(1)
  nums.right.left.insert_right(1)
  print "Found univals in nums: " + str(count_univals(nums))
  assert count_univals(nums) == 5
  assert count_on(nums) == 5

  chars = Tree('a')
  chars.insert_left('c')
  chars.insert_right('b')
  chars.right.insert_left('b')
  chars.right.insert_right('b')
  chars.right.right.insert_right('b')
  print "Found univals in chars: " + str(count_univals(chars))
  assert count_univals(chars) == 5
  assert count_on(chars) == 5

  As = Tree('a')
  As.insert_left('a')
  As.insert_right('a')
  As.right.insert_left('a')
  As.right.insert_right('a')
  As.right.right.insert_right('A')
  print "Found univals in As: " + str(count_univals(As))
  assert count_univals(As) == 3
  assert count_on(As) == 3


if __name__ == "__main__":
    main()
