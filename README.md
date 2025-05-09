# Introduction to Programming With Python

Programming is the process of telling the computer what to do. These compiled instructions to the computer are called programs. We almost always use a programming language to write these set of instructions. A programming language is how we write code, what keywords we use, to tell the computer what to do. In this short course you will learn how to write instructions to a computer with a programming language called Python. 

## How to take this course

1. Review yesterday's homework. Fill in the progress report.
2. Read the day's content. Watch the videos in the additional resources. Make effort to understand the work.
3. Come to my desk so I can explain the course's content to you.
4. Do the day's homework.

# Monday

## Arithmetic and Operators

Arithmetic deals with numerical operations like addition, subtraction, multiplication, and division. Like we do with calculators we can ask the computer to perform some arithmetic operations, for example, we can write the following in a python file:

💡: _A python file ends with the extension "py"_

```python3
1 + 1
3 * 9
10 / 2
7 - 4
```

💡 _Instead of using the obelus (÷), we use the slash (/) to perform division. We also use use an asterick (*) for multiplication instead of the times sign (×)._

If we were to run the python file with those operations, there will be no output. In order to see output on the screen we'll introduce a `print` statement. Don't worry about what it is and how it works for now, the only thing that you need to know is that it prints output on the terminal.

💡 _To run a Python file look for a play button usually found on the top right corner of your IDE or write python3 [filename] and press enter._

The above statements can be rewritten as such:

```python3
print(1 + 1)
print(3 * 9)
print(10 / 2)
print(7 - 4)
```

💡 _Think of a statement as a complete instruction that could be understood by the computer. This is similar to how we define a sentence: a set of words that is complete in itself._

## Variables

To be able to perform advanced operations and write much more clean operations that others understand we need to have variables just like we do in mathematics. Think of a variable as a named storage that holds or remembers a value.

With this new knowledge of variables we can perform more complex calculations like the following:

```python
x = 3
print(x - 1)
```

In the above code `x` will be substituted with `3` and the result will be `2`.

💡 *We use the equals sign (`=`) to assign a value to a variable. This is called assignment. It does not mean "equals" like it does in math.*

You can create as many variables as you want:

```python
a = 10
b = 5
print(a + b)
print(a * b)
```

Here, `a` stores the value 10, and `b` stores the value 5. The computer remembers those values and uses them whenever `a` or `b` appear in a calculation.

Variables can also be updated. The value stored inside them can change:

```python
x = 7
print(x)

x = 4
print(x)
```

💡 *Variables store only one value at a time. When you assign a new value to the same variable, it replaces the old one.*

We can even use one variable to help define another:

```python
length = 8
width = 3
area = length * width
print(area)
```

Here, `area` will store the result of multiplying `length` and `width`, which is `24`. This is the foundation of how we build more powerful programs — by breaking them into understandable steps with variables.

💡 *Variable names should be descriptive. Instead of calling everything `x` or `a`, use names like `score`, `temperature`, or `age`.*

But keep in mind: there are some rules for naming variables:

- Variable names can’t have spaces.
- They must start with a letter or underscore (`_`), not a number.
- They can only contain letters, numbers, and underscores.
- They are case-sensitive. `score` and `Score` are two different variables.

Here are some good and bad examples:

✅ Good:

```python
player_score = 15
totalAmount = 20
_name = "Alex"
```

❌ Bad:

```python
1st_place = 10      # starts with a number
total-amount = 20   # uses a dash, which is not allowed
my score = 100      # contains a space
```

💡 *Pick variable names that make your code easier to read. Think of them like labels on storage boxes.*

By using variables, we can now write code that remembers values, performs calculations with those values, and changes them as needed.

### Additional Resources
[Variables Short](https://youtu.be/ylhcZZ7O3Tk)

# Tuesday

## Input and Strings

So far, we’ve written programs where we give the computer information ahead of time. But most programs need to talk to people — and that means getting input from a user. We can do that in Python using the `input()` function.

Let’s start with a simple example where the computer asks for your name:

```python
name = input("What is your name? ")
print(name)
```

When this code runs, the computer will print the question: *What is your name?* and wait for you to type something. Whatever you type gets stored in the variable `name`. Then, the program prints that name back to you.

💡 *The `input()` function pauses the program and waits for the user to type something and press Enter. Whatever the user types is treated as a string.*

### What is a String?

A **string** is any sequence of characters — letters, numbers, spaces, punctuation — all treated as text. Strings are always written inside quotation marks:

```python
"hello"
"123"
"Python is fun!"
```

Even though `"123"` looks like a number, it’s actually a string because it’s inside quotes. Strings can be stored in variables just like numbers:

```python
greeting = "Hello"
language = "Python"
print(greeting)
print(language)
```

💡 *You can use either single quotes (`'Python'`) or double quotes (`"Python"`) to define a string. Just make sure they match.*

### Using Input and Strings Together

We can make the program a bit more friendly by combining strings with variables. For example:

```python
name = input("What is your name? ")
print("Hello, " + name + "!")
```

If the user types `Sam`, the output will be:

```
Hello, Sam!
```

This is called **string concatenation** — joining strings together using the `+` sign. In the example above, we're joining `"Hello, "`, the value of `name`, and `"!"`.

💡 *You can only use `+` to join strings together. You can’t add a string and a number without converting one to the other first.*

Here’s a slightly longer example combining everything we've learned so far:

```python
name = input("What is your name? ")
age = input("How old are you? ")
print("Nice to meet you, " + name + ". You are " + age + " years old.")
```

Even though `age` is a number in real life, it is treated as a string here because `input()` always gives us strings. We'll learn how to turn it into a number later.

### Additional resources

- [String methods](https://youtu.be/f4_ZPwvKF5g)
- [String slice](https://youtu.be/COWxTAPkr_k)


## Functions

Sometimes we want to perform the same action multiple times in different places. Instead of repeating ourselves, we can **define a function** and use it whenever we want.

This follows the rule of **DRY**: *Don’t Repeat Yourself.*

Here’s an example of a function:

```python
def greet():
    print("Hello!")
    print("Welcome to our program!")
```

Now if we want to greet someone multiple times, we just call the function:

```python
greet()
greet()
```

💡 *A function is like a named action. You define it once, and then the computer knows how to perform it.*

We can also create functions that take in values (parameters):

```python
def greet(name):
    print("Hello, " + name)
```

```python
greet("Alice")
greet("Bob")
```

## Additional resources

- [Functions short](https://youtu.be/lGS6O47debI)
- [Return values short](https://youtu.be/AetGXMcNU3M)

# Wednesday

## Loops

Loops help us repeat actions.

### While Loop

Let’s say a cat has to meow 3 times. You could write:

```python
print("meow")
print("meow")
print("meow")
```

But what if it needed to meow 20 times? Repeating `print("meow")` over and over isn't very smart.

That’s where a **while loop** comes in:

```python
i = 3
while i != 0:
    print("meow")
    i = i - 1
```

### For Loop

A for loop is another kind of loop. It’s best understood when we talk about **lists**.

Let’s say we have:

```python
for i in [0, 1, 2]:
    print("meow")
```

This does the same thing — prints "meow" three times.

Instead of writing out the list manually, we can use `range()`:

```python
for i in range(3):
    print("meow")
```

Even better, since we don’t use `i`, we can write:

```python
for _ in range(3):
    print("meow")
```

💡 *The underscore `_` is used when we don’t care about the variable.*

### Validating Input With Loops

Sometimes, we want to ask the user for input until they give us a valid one:

```python
while True:
    n = int(input("What's n? "))
    if n > 0:
        break
```

Then we can use that number in a loop:

```python
for _ in range(n):
    print("meow")
```

Putting this all into functions:

```python
def main():
    meow(get_number())

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()
```

### Additional resources

- [For loops short](https://youtu.be/iTRBRXOMzeM)
- [While loops short](https://youtu.be/CYobbeiGgp8)

## Lists

In Python, a list is a way to store multiple values in a single variable. Think of it like a container — or even like a shopping list. Each item is stored in a specific order, and we can go in and get exactly what we want.

Here’s how you make a simple list:

```python
grocery_list = ["milk", "bread", "eggs"]
```

This list has three items in it: `"milk"`, `"bread"`, and `"eggs"`.

### Getting Values From a List

Each item in a list has a position, starting from 0. That means:

- `"milk"` is at position **0**
- `"bread"` is at position **1**
- `"eggs"` is at position **2**

We can get an item from the list like this:

```python
print(grocery_list[0])  # prints milk
print(grocery_list[2])  # prints eggs
```

💡 *The position number is called the index. In Python, indexes always start at 0.*

### Setting Values in a List

You can also change an item in a list by setting a new value at a certain index:

```python
grocery_list[1] = "butter"
print(grocery_list)  # now it's ["milk", "butter", "eggs"]
```

We changed the second item from `"bread"` to `"butter"`.

### Getting the Length of a List

Python gives us a simple function to count how many items are in a list. It’s called `len()`, short for “length”:

```python
print(len(grocery_list))  # prints 3
```

This is useful if your list changes and you want to know how many items it has.

### Looping Through a List

You can use a `for` loop to go through all the items in a list. Here’s how:

```python
for item in grocery_list:
    print(item)
```

This loop will print:

```
milk
butter
eggs
```

💡 *This kind of loop is really useful when you don’t care about the position of the items — you just want to go through them all one by one.*

### Additional resources

- [Lists](https://youtu.be/xdpABsJZQYU)
- [List methods](https://youtu.be/sBaB1bcOgVE)



## Dictionaries

So far, we’ve worked with lists, which are great when you just need to store items in order. But what if you want to store labeled data — like names and phone numbers, or countries and their capitals?

That’s where **dictionaries** come in.

A dictionary is a collection of **key-value pairs**. You can think of it like a real dictionary: you look up a word (the key), and you get its definition (the value).

Here’s how to create a simple dictionary in Python:

```python
capitals = {
    "France": "Paris",
    "Ghana": "Accra",
    "Japan": "Tokyo"
}
```

In this dictionary:

- `"France"` is a key, and `"Paris"` is its value.
- `"Ghana"` is a key, and `"Accra"` is its value.

### Getting Values From a Dictionary

You can get the value for a specific key like this:

```python
print(capitals["Japan"])   # prints Tokyo
print(capitals["France"])  # prints Paris
```

💡 *Keys must be exact. If you misspell or use the wrong capitalization, Python will give you an error.*

### Setting Values in a Dictionary

You can change the value for a key, or even add a new key-value pair:

```python
capitals["France"] = "Lyon"      # change existing value
capitals["Nigeria"] = "Abuja"    # add new key and value
print(capitals)
```

Now the dictionary looks like this:

```python
{
    "France": "Lyon",
    "Ghana": "Accra",
    "Japan": "Tokyo",
    "Nigeria": "Abuja"
}
```

### Getting the Length of a Dictionary

Just like with lists, we can use `len()` to find out how many key-value pairs are in the dictionary:

```python
print(len(capitals))  # prints 4
```

### Looping Through a Dictionary

We can loop through a dictionary to see each key and its value:

```python
for country in capitals:
    print(country, "->", capitals[country])
```

This will print something like:

```
France -> Lyon
Ghana -> Accra
Japan -> Tokyo
Nigeria -> Abuja
```

If you want to be more specific and loop through both keys and values at the same time, Python gives you a built-in method called `.items()`:

```python
for country, city in capitals.items():
    print(country, "has its capital in", city)
```

Which prints:

```
France has its capital in Lyon
Ghana has its capital in Accra
Japan has its capital in Tokyo
Nigeria has its capital in Abuja
```

Dictionaries are perfect for storing data that’s related by label. They give you a clear way to associate one value with another, and they’re easy to search, update, and loop through.

### Additional resources

- [Dictionaries](https://youtu.be/yPyFlO8G6rw)
- [Dictionary methods](https://youtu.be/3zJoCpvKhx4)

# Thursday

Content for Thursday can be found [here](https://github.com/lindelwa122/Hacktoberfest-Introduction-To-Programming).

# Friday

## Conditionals

Sometimes we want our programs to make decisions. This is where **conditionals** come in. Conditionals let us ask questions and do something based on the answer.

Think of it like this:

- If it’s raining, take an umbrella.
- If it’s sunny, wear sunglasses.
- If it’s snowing, stay warm.

We can teach Python to do the same kind of thinking using `if`, `elif`, and `else`.

### Basic If Statement

Here’s an example:

```python
age = 18

if age >= 18:
    print("You're an adult.")
```

This code checks if `age` is greater than or equal to 18. If it is, it prints a message.

💡 *The colon `:` at the end of the `if` line means “here comes a block of code that runs if the condition is true.”*

### Using Else

We can add an `else` to handle what happens if the condition is not true:

```python
age = 16

if age >= 18:
    print("You're an adult.")
else:
    print("You're a minor.")
```

### Using Elif (Else If)

Sometimes we want to check more than one condition. That’s where `elif` comes in:

```python
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Keep working hard!")
```

Python checks each condition from top to bottom. As soon as it finds one that’s true, it runs that block and skips the rest.

### Comparison Operators

When we write conditions, we use **comparison operators** to ask questions. Here are the most common ones:

| Symbol | Meaning                 | Example   |
|--------|-------------------------|-----------|
| `==`   | equal to                | `x == 5`  |
| `!=`   | not equal to            | `x != 3`  |
| `>`    | greater than            | `x > 10`  |
| `<`    | less than               | `x < 7`   |
| `>=`   | greater than or equal   | `x >= 18` |
| `<=`   | less than or equal      | `x <= 100`|

💡 *Make sure to use `==` (double equals) when asking if two things are the same. A single equals `=` is for assigning values.*

### The Match Statement

Python also has something called a `match` statement. It’s like a more organized way of doing multiple `if`/`elif`/`else` checks — especially when checking for exact matches.

Here’s an example:

```python
day = "Saturday"

match day:
    case "Monday":
        print("Back to work!")
    case "Friday":
        print("Almost weekend!")
    case "Saturday" | "Sunday":
        print("It’s the weekend!")
    case _:
        print("Just another day.")
```

- Python checks which `case` matches the value of `day`.
- The `|` symbol means “or”, so that case will match `"Saturday"` or `"Sunday"`.
- The underscore `_` is a catch-all — it runs if no other case matches.

This is clean, easy to read, and perfect when you’re checking many specific values.

### Additional resources

- [Conditionals short](https://youtu.be/vGr1tvjqWs0)
- [Boolean expression short](https://youtu.be/51BNn5Ojupw)
