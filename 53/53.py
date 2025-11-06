import math
# we are interested in the values of get_comb(n, r) that exceed a million, where 23 <= n <= 100

def get_comb(n,r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n-r))

# we know it starts at 23, so n starts at 23
count = 0
for n in range(23, 101):
    for r in range(0, n+1):
        if get_comb(n, r) > 1000000:
            count += 1
print(count)
