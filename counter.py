def counter():
    """
    Creates an independent counter function using closures.
    
    Returns:
        function: A closure that increments and returns an internal count.
    """
    count = 0  # Internal count variable, private to this closure

    def increment():
        nonlocal count  # Allows modification of the count variable in the enclosing scope
        count += 1
        return count

    return increment

# Example usage
counter1 = counter()  # Create the first counter
counter2 = counter()  # Create the second counter

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