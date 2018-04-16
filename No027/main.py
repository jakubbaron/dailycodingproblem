#!/usr/bin/env python
# Good morning. Here's your coding interview problem for today.
# This problem was asked by Facebook.
#
# Given a string of round, curly, and square open and closing brackets,
# return whether the brackets are balanced (well-formed).
#
# For example, given the string "([])[]({})", you should return true.
#
# Given the string "([)]" or "((()", you should return false.

opening_brackets = {}
opening_brackets["("] = ")"
opening_brackets["["] = "]"
opening_brackets["{"] = "}"

closing_brackets = {}
closing_brackets[")"] = "("
closing_brackets["]"] = "["
closing_brackets["}"] = "{"

def bracket_check(in_str):
  if not in_str:
    return False
  stack = []
  for bracket in in_str:
    if bracket in opening_brackets.keys():
      stack.append(bracket)
    elif bracket in closing_brackets.keys():
      if len(stack) == 0:
        return False
      elif closing_brackets[bracket] == stack[-1]:
        stack.pop()
      else:
        return False

  return len(stack) == 0

def main():
  in_str = "()"
  assert bracket_check(in_str)
  in_str = "([])[]({})"
  assert bracket_check(in_str)
  in_str = "([)]"
  assert not bracket_check(in_str)
  in_str = "((()"
  assert not bracket_check(in_str)
  in_str = ""
  assert not bracket_check(in_str)

if __name__ == "__main__":
  main()
