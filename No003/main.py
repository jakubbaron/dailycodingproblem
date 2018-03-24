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

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
  def __str__(self):
    return str(serialize(self))

def serialize(root):
  output = {}
  output["val"] = str(root.val)
  if root.left:
    output["left"] = serialize(root.left)
  if root.right:
    output["right"] = serialize(root.right)

  return str(output)

import ast
def deserialize(data):
  dictionary = ast.literal_eval(data)
  val = dictionary.get("val", "")
  left = None
  if "left" in dictionary:
    left = deserialize(dictionary["left"])
  right = None
  if "right" in dictionary:
    right = deserialize(dictionary["right"])
  return Node(val, left, right)

def main():
  node = Node('root', Node('left', Node('left.left')), Node('right'))
  print "Serialized node: " + str(serialize(node))

  new_node = deserialize(serialize(node))
  print "From deserialized node: " + str(serialize(new_node))

  assert deserialize(serialize(node)).left.left.val == 'left.left'
  assert deserialize(serialize(node)).right.val == 'right'
  assert deserialize(serialize(node)).left.val == 'left'
  assert deserialize(serialize(node)).val == 'root'

if __name__ == "__main__":
  main()
