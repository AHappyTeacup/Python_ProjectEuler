def PEprob4(n):
    a, c, e = (10**n)-1, 0, 0
    while a > ((10**(n-1))-1):
        b=(10**n)-1
        while b > ((10**(n-1))-1):
            c = a*b
            d = str(c)
            if d[0] == d[-1]:
                if d[1] == d[-2]:
                    if d[2] == d[-3]:
                        if c>e:
                            e=c
            b=b-1
        a=a-1
    return e

print(PEprob4(3))