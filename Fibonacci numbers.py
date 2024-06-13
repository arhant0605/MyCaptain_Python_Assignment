def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n+2:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence[2:n+2]

 
n_terms = int(input("Enter no of fibonacci terms needed :"))
if n_terms <= 0:
        raise ValueError("The number of terms must be a positive integer.")
fibonacci_result = generate_fibonacci(n_terms) 
print(f"the first {n_terms} fibonacci numbers are: {fibonacci_result}")
        
