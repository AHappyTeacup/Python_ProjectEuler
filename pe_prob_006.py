from my_timer import timed


@timed
def pe_prob_006(n):
    """Find the difference between the sum of the squares of the first n 
    natural numbers, and the square of the sum of the first n natural numbers.
    
    :param n: 0ur amount of natural numbers to calculate with
    :return: The difference of the sum of the squares, and the square of the 
        sum of the first n natural numbers
    """
    a, b = 0, 0
    for i in range(1, n+1):
        a += i
        b += (i**2)
    a = (a**2)
    r_val = a-b
    return r_val


if __name__ == '__main__':
    print pe_prob_006(100)
