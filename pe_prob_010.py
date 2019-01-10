from my_timer import timed
from prime_numbers import sieve


@timed
def pe_prob_010(x):
    """Get the sum of all the primes below x.

    :param x: Our number
    :return: The sum of all the primes under x
    """
    r_val = 0
    primes = sieve(x)
    for i in primes:
        r_val += i
    return r_val


if __name__ == '__main__':
    print pe_prob_010(2000000)
g