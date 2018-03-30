#!/usr/bin/env python

# Good morning. Here's your coding interview problem for today.
# This problem was asked by Apple.
#
# Implement a job scheduler which takes in a function f and an integer n,
# and calls f after n milliseconds.

import heapq
import time
current_micros_time = lambda: int(round(time.time() * 1000000))

class Task:
  def __init__(self, entry, micros):
    self.entry = entry
    self.micros = micros
  def run(self):
    if self.entry:
      self.entry()
  def __gt__(self, other):
    return self.micros > other.micros
  def __lt__(self, other):
    return self.micros < other.micros

class Scheduler:
  def __init__(self):
    self.pqueue = []
    pass
  def schedule(self, entry, n):
    time_to_run_at = current_micros_time() + n * 1000
    print str(current_micros_time()) + " Scheduling a task to be run at: " + str(time_to_run_at)
    task = Task(entry, time_to_run_at)
    heapq.heappush(self.pqueue, task)
    # Below should be invoked in a separate thread, which would check the queue
    # each 100 micro seconds or so and run the tasks when appropriate
    self.run()

  def run(self):
    next_task = heapq.heappop(self.pqueue)
    while self.pqueue or next_task is not None:
      if current_micros_time() >= next_task.micros:
        print "Running task at: " + str(current_micros_time())
        next_task.run()
        next_task = None
    print "All tasks finished"

def hello_world():
  print "Running Hello World at: " + str(current_micros_time())
  print "Hello world"

def main():
  s = Scheduler()
  s.schedule(hello_world, 1000)
  pass

if __name__ == "__main__":
    main()
