from my_timer import timed
from prime_numbers import sieve
import math


@timed
def pe_prob_007(n):
    """Return the n'th prime number
    
    :param n: The prime we want
    :return: The n'th prime number
    """
    upper_prime_bound = int(3*n*math.log(n))+1
    primes = sieve(upper_prime_bound)
    while len(primes) < (n+1):
        upper_prime_bound = upper_prime_bound*2
        primes = sieve(upper_prime_bound)
    return primes[n-1]


if __name__ == '__main__':
    print pe_prob_007(10001)
