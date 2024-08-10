# Question 1: Implementing a Counter Factory

Create a function named counter() that serves as a factory for generating independent counter objects using the concept of closures.

### Requirements

1. Define a function named counter() that takes no arguments. 
2. The counter() function should return a new function (closure). Each function returned by counter() should act as an independent counter.
3. When called, this returned function should:
    - Increment an internal count by 1 and 
    - Return the new value of the count.
4. Incrementing one counter should not affect the count of any other counter.

### Note

1. Each new counter (i.e., each function returned by counter()) should initialize its count to 0.
2. Multiple counters created by calling counter() multiple times should operate independently.
3. The count variable should not be directly accessible from outside the closure. 
4. The implementation should not use any global variables.

### Illustration

```python
counter1 = counter()
counter2 = counter()

# Using counter1
print(counter1())  # Prints 1
print(counter1())  # Prints 2
print(counter1())  # Prints 3

# Using counter2
print(counter2())  # Prints 1
print(counter2())  # Prints 2

# counter1 continues from where it left off
print(counter1())  # Prints 4

# Creating a new counter
counter3 = counter()
print(counter3())  # Prints 1
```

# Question 2: Implementing a Multiplier Factory

Create a function named multiplier(n) that generates specialized multiplication functions using the concept of closures.

### Requirements:

1. Define a function named multiplier that takes one parameter n (a number).
2. The multiplier(n) function should return a new function (closure). Each function returned by multiplier(n) should act as a specialized multiplier.
3. When called, this returned function should:
    a. Accept one argument x (a number).
    b. Multiply x by the n value that was passed to the original multiplier function.
    c. Return the result of this multiplication.
4. It should be possible to create multiple, independent multiplier functions with different n values. These functions should not interfere with each other.

### Note

1. The returned function must retain access to the n value from multiplier(n), even after multiplier(n) has finished executing.
2. The n value should not be directly accessible or modifiable from outside the closure.
3. The implementation should not use any global variables.

### Illustration

```python
double = multiplier(2)
triple = multiplier(3)
quadruple = multiplier(4)

# Using the multiplier functions
print(double(5))     # Prints 10
print(triple(5))     # Prints 15
print(quadruple(5))  # Prints 20

# Creating and using another multiplier
times_ten = multiplier(10)
print(times_ten(5))  # Prints 50

# Verifying independence
print(double(10))    # Prints 20
```
