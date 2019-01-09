from my_timer import timed
from prime_numbers import sieve, get_unique_factors


@timed
def pe_prob_003(num):
    """Get the largest prime factor of num

    :param num: Our number
    :return: The largest prime factor
    """
    factors = get_unique_factors(num)

    return factors[-1] if factors else 1


if __name__ == '__main__':
    print pe_prob_003(600851475143)
