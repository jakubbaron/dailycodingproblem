#!/usr/bin/env python
# Good morning. Here's your coding interview problem for today.
#
# This problem was asked by Palantir.
#
# Write an algorithm to justify text. Given a sequence of words and an integer
# line length k, return a list of strings which represents each line, fully
# justified.
#
# More specifically, you should have as many words as possible in each line.
# There should be at least one space between each word. Pad extra spaces when
# necessary so that each line has exactly length k. Spaces should be distributed
# as equally as possible, with the extra spaces, if any, distributed starting from
# the left.
#
# If you can only fit one word on a line, then you should pad the right-hand side
# with spaces.
#
# Each word is guaranteed not to be longer than k.
#
# For example, given the list of words ["the", "quick", "brown", "fox", "jumps",
# "over", "the", "lazy", "dog"] and k = 16, you should return the following:
#
# ["the  quick brown", # 1 extra space on the left
# "fox  jumps  over", # 2 extra spaces distributed evenly
# "the   lazy   dog"] # 4 extra spaces distributed evenly

def justify(arr, k):
  result = []
  if len(arr) == 0:
    return result
  current_line = []
  current_line_length = 0
  for word in arr:
    word_len = len(word)
    if current_line_length + word_len == k:
      current_line.append(word)
      result.append(' '.join(current_line))
      current_line = []
      current_line_length = 0

    elif current_line_length + word_len > k:
      number_of_extra_spaces = k - current_line_length + 1
      number_of_words = len(current_line)
      spaces_per_word = number_of_extra_spaces / (number_of_words - 1)
      current_line = [s + spaces_per_word * ' ' for s in current_line]
      for i in range(0, number_of_extra_spaces % number_of_words):
        current_line[i] += ' '
      result.append(' '.join(current_line))
      current_line_length = word_len + 1
      current_line = []
      current_line.append(word)

    else:
      current_line.append(word)
      current_line_length += word_len + 1
      print "current line length:", current_line_length, "arr:", str(current_line)

  if len(current_line) == 1:
    reult.append(current_line + (current_line_length * ' '))
  elif current_line_length == k:
    result.append(' '.join(current_line))
  elif current_line_length < k:
    number_of_extra_spaces = k - current_line_length + 1
    number_of_words = len(current_line)
    spaces_per_word = number_of_extra_spaces / (number_of_words - 1)
    print "spaces per word", spaces_per_word
    print "words", number_of_words
    print "extra spaces", number_of_extra_spaces
    current_line = [s + spaces_per_word * ' ' for s in current_line]
    for i in range(0, (number_of_extra_spaces - (spaces_per_word * (number_of_words - 1))) % (number_of_words - 1)):
      current_line[i] += ' '
    result.append(' '.join(current_line))

  print result
  return result

def main():
 arr = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
 k = 16
 result = justify(arr, k)
 assert len(result) == 3
 assert result[0] == "the  quick brown"
 assert len(result[0]) == k
 assert result[1] == "fox  jumps  over"
 assert len(result[1]) == k
 assert result[2] == "the   lazy   dog"
 assert len(result[2]) == k

if __name__ == "__main__":
  main()
