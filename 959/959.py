from scipy.special import comb

def get_f(a, b, n=100):
    sum = 0
    for i in range(1, n):
        sum += (1/((a+b)*i)) * comb((a+b)*i, a*i, exact=False) * (2 ** (-(a+b)*i))
    return 1 - sum

print(get_f(1, 2))
