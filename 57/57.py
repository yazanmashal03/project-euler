from fractions import Fraction

def get_square_root_expansion(n):
    result = Fraction(1, 2)  # base case: 1/2
    for i in range(2, n+1):
        result = Fraction(1) / (Fraction(2) + result)
    return result

def get_sqroot_iterates(n):
    count = 0
    for i in range(1, n+1):
        result = 1 + get_square_root_expansion(i)
        if len(str(result.numerator)) > len(str(result.denominator)):
            count += 1
    return count

print(get_sqroot_iterates(1000))