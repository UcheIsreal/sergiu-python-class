def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_term = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_term)
    return fib_sequence

N = 10
fibonacci_terms = fibonacci_sequence(N)
print(fibonacci_terms)
