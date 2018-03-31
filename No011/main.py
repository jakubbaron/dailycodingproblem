#!/usr/bin/env python

# Good morning. Here's your coding interview problem for today.
# This problem was asked by Twitter.
#
# Implement an autocomplete system. That is, given a query string
# s and a set of all possible query strings, return all strings
# in the set that have s as a prefix.
#
# For example, given the query string de and the set of strings
# [dog, deer, deal], return [deer, deal].
#
# Hint: Try preprocessing the dictionary into a more efficient data
# structure to speed up queries.

class DictionaryAutocomplete:
  def __init(this, arr):
    pass

#This class assumes that words have been filtered out and that
# they all begin with the same character
class Autocomplete:
  def __init__(this, char, arr = None):
    this.value = char
    this.children = {}
    this.full_word = False
    if arr is not None:
      for item in arr:
        this.add_node(item[1:])

  def add_node(this, word):
    if len(word) == 0:
      this.full_word = True
      return
    char = word[0]
    if char not in this.children.keys():
      this.children[char] = Autocomplete(char)
    this.children[char].add_node(word[1:])

  def get_words(this):
    out = []
    #print "Value: " + str(this.value) + " kids: " + str(this.children.keys())
    if this.full_word:
      out.extend(this.value)
    for k,v in this.children.iteritems():
      words = [str(this.value) + str(w) for w in v.get_words()]
      out.extend(words)
    return out

  def autocomplete(this, query):
    if len(query) == 0:
      return []

    pass
def main():
  arr = ['dog', 'deer', 'deal']
  autocomplete = Autocomplete('d', arr)
  query = 'de'
  print str(autocomplete.get_words())

if __name__ == "__main__":
  main()
