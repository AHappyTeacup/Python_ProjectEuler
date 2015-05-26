import math

primes = [2]
def generatePrime(n):
    if n>100:
        m = int(n**0.5)
    else:
        m = n
    for i in range(3, m, 2):
        p = not any(i%p == 0 for p in primes)
        if p:
            primes.append(i)

def PEprob7(n):
    derp, m = int(3*n*math.log(n))+1, n
    generatePrime(derp)
    while len(primes) < (n+1):
        m=m*2
        generatePrime(m)
    return primes[n-1]

print(PEprob7(10001))