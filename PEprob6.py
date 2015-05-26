def PEprob6(n):
    a, b = 0, 0
    for i in range(1, n+1):
        a += i
        b += (i**2)
    a=(a**2)
    return a-b

print(PEprob6(100))