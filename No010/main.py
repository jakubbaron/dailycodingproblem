#!/usr/bin/env python

# Good morning. Here's your coding interview problem for today.
# This problem was asked by Apple.
#
# Implement a job scheduler which takes in a function f and an integer n,
# and calls f after n milliseconds.

import heapq
import time
import threading

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

class Scheduler(threading.Thread):
  def __init__(self):
    self.queue = []
    self.mutex = threading.Lock()
    self.run_scheduler = True
    super(Scheduler, self).__init__()

  def toggle_run_scheduler(self):
    self.run_scheduler = not self.run_scheduler
    if self.run_scheduler:
      self.run()

  def run(self):
    while self.run_scheduler:
      if not self.queue:
        time.sleep(0.0001) #sleep 100 microseconds
        continue
      if current_micros_time() >= self.queue[0].micros: #What if there are more tasks that were to be run now?
        while self.queue and current_micros_time() >= self.queue[0].micros:
          self.mutex.acquire()
          next_task = heapq.heappop(self.queue)
          next_task.run()
          self.mutex.release()
      time.sleep(0.0001) #sleep 100 microseconds
    print "Scheduler has been stopped"

  def schedule(self, entry, n):
    time_to_run_at = current_micros_time() + n * 1000
    print str(current_micros_time()) + " Scheduling a task to be run at: " + str(time_to_run_at)
    task = Task(entry, time_to_run_at)

    self.mutex.acquire()
    heapq.heappush(self.queue, task)
    self.mutex.release()

def hello_world():
  print "Running Hello World at: " + str(current_micros_time())
  print "Hello world"

def hello_world2():
  print "Running Hello World 2 at: " + str(current_micros_time())
  print "Hello world 2"

def main():
  s = Scheduler()
  s.start()
  s.schedule(hello_world, 1000)
  time.sleep(2)
  s.schedule(hello_world2, 500)
  s.schedule(hello_world2, 5000)
  s.schedule(hello_world, 1000)
  time.sleep(10)
  s.toggle_run_scheduler()
  s.join()

if __name__ == "__main__":
  main()
