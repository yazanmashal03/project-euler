from itertools import combinations

def is_prime(n): 
    if n < 2: 
        return False 
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0: 
            return False 
    return True

def positions_subsets(num_digits: int):
    # all non-empty subsets of {0,1,...,num_digits-1}
    idx = range(num_digits)
    for r in range(1, num_digits + 1):
        for comb in combinations(idx, r):
            yield comb

def family_for_mask(p: int, mask: tuple[int, ...]) -> list[int]:
    s = list(str(p))
    # the digits at masked positions in the base number must be equal
    first = s[mask[0]]
    if any(s[i] != first for i in mask):
        return []

    fam = []
    for d in map(str, range(10)):
        # no leading zero
        if 0 in mask and d == '0':
            continue
        # if last digit is in mask, only try 1,3,7,9
        if len(s) - 1 in mask and d not in ('1','3','7','9'):
            continue

        t = s[:]
        for i in mask:
            t[i] = d
        n = int(''.join(t))
        if is_prime(n):
            fam.append(n)
    return fam

def smallest_prime_in_eight_family(limit: int = 2_000_000) -> int | None:
    # simple prime
    for n in range(11, limit, 2):  # start odd ≥ 11
        if not is_prime(n):
            continue
        L = len(str(n))
        # heuristic: at least one repeated digit must exist to make large families likely
        digits = str(n)
        if len(set(digits)) == L:
            continue
        for mask in positions_subsets(L):
            fam = family_for_mask(n, mask)
            if len(fam) >= 8:
                return min(fam)
    return None

if __name__ == "__main__":
    print(smallest_prime_in_eight_family())
