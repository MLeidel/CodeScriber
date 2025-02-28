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

2025-02-21 19:25:27

Sure! Below is a Bash script that performs the tasks you've outlined. This script:

1. Checks if the `gtk-3.0` directory exists in the `~/.config` directory.
2. If the directory exists, it copies `gtk.css` from the current directory to `~/.config/gtk-3.0/`.
3. If the directory does not exist, it creates it and then copies `gtk.css` into it.
4. Finally, it copies `xfce4-panel-tweaks.css` from the current directory to `~/.config/gtk-3.0/`.

### Bash Script: `setup_gtk.sh`

```bash
#!/bin/bash

# Define the target directory
TARGET_DIR="$HOME/.config/gtk-3.0"

# Define the source files
GTK_CSS="gtk.css"
XFCE_TWEAKS_CSS="xfce4-panel-tweaks.css"

# Function to copy a file and handle errors
copy_file() {
    local src="$1"
    local dest="$2"

    if [[ -f "$src" ]]; then
        cp "$src" "$dest"
        if [[ $? -eq 0 ]]; then
            echo "Successfully copied $src to $dest."
        else
            echo "Error: Failed to copy $src to $dest."
            exit 1
        fi
    else
        echo "Error: Source file '$src' does not exist."
        exit 1
    fi
}

# Check if the gtk-3.0 directory exists
if [[ -d "$TARGET_DIR" ]]; then
    echo "Directory '$TARGET_DIR' exists."
else
    echo "Directory '$TARGET_DIR' does not exist. Creating it..."
    mkdir -p "$TARGET_DIR"
    if [[ $? -eq 0 ]]; then
        echo "Successfully created directory '$TARGET_DIR'."
    else
        echo "Error: Failed to create directory '$TARGET_DIR'."
        exit 1
    fi
fi

# Copy gtk.css to the target directory
copy_file "$GTK_CSS" "$TARGET_DIR/"

# Copy xfce4-panel-tweaks.css to the target directory
copy_file "$XFCE_TWEAKS_CSS" "$TARGET_DIR/"

echo "All files have been copied successfully."

exit 0
```

### How to Use the Script

1. **Save the Script:**
   
   Save the above script to a file, for example, `setup_gtk.sh`.

2. **Make the Script Executable:**
   
   Open your terminal and navigate to the directory where you saved `setup_gtk.sh`. Then run:

   ```bash
   chmod +x setup_gtk.sh
   ```

3. **Run the Script:**
   
   Ensure that `gtk.css` and `xfce4-panel-tweaks.css` are present in the current directory. Then execute the script:

   ```bash
   ./setup_gtk.sh
   ```

4. **Script Output:**
   
   The script will output messages indicating whether the `gtk-3.0` directory exists, whether it was created, and whether each file was successfully copied.

### Explanation of the Script

- **Variables:**
  
  - `TARGET_DIR`: The path to the `gtk-3.0` directory within `~/.config`.
  - `GTK_CSS` and `XFCE_TWEAKS_CSS`: The names of the CSS files to be copied.

- **copy_file Function:**
  
  A helper function to copy files and handle potential errors, ensuring that the source file exists before attempting to copy.

- **Directory Check:**
  
  The `if [[ -d "$TARGET_DIR" ]]; then` statement checks if the target directory exists. If not, it creates the directory using `mkdir -p`.

- **Copy Operations:**
  
  The script uses the `copy_file` function to copy both `gtk.css` and `xfce4-panel-tweaks.css` to the target directory.

- **Exit Status:**
  
  The script exits with a status of `0` upon successful completion. If any step fails, it exits with a status of `1`, indicating an error.

### Notes

- Make sure you have the necessary permissions to create directories and copy files within your home directory.
- This script assumes that `gtk.css` and `xfce4-panel-tweaks.css` are present in the directory from which the script is run. If they are located elsewhere, update the `GTK_CSS` and `XFCE_TWEAKS_CSS` variables with the correct paths.

Feel free to customize the script further based on your specific needs!

---

