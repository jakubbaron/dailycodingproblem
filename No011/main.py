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
  def __init__(this):
    this.autocompletes = {}
    pass
  def add_autocomplete(this, ac):
    if ac.char is None:
      print "Cannot add empty Autocomplete"
      return
    this.autocompletes[ac.char] = ac
  def autocomplete(this, query):
    if len(query) == 0:
      print "Provided empty string"
      return
    char = query[0]
    if char not in this.autocompletes.keys():
      return []

    return this.autocompletes[char].autocomplete(query)

#This class assumes that words have been filtered out and that
# they all begin with the same character
class Autocomplete:
  def __init__(this, arr = None):
    this.char = None
    this.children = {}
    this.full_word = False
    if arr is not None:
      for item in arr:
        this.add_word(item)

  def add_word(this, word):
    if len(word) == 0:
      return
    char = word[0]

    #First added word
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
    #print "Invoking add_word: " + str(word[1:])
    this.children[char].add_word(word[1:])

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
    out = []
    if len(query) == 0:
      return out
    elif len(query) == 1:
      char = query[0]
      if char == this.char:
        return [str(w) for w in this.get_words()]
    elif len(query) > 1:
      char = query[1]
      if char in this.children.keys():
        words = [str(query[0]) + str(w) for w in this.children[char].autocomplete(query[1:])]
        out.extend(words)

    return out

def main():
  arr = ['dog', 'deer', 'deal']
  autocomplete = Autocomplete(arr)
  autocomplete.add_word('dandruf')
  autocomplete.add_word('drone')
  query = 'de'
  print str(autocomplete.get_words())
  print str(autocomplete.autocomplete(query))
  assert ['deal', 'deer'] == autocomplete.autocomplete('de')
  dc = DictionaryAutocomplete()
  dc.add_autocomplete(autocomplete)
  assert ['deal', 'deer'] == dc.autocomplete('de')

if __name__ == "__main__":
  main()
