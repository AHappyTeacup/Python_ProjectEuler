def isPrime(n):
    a=primes[-1] 
    while a<n:
        if n%a==0:
            return False
        a=a+1
    return True
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

factors = []
def PEprob3(n):
    if isPrime(n):
        return n
    generatePrime(n)
    m=n
    for p in primes:
        if m%p == 0:
            m = n / p
            factors.append(p)
        if m==0:
            break
    return factors

print(PEprob3(600851475143))