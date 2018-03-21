#!/bin/python

# Good morning. Here's your coding interview problem for today.
# Given a list of numbers, return whether any two sums to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

def brute_force(input, k):
    input_length = len(input)
    for i in range(0, input_length):
        for j in range(0, input_length):
            if i == j:
                continue
            if input[i] + input[j] == k:
                return True
    return False

def one_go(input, k):
    input_length = len(input)
    copy_input = input[:]
    copy_input.sort()
    i = 0
    j = input_length - 1

    if copy_input[i] > k:
        return False

    while j > 0 and copy_input[j] > k:
        j -= 1
    if j == 0:
        return False

    while i < j:
        front_el = copy_input[i]
        back_el = copy_input[j]
        added = front_el + back_el
        if added == k:
            return True
        if front_el + back_el > k:
            j -= 1
        elif front_el + back_el < k:
            i += 1

    return False 

def kosa_try(input, k):
    s = set()
    for i in input:
        if k - i in s:
            return True
        s.add(i)
    return False

def main():
    from datetime import datetime
    import random


    input = [10, 15, 3, 7]
    k = 17

    max_range = 10000
    input = random.sample(range(1, max_range), max_range/2)
    k = random.randint(1, max_range)

    runs = 100
    print "Performing: " + str(runs) + " runs"
    print str(max_range/2) + " of elements from range (1, " + str(max_range) + ")"

    start_time = datetime.now()
    for i in range(0, runs):
        output=brute_force(input, k)
    time_elapsed = datetime.now() - start_time

    per_run = (time_elapsed.microseconds/(runs * 1.0))
    print "Brute force: Per run: " + str(per_run) + "us"

    if output:
        print "Brute force: Yup"
        #print "Given input " + str(input) + " has at least two elements adding up to: " + str(k)
    else:
        print "Brute force: Nope"

    start_time = datetime.now()
    for i in range(0, runs):
        output=one_go(input, k)
    time_elapsed = datetime.now() - start_time

    per_run = (time_elapsed.microseconds/(runs * 1.0))
    print "One go: Per run: " + str(per_run) + "us"

    if output:
        print "One go: Yup"
        #print "Given input " + str(input) + " has at least two elements adding up to: " + str(k)
    else:
        print "One go: Nope"

    start_time = datetime.now()
    for i in range(0, runs):
        output=kosa_try(input, k)
    time_elapsed = datetime.now() - start_time

    per_run = (time_elapsed.microseconds/(runs * 1.0))
    print "Kosa try: Per run: " + str(per_run) + "us"

    if output:
        print "Kosa try: Yup"
        #print "Given input " + str(input) + " has at least two elements adding up to: " + str(k)
    else:
        print "Kosa try: Nope"

if __name__ == "__main__":
    main()
