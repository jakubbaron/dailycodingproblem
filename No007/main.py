#!/bin/python

# Good morning. Here's your coding interview problem for today.
# This problem was asked by Facebook.
# Given the mappin a = 1, b = 2, ... z = 26, and an
# encoded message, count the number of ways it can be decoded
# For example, the message '111' would give 3, since it
# could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that messages are decodable.
# For example, '001' is not allowed.

arr = {}
arr['1']   = 'a'
arr['2']   = 'b'
arr['3']   = 'c'
arr['4']   = 'd'
arr['5']   = 'e'
arr['6']   = 'f'
arr['7']   = 'g'
arr['8']   = 'h'
arr['9']   = 'i'
arr['10']  = 'j'
arr['11']  = 'k'
arr['12']  = 'l'
arr['13']  = 'm'
arr['14']  = 'n'
arr['15']  = 'o'
arr['16']  = 'p'
arr['17']  = 'q'
arr['18']  = 'r'
arr['19']  = 's'
arr['20']  = 't'
arr['21']  = 'u'
arr['22']  = 'v'
arr['23']  = 'w'
arr['24']  = 'x'
arr['25']  = 'y'
arr['26']  = 'z'

def decode_next(msg, current_word):
  print 'msg: ' + str(msg) + ' current word: ' + str(current_word)
  if len(msg) == 0:
    return ''
  if len(msg) == 1 and msg[0] == '0':
    return 'NOPENOPE' #invalid
  if msg[0] != '0':
    current_word += arr[msg[0]]
    decode_next(msg[1:], current_word)
  if len(msg) > 2 and msg[:2] in arr:
    print "Decoding: " + str(msg[:2])
    current_word += arr[msg[:2]]
    decode_next(msg[2:], current_word)
  print current_word

def try_2(msg, current_word, results):
  #print 'msg: ' + str(msg) + ' current dict: ' + str(current_dict)
  if len(msg) == 0:
    results.append(current_word)
    return
  if len(msg) >= 1 and msg[0] in arr:
    try_2(msg[1:], current_word + arr[msg[0]], results)
  if len(msg) >= 2 and msg[:2] in arr:
    try_2(msg[2:], current_word + arr[msg[:2]], results)
  return results


def count_decode_ways(msg, currently_decoded, last_char):
  print "Count decode ways for: " + str(msg)
  print "Currently decoded: " + str(currently_decoded)
  print "Last char: " + str(last_char)
  if len(msg) == 0: #successfully decoded whole message
    return currently_decoded
  # if 0 is at the second char, this isn't valid, thus discard
  decode_next(msg, "")

def main():
  message = '111'
  output = []
  print "Results: " + str(try_2(message, "", output))
  message ='10202223'
  output = []
  print "Results: " + str(try_2(message, "", output))

if __name__ == "__main__":
    main()
