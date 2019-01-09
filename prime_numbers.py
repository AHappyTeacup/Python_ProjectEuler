# sieve of Eratosthenes
def sieve(x):
    """Generates a list of prime numbers using the Sieve of Eratosthenes method

    :param x: The ceiling for the prime number list
    :return: A list of prime numbers less than or equal to x
    """
    if x == 1:
        primes = [2]
    else:
        primes = [2]
        # list, starting at one, jumping in twos.
        ls = list(range(1, x+1, 2))

        # sieve. Indexed 0->x-1
        s = [True]*((x//2)+1)

        s[0] = False

        # Jump up along the list in jumps of ls[i]
        for i in range(1, len(ls)):
            # If a number is Prime...
            if s[i]:
                # j tracks the index number. k tracks the increment value.
                j, k = i, ls[i]
                # Add the corresponding list number to our primes
                primes.append(k)
                while j < x//2:
                    s[j] = False
                    j += k

        primes.sort()
    return primes


def get_unique_factors(num):
    """Get a list of Prime factors of num

    :param num: Our number
    :return: A list of prime factors
    """
    a = num
    m = int(num ** 0.5) if num > 100 else num
    factors = []
    primes = sieve(m)
    # Divide the number by compatible primes until it is 1
    # (or we run out of primes...)
    for p in primes:
        if a % p == 0:
            a = a / p
            factors.append(p)
        if a == 1:
            break
    return factors


def get_prime_factor_counts(num):
    """Get a dictionary of prime factors of num, and the number of times they
    divide num

    :param num: Our number
    :return: A dictionary of primes, to number of times they can divide
    """
    unique_prime_factors = get_unique_factors(num)
    a = num
    prime_factor_counts = {}
    for prime in unique_prime_factors:
        prime_factor_counts[prime] = 0
        divisible = True
        while divisible:
            if a % prime == 0:
                a = a / prime
                prime_factor_counts[prime] += 1
            else:
                divisible = False
    return prime_factor_counts


def get_lowest_common_multiple(*args):
    lcm_factors = {}
    factors_list = []
    for number in args:
        factors_list.append(get_prime_factor_counts(number))
    for factors in factors_list:
        for factor in factors:
            if factor in lcm_factors:
                if lcm_factors[factor] > factors[factor]:
                    continue
            lcm_factors[factor] = factors[factor]

    r_val = 1
    for factor in lcm_factors:
        r_val *= (factor**lcm_factors[factor])
    return r_val
