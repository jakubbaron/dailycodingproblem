#!/usr/bin/env python

def benchmark(method, name, runs, input, k):
    import time
    current_micro_time = lambda: int(round(time.time() * 1000000))
    start_time = current_micro_time()
    for i in range(0, runs):
        output=method(input, k)
    time_elapsed = current_micro_time() - start_time

    per_run = (time_elapsed/(runs * 1.0))
    print str(name) + ": Per run: " + str(per_run) + "us"

    if output:
        print str(name) + " output: " + str(output)
    else:
        print str(name) + " no output"


def main():
  pass

if __name__ == "__main__":
  main()
