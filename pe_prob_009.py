from my_timer import timed


@timed
def pe_prob_009():
    """Fomd the product of a pytagorean triplet who's sum is 1000
    A pythagorean triplet is a set of thee natural numbers a, b, c for which
    the sum of the squares of a and b equals the square of c.
    0 <= a < b < c, and a**2 + b**2 = c**2
    
    We want the product abc for the pythagorean triplet a + b + c = 1000
    
    :return: the product abc
    """
    for c in range(3, 1000):
        for a in range(0, c-1):
            b = 1000 - (a+c)
            if a**2 + b**2 == c**2:
                return a*b*c
    return "Failure"


if __name__ == '__main__':
    print pe_prob_009()
