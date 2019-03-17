from my_timer import timed


def colatz_seq(n):
    """Get the next element in the Colatz Sequence when given a number 'n'

    :param n: A positive integer
    :return: A positive Integer
    """
    x = n / 2 if n % 2 == 0 else 3 * n + 1
    return x


@timed
def pe_prob_013(num):
    """Find the number below 'num' which generates the longest colatz chain back to 1.
    This code operates on the assumption that there is indeed one single number in
    the range that produces a sequence longer than any other number in the range.

    :param num: The upper bound of the range
    :return: An integer - the number in the range which produces the longest COlatz sequence.
    """
    # A dictionary of integers, to lists of incomplete Colatz sequences.
    colatz_chain = {}
    # list of most recently found next elements.
    next_elems = []

    # Set up for main loop
    for i in range(2, num):
        # Get the next Colatz element.
        next_elem = colatz_seq(i)
        # Initiate a list of the Colatz sequence for this starting number
        colatz_chain[i] = [next_elem]
        if next_elem == 1:
            # Remove it from the dictionary as we have hit one.
            del(colatz_chain[i])
        else:
            # Add it the list of most recently found next elements
            next_elems.append(next_elem)

    # Main loop - iterate until colatz_chain has only one element.
    while len(colatz_chain) != 1:
        # Check the most recently generated list of recent colatz numbers.
        for elem in next_elems:
            # Remove them from the Colatz chain if found.
            # If a number appears in another number's Colatz sequence,
            # the second  number's sequence must be longer, by dint of
            # containing the entire first numbers sequence in addition.
            if elem in colatz_chain.keys():
                del(colatz_chain[elem])

        print len(colatz_chain)
        # A new list of most recently found next elements.
        next_elems = []
        # For each of the remaining starting numbers, calculate the
        # next element in their Colatz sequence.
        for key in colatz_chain.keys():
            next_elem = colatz_seq(colatz_chain[key][-1])
            if next_elem == 1:
                # Remove it from the dictionary as we have hit one.
                del(colatz_chain[key])
            else:
                # Add it the list of most recently found next elements
                colatz_chain[key].append(next_elem)
                next_elems.append(next_elem)

    # There is now one element left.
    return colatz_chain.keys()[0]


if __name__ == "__main":
    print pe_prob_013(1000000)
