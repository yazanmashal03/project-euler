from string import printable

with open("59/0059_cipher.txt", "r") as f:
    data = [int(x) for x in f.read().strip().split(",")]

def decrypt_with_key(nums, key_bytes):
    out = []
    for i, n in enumerate(nums):
        out.append(n ^ key_bytes[i % 3])
    return bytes(out)

def is_printable(bs):
    try:
        s = bs.decode("utf-8", errors="strict")
    except UnicodeDecodeError:
        return False
    return all(ch in printable or ch == "\n" for ch in s)

COMMON = [" the ", " and ", " to ", " of ", " in ", " that ", " is ", " it ", " as ", "with", "for", "was", "are"]

best = None

for a in range(97, 123):
    for b in range(97, 123):
        for c in range(97, 123):
            key = bytes([a, b, c])
            pt = decrypt_with_key(data, key)
            if not is_printable(pt):
                continue
            s = pt.decode("utf-8")
            # simple English-likeness score
            word_hits = sum(s.lower().count(w) for w in COMMON)
            letters = sum(ch.isalpha() for ch in s)
            spaces = s.count(" ")
            punctuation_bad = sum(ch in "{}[]|~`" for ch in s)  # rare in normal prose
            score = 5*word_hits + 0.01*letters + 0.02*spaces - 2*punctuation_bad

            if (best is None) or (score > best[0]):
                best = (score, key, s)

# report best candidate
score, key, plaintext = best
ascii_sum = sum(ord(ch) for ch in plaintext)

print(f"Key: {key.decode('ascii')}")
print("Decrypted message:\n")
print(plaintext)
print("\nSum of ASCII values:", ascii_sum)
