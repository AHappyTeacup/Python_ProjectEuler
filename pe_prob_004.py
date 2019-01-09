from my_timer import timed


@timed
def pe_prob_004(n):
    """Get the largest palindrome product of two n-digit numbers
    A palindromic number reads the same both ways.

    Since it's pretty straightforward to see a large number will be the
    product of large numbers, we'll start large.
    This ended up being pointless as we continue to cycle through everything,
    so this whole thing is needlessly complex, and a nightmare to read a year
    later without comments.


    :param n: The number of digits we are working with
    :return: The largest palindrome product of two n-digit numbers
    """
    # a is the largest n-digit number
    # c and e are set to 0. c will track current products,
    # e will track the final value
    a, c, e = (10**n)-1, 0, 0
    # Lower a with each loop
    while a > ((10**(n-1))-1):
        # Like a, b will the largest n-digit number
        b = (10**n)-1
        # lower b with each loop
        while b > ((10**(n-1))-1):
            # c is the current product
            c = a * b
            # d is a string of c so we can pick up each digit as a character
            d = str(c)
            # pare across half of the string
            for i in range(len(d)//2+1):
                # if the characters across it are equal
                if d[i] == d[-(i+1)]:
                    # and we made it to the halfway mark without breaking
                    if i == len(d)//2:
                        # Check if this product is larger than our largest
                        if c > e:
                            # Set the largest found palindromic product
                            e = c
                else:
                    # Break if characters don't match
                    break
            b = b-1
        a = a-1
    return e


if __name__ == '__main__':
    print(pe_prob_004(3))
