# finbonnaci 
def get_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return get_fibonacci(n-1) + get_fibonacci(n-2)

# sum of even fibonacci numbers below 4 million
sum = 0
i = 0
while get_fibonacci(i) < 4000000:
    if get_fibonacci(i) % 2 == 0:
        sum += get_fibonacci(i)
    i += 1
print(sum)