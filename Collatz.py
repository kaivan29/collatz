#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2017
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------
optimize = [0]*5000001

def collatz_read (r) :
    """
    read an int from r
    r a reader
    return the int
    """
    n = int(r.readline())
    assert n > 0
    return n

# ------------
# collatz_eval
# ------------

def collatz_eval (n) :
    """
    n the end of the range [1, n], inclusive
    return the value that produces the max cycle length of the range [1, n]
    """
    # <your code>
    global optimize
    max = 1
    max_sum = 1
    for i in range(1,n+1):
        sum = 1
        j = i
            
        while j != 1:
            #caching
            if(j < 5000001 and optimize[j]!=0):
                sum = sum + optimize[j]-1
                break
            
            #if not in the cache lets calculate the length
            if j%2 == 0:
                j = int (j >> 1)
                sum+=1
            else:
                j = int((j >> 1) + 1 + j)
                sum+=2
            
        if sum >= max_sum:
            max_sum = sum
            max = i
            
        if i < 5000001:
            optimize[i] = sum

    assert max > 0
    return max


# -------------
# collatz_print
# -------------

def collatz_print (w, m) :
    """
    print an int to w
    w a writer
    m the max cycle length
    """
    assert m > 0
    w.write(str(m) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    t = int(r.readline())
    for _ in range(t) :
        n = collatz_read(r)
        m = collatz_eval(n)
        collatz_print(w, m)