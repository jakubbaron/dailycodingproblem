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

def decode_ways(msg, current_word=""):
  output = []
  if len(msg) == 0:
    return [current_word]
  if len(msg) >= 1 and msg[0] in arr:
    output.extend(decode_ways(msg[1:], current_word + arr[msg[0]]))
  if len(msg) >= 2 and msg[:2] in arr:
    output.extend(decode_ways(msg[2:], current_word + arr[msg[:2]]))
  return output

def main():
  message = '111'
  print "Message: " + str(message)
  print "Results: " + str(decode_ways(message))
  print "Ways: " + str(len(decode_ways(message)))

  message ='10202223'
  print "Message: " + str(message)
  print "Results: " + str(decode_ways(message))
  print "Ways: " + str(len(decode_ways(message)))

if __name__ == "__main__":
    main()
