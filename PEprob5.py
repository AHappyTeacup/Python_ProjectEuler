from my_timer import timed
from prime_numbers import get_lowest_common_multiple


@timed
def pe_prob_005(n):
    """Find the smallest number that can be devided by all the numbers from
    1 to n

    :param n: Our number
    :return: The smallest number divisible by all numbers from 1 to n
    """
    a, b = n, get_lowest_common_multiple(*list(range(1, (n+1))))
    print b

    while a <= b:
        is_good = True
        for f in range(1, (n+1)):
            if a % f != 0:
                is_good = False
                break
        if is_good:
            return a
        a += n


if __name__ == '__main__':
    print pe_prob_005(20)
