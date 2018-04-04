#!/usr/bin/env python
# Good morning. Here's your coding interview problem for today.
# This problem was asked by Amazon.
#
# Given an integer k and a string s, find the length of the longest
# substring that contains at most k distinct characters.
#
# For example, given s = "abcba" and k = 2, the longest substring
# with k distinct characters is "bcb".

from collections import deque

def find_longest_substring(string, number_of_distinct_characters):
  indices = deque(maxlen = number_of_distinct_characters + 1)
  characters = deque(maxlen = number_of_distinct_characters + 1)
  start, end = 0, 0
  for i in range(0, len(string)):
    character = string[i]
    if character not in characters:
      characters.append(character)
      indices.append(i)
    if len(characters) > number_of_distinct_characters:
      first_char_idx = indices.popleft()
      characters.popleft()
      last_char_idx = i - 1
    else:
      first_char_idx = indices[0]
      last_char_idx = i

    if (last_char_idx) - first_char_idx > end - start:
      start, end = first_char_idx, last_char_idx

  return string[start:end+1]

def main():
  assert find_longest_substring("abcba", 2) == "bcb"
  assert find_longest_substring("aaa", 2) == "aaa"
  assert find_longest_substring("aaabbbbbbbbbcdcdcdcdcdcdcdcdc", 2) == "cdcdcdcdcdcdcdcdc"
  assert find_longest_substring("aaabbbbbbbbbcdcdcdcdcdcdcdcdc", 4) == "aaabbbbbbbbbcdcdcdcdcdcdcdcdc"
  assert find_longest_substring("aaabbbbbbbbbcdcdcdcdcdcdcdcdc", 3) == "bbbbbbbbbcdcdcdcdcdcdcdcdc"

if __name__ == "__main__":
  main()
