#!/bin/python

# Good morning. Here's your coding interview problem for today.
# Given a list of numbers, return whether any two sums to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

def brute_force(input, k):
    input_length = len(input)
    for i in range(0, input_length):
        for j in range(i+1, input_length):
            if input[i] + input[j] == k:
                return True
    return False

def one_go(input, k):
    copy_input = input[:] #https://stackoverflow.com/a/2612990
    copy_input.sort()
    i = 0
    j = len(input) - 1

    if copy_input[i] > k:
        return False

    while i < j:
        added = copy_input[i] + copy_input[j]
        if added == k:
            return True
        if added > k:
            j -= 1
        else:
            i += 1

    return False

def kosa_try_set(input, k):
    s = set()
    for i in input:
        if k - i in s:
            return True
        s.add(i)
    return False

def kosa_try_dict(input, k):
    s = {}
    for i in input:
        if k - i in s:
            return True
        s[i] = ""
    return False

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
        print str(name) + ": Found a pair"
    else:
        print str(name) + ": Pair not found"


def main():
    import random

    max_range = 10000
    input = random.sample(range(1, max_range), max_range/2)
    k = random.randint(1, max_range)
    runs = 100
    print "Performing: " + str(runs) + " runs"

    print str(max_range/2) + " of elements from range (1, " + str(max_range) + ")"

    benchmark(brute_force,   "Brute force", runs, input, k)
    benchmark(one_go,        "One go", runs, input, k)
    benchmark(kosa_try_set,  "Kosa try set", runs, input, k)
    benchmark(kosa_try_dict, "Kosa try dict", runs, input, k)

if __name__ == "__main__":
    main()
