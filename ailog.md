2025-01-27 19:57:59

Sure! Here's a simple Python script that calculates the factorial of a number:

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")
```

When you run this code, it will output:

```
The factorial of 5 is 120
```

---

2025-01-27 19:58:35

Sure! Here's a simple Python script that calculates and prints the Fibonacci sequence up to a specified number of terms:

        def fibonacci(n):
            sequence = []
            a, b = 0, 1
            while len(sequence) < n:
                sequence.append(a)
                a, b = b, a + b
            return sequence
        
        number_of_terms = 10
        fib_sequence = fibonacci(number_of_terms)
        print(f"Fibonacci sequence up to {number_of_terms} terms: {fib_sequence}")

**Output:**

```
Fibonacci sequence up to 10 terms: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

This script defines a `fibonacci` function that generates the Fibonacci sequence up to `n` terms. It then calls this function with `number_of_terms` set to 10 and prints the resulting sequence.

---

2025-01-27 19:59:34

Certainly! Here's a simple Python script that generates a list of the first 10 Fibonacci numbers and prints them:

<code>
def generate_fibonacci(n):
    """Generate a list of the first n Fibonacci numbers."""
    fib_sequence = []
    a, b = 0, 1
    while len(fib_sequence) < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

\# Number of Fibonacci numbers to generate
count = 10
fibonacci_numbers = generate_fibonacci(count)

print(f"The first {count} Fibonacci numbers are:")
print(fibonacci_numbers)
</code>

**Output:**

```
The first 10 Fibonacci numbers are:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

**Explanation:**

1. **Function `generate_fibonacci(n)`**:
    - Initializes an empty list `fib_sequence` to store Fibonacci numbers.
    - Uses two variables `a` and `b` starting at 0 and 1, the first two numbers in the Fibonacci sequence.
    - Appends `a` to the list and then updates `a` and `b` to the next two numbers in the sequence.
    - Continues this process until the list contains `n` numbers.

2. **Generating and Printing**:
    - Sets `count` to 10, meaning we want the first 10 Fibonacci numbers.
    - Calls the `generate_fibonacci` function with `count` and stores the result in `fibonacci_numbers`.
    - Prints the list of Fibonacci numbers.

You can run this script in any Python environment to see the output. Feel free to modify the `count` variable to generate a different number of Fibonacci numbers!

---

