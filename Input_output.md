## What is I/O?
* Input: Data or information that the program receives from the user, file, or other sources.
* Output: Data or information that the program produces and sends to the screen, a file, or another destination.
* Think of I/O as a conversation between the user and the program:

* Input is like the user asking a question or giving a command.
* Output is the program responding with an answer or performing an action based on that command.

## 1. Basic Input with input()
In Python, the input() function is used to get input from the user.

```
name = input("Enter your name: ")  ->Input
print("Hello, " + name + "!")  -> Output

```

## 2. Processing Input
Often, input data needs to be processed or converted. By default, input() returns a string, so if you're dealing with numbers, you have to convert them.

```
age = input("Enter your age: ")  # This is a string
age = int(age)  # Convert the string to an integer
print("Next year, you will be", age + 1, "years old.")

```

## 3. Output with print()
The print() function sends information to the screen, allowing the user to see results.

### Example: Output with Formatting
You can format the output to make it more readable:

```
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello, {name}. Next year, you will be {age + 1} years old.")

```
## 4. Working with Files (File I/O)
Apart from user input, programs often need to read from or write to files. This is called File I/O.

Reading from a file: Input from a file.
Writing to a file: Output to a file.

### Example: Writing to a File

```
# Opening a file to write data (output)
with open('output.txt', 'w') as file:
    file.write("This is a line of text.\n")
    file.write("This is another line of text.\n")

```

* open() opens the file. The 'w' mode stands for "write" mode, which means the file will be written to (and created if it doesn’t exist).
* write() writes data to the file.
* Using with ensures the file is properly closed after writing.

### Example: Reading from a File

```
# Opening a file to read data (input)
with open('output.txt', 'r') as file:
    content = file.read()

print(content)  # Output: Print the file's content

```

* 'r' mode is for reading.
* read() reads the entire content of the file.
