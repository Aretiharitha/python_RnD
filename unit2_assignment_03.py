__author__ = 'Krish'

notes = '''
These are the kind of questions that are typically asked in written screening tests by companies,
so treat this as practice!

Convert the passed in positive integer number into its prime factorization form.

If number = a1 ^ p1 * a2 ^ p2 ... where a1, a2 are primes and p1, p2 are powers >=1 then we represent that using lists
and tuples in python as [(a1,p1), (a2,p2), ...]

Note that a1 < a2 < ... and p1, p2 etc are all >= 1.

For e.g.
 [(2,1), (5,1)] is the correct prime factorization of 10 as defined above.
 [(5,1), (2,1)] is invalid as the the order is not correct.
 [(2,1), (3,0), (5,1)] is invalid as a prime with power 0 is present in the result.

Notes
0. This problems asks for explicit type checking!
1. Corner case 1 is represented as an empty list: []
2. Non positive numbers should raise a ValueError
3. If the type of number is not int raise a TypeError

Write simple brute force code. No need to write code for generating primes etc.
'''


def generatePrimes(n):
    """Returns a list of prime numbers with length n"""
    primfac = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac


def factorize_number(number):
    res=set()
    try:
        if number <= 1 :
            if number == 1:
                return []
            else:
                raise ValueError
        res = generatePrimes(number)
    except ValueError as ve:
        print("")
    except TypeError as te:
        print("")
    r_t = []
    powe = []
    while res.__len__() > 0 :
        t=res[0]
        v=res.count(t)
        powe.append(v)
        for j in range(v):
            res.remove(t)
        r_t.append(t)
    f=dict(zip(r_t,powe))
    f=list(f.items())
    return f
# you are given the tests here according to the spec, usually you will have to write these yourself from the spec!
def test_factorize_number():
    assert [] == factorize_number(1)
    assert [(2, 1)] == factorize_number(2)
    assert [(2, 1), (5, 1), (601, 1)] == factorize_number(6010)
    assert [(5, 2), (7, 1)] == factorize_number(175)
    assert [(2, 1), (7919, 4)] == factorize_number(7865228921869442)
    try:
        factorize_number(-3)
        assert True, "negative number did not throw"
    except ValueError as ve:
        pass

    try:
        factorize_number(2.3)
        assert True, "float did not throw"
    except TypeError as te:
        pass
