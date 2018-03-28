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
  if value != root.value:
    return False
  if root.left is None and root.right is None:
    return True

  output = True
  if root.left is not None:
    output = output and is_unival(root.left, root.value)
  if root.right is not None:
    output = output and is_unival(root.right, root.value)

  return output

def count_univals(root):
  if root is None:
    return 0
  left = count_univals(root.left)
  right = count_univals(root.right)
  this_tree = is_unival(root, root.value)
  return left + right + this_tree


def main():
  t = Tree(0)
  t.insert_left(1)
  t.insert_right(0)
  t.right.insert_right(0)
  t.right.insert_left(1)
  t.right.left.insert_left(1)
  t.right.left.insert_right(1)
  print "Found univals: " + str(count_univals(t))

if __name__ == "__main__":
    main()
