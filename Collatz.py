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
cache = [25,27,54,55,73,97,129,171,
         231,235,313,327,649,654,655,667,703,871,1161,
         2223,2322,2323,2463,2919,3711,6171,10971,13255,
         17647,17673,23529,26623,34239,35497,35655,52527,
         77031,106239,142587,156159,216367,230631,410011,
         511935,626331,837799,1117065,1126015,1501353,1564063,
         1723519,2298025,3064033,3542887,3732423,5649499]

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
    global optimize
    max = 1
    max_sum = 1
    #meta_cache
    winner = collatz_winner(n)
    if (winner != -1):
        return winner
    #calculate if the winner is not in my meta cache
    #I use a lazy cache to caclulate the value outside of my meta cache
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
        #update the number that has the max cycle length
        if sum >= max_sum:
            max_sum = sum
            max = i
        #caching as we go 
        if i < 5000001:
            optimize[i] = sum

    assert max > 0
    return max

# -------------
# collatz_winner
# -------------
def collatz_winner(n):
    global cache
    i=0
    total_len = len(cache)
    if n < 25:
        return -1
    if n > cache[total_len-1]:
        return -1
    while n >= cache[i]:
        i+=1
    return cache[i-1]


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