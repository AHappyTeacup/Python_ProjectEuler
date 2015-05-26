def PEprob5(n):
    a, b, c = n, 1, 0
    for i in range (1, (n+1)):
        b = b*i
        for f in range(1, (n+1)):
            if b%f == 0:
                c=b
    if c > 0:
        b=c
    while a<=b:
        derp = True
        for f in range(1, (n+1)):
            if a%f != 0:
                derp = False
                break;
        if derp == True:
            return a
        a+=n

print(PEprob5(20))