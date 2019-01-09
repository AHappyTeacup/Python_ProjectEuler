from my_timer import timed


@timed
def pe_prob_001(n):
    """Find the sum of all multiples of 3 or 5 below n

    :param n: Our number
    :return: The sum of all multiples of 3 or 5 below n
    """
    a = 0
    f = []
    for i in range(0, n):
        if i % 3 == 0 or i % 5 == 0:
            f = f+[i]
    for x in f:
        a = a+x
    return a


if __name__ == '__main__':
    print pe_prob_001(1000)
