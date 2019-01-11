from my_timer import timed


def unpack_grid(raw_grid):
    """Convert an unformatted grid of single digit unspaced numbers into a 
    list of ints
    
    :param raw_grid: An unformatted grid of numbers
    :return: A list of ints
    """
    number_list = []
    raw_grid = raw_grid.split("\n")
    for row in raw_grid:
        row = row.strip()
        if row is not '':
            for number in row:
                number_list.append(int(number))

    return number_list


@timed
def pe_prob_008(my_grid_raw, num):
    """Get the greatest product of num consecutive digits in my_grid_raw
    
    :param my_grid_raw: A grid of sinbgle digint unspaced numbers as a plain 
        string
    :param num: The number of consecutive digits
    :return: The greatet product of num consecutive digits in my_grid_raw
    """
    number_list = unpack_grid(my_grid_raw)
    product = 1
    r_val = 0
    digit_count = 0
    for i in range(0, len(number_list)):
        if number_list[i] != 0:
            if digit_count < num:
                product *= number_list[i]
                digit_count += 1
            else:
                product /= number_list[i-num]
                product *= number_list[i]
                if product > r_val:
                    r_val = product
        else:
            product = 1
            digit_count = 0

    return r_val

if __name__ == '__main__':
    grid = """
    73167176531330624919225119674426574742355349194934
    96983520312774506326239578318016984801869478851843
    85861560789112949495459501737958331952853208805511
    12540698747158523863050715693290963295227443043557
    66896648950445244523161731856403098711121722383113
    62229893423380308135336276614282806444486645238749
    30358907296290491560440772390713810515859307960866
    70172427121883998797908792274921901699720888093776
    65727333001053367881220235421809751254540594752243
    52584907711670556013604839586446706324415722155397
    53697817977846174064955149290862569321978468622482
    83972241375657056057490261407972968652414535100474
    82166370484403199890008895243450658541227588666881
    16427171479924442928230863465674813919123162824586
    17866458359124566529476545682848912883142607690042
    24219022671055626321111109370544217506941658960408
    07198403850962455444362981230987879927244284909188
    84580156166097919133875499200524063689912560717606
    05886116467109405077541002256983155200055935729725
    71636269561882670428252483600823257530420752963450
    """
    print pe_prob_008(grid, 13)
