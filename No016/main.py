#!/usr/bin/env python
# Good morning. Here's your coding interview problem for today.
# This problem was asked by Twitter.
#
# You run an e-commerce website and want to record the last N order ids in a log.
# Implement a data structure to accomplish this, with the following API:
#
# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be
# smaller than or equal to N.
# You should be as efficient with time and space as possible.

class LastLogs:
  def __init__(this, max_size = 10):
    this.__max_size = max_size
    this.__current_id = 0
    this.__log = [None] * this.__max_size

  def record(this, order_id):
    #Put this to a list of logs
    #print "BEFORE Adding", order_id, "current_id", this.__current_id, "array", this.__log
    this.__log[this.__current_id] = order_id
    if this.__current_id + 1 >= this.__max_size:
      this.__current_id = 0
    else:
      this.__current_id += 1
    #print "AFTER Adding", order_id, "current_id", this.__current_id, "array", this.__log

  def get_last(this, i):
    #Transform this to a correct id in an array
    return this.__log[this.__current_id - i]

def main():
  l = LastLogs(max_size = 5)
  l.record(1)
  l.record(2)
  l.record(3)
  l.record(4)
  l.record(5)
  l.record(6)
  l.record(7)
  print l.get_last(1)
  print l.get_last(2)
  print l.get_last(3)
  print l.get_last(4)
  print l.get_last(5)

if __name__ == "__main__":
  main()
