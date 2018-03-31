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
  def __init__(this, arr = None):
    this.char = None
    this.children = {}
    this.full_word = False
    if arr is not None:
      for item in arr:
        this.add_node(item)

  def add_node(this, word):
    if len(word) == 0:
      return
    char = word[0]

    #First added node
    if this.char is None:
      this.char = char

    #Shouldn't be appended to this autocomplete
    if this.char != char:
      return

    if len(word) == 1:
      #print "This is the full word"
      this.full_word = True
      return

    char = word[1]
    if char not in this.children.keys():
      #print "New autocomplete for: " + str(char) + " this char: " + str(this.char)
      this.children[char] = Autocomplete()
    #print "Invoking add_node: " + str(word[1:])
    this.children[char].add_node(word[1:])

  def get_words(this):
    out = []
    #print "char: " + str(this.char) + " kids: " + str(this.children.keys())
    if this.full_word:
      out.extend(this.char)
    for k,v in this.children.iteritems():
      words = [str(this.char) + str(w) for w in v.get_words()]
      out.extend(words)
    return out

  def autocomplete(this, query):
    if len(query) == 0:
      return []

    pass
def main():
  arr = ['dog', 'deer', 'deal']
  autocomplete = Autocomplete(arr)
  query = 'de'
  print str(autocomplete.get_words())

if __name__ == "__main__":
  main()
