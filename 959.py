import numpy as np

def asym_walk(n):
    return np.random.choice([-1, 1], size=n)

# define a main function
def main():
    n = 1000
    walks = asym_walk(n)
    print(walks)

if __name__ == "__main__":
    main()