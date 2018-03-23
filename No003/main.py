#!/bin/python

#Good morning. Here's your coding interview problem for today.
#This problem was asked by Google.
#Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
#For example, given the following Node class
#
#class Node:
#   def __init__(self, val, left=None, right=None):
#       self.val = val
#       self.left = left
#       self.right = right
#
#The following test should pass:
#node = Node('root', Node('left', Node('left.left')), Node('right'))
#assert deserialize(serialize(node)).left.left.val == 'left.left'


def benchmark(method, name, runs, in_array):
  import time
  current_micro_time = lambda: int(round(time.time() * 1000000))
  start_time = current_micro_time()
  for i in range(0, runs):
    output = method(in_array)
  time_elapsed = current_micro_time() - start_time

  print str(name) + ": Output:" + str(output)
  per_run = (time_elapsed/(runs * 1.0))
  print str(name) + ": Per run: " + str(per_run) + "us"


def main():
  in_array = [1, 2, 3, 4, 5]
  runs = 1000

if __name__ == "__main__":
  main()
