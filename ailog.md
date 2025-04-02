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

