def sieve_of_eratosthenes(n: int) -> List[int]:
    """
    Generates all prime numbers up to n using the Sieve of Eratosthenes.
    Time Complexity: O(n log log n)
    """
    if n < 2:
        return []

    # Initialize a boolean list (sieve) where True means the number is prime
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    p = 2
    while (p * p) <= n:
        # If is_prime[p] is not changed, then it is a prime
        if is_prime[p]:
            # Update all multiples of p starting from p*p
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
        
    # Extract the prime numbers from the boolean list
    primes = [i for i, is_p in enumerate(is_prime) if is_p]
    return primes

# Example Usage:
# print(sieve_of_eratosthenes(30)) 
# Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
