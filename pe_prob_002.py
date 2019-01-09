from my_timer import timed
memo = {0: 1, 1: 1}


def fibm(n):
    """Return the n'th Fibonacci number.
    Uses a global dict to lessen computation

    :param n: The Fibonacci term we want
    :return:  The n'th Fibonacci number
    """
    if n not in memo:
        # A Fibonacci number is the sum of the previous two Fibonacci numbers
        memo[n] = fibm(n-1) + fibm(n-2)
    return memo[n]


@timed
def pe_prob_002(n):
    """Find the sum of all even valued fibonnaci terms below n

    :param n: Our number
    :return: The sum of all even-valued fibonacci numbers below n
    """
    a, i = 0, 0
    # For all Fib numbers less than n
    while fibm(i) < n:
        # If the number is even
        if fibm(i) % 2 == 0:
            # sum it
            a = a+fibm(i)
        i = i+1
    return a


if __name__ == '__main__':
    print pe_prob_002(4000000)
