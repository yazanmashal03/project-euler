# I am thinking of using this recursive form for calculating the E[I_i], and then taking the sum of the E[I_i] for all i from 1 to n.

def get_expectation_i(a, b, i, n):
    if i == n - 1:
        return 1
    else:
        return (1/2)**(n-i-1)

def get_f(a, b, n=100):
    return 0

print(get_f(1, 2))
