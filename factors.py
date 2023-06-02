#!/usr/bin/python3
import sys
import signal
def handler(signum, frame):
    print("Time's up!")
    raise SystemExit
def factorize(n):
    """
    Factorize a number into a product of two smaller numbers.
    Returns a tuple (p, q), where p and q are the factors.
    If no factorization is possible, returns None.
    """
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return (i, n // i)
    signal.alarm(0)
    return None


def factor_file(filename):
    """
    Factorize each number in a file into a product of two smaller numbers.
    Outputs the factorization for each number in the format n=p*q.
    """
    
    with open(filename, "r") as f:
        for line in f:
            n = int(line.rstrip())
            
            factors = factorize(n)
            if factors is not None:
                p, q = factors
                print(f"{n}={p}*{q}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)
    factor_file(sys.argv[1])
