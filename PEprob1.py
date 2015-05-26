def PEprob1(n):
    a=0
    f = []
    for i in range (0, n):
        if i%3 == 0 or i%5 == 0:
            f=f+[i]
    for x in f:
        a=a+x
    return a