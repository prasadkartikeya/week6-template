def  multiplier(n):
    """
    Creates a specialized multiplication function using closures.
    
    Args:
        n (int or float): The multiplier value.
    
    Returns:
        function: A closure that multiplies its input by n.
    """
    def multiply(x):
        return x * n  # Multiply the input x by n
    
    return multiply

# Example usage
double = multiplier(2)       # Multiplier function for doubling
triple = multiplier(3)       # Multiplier function for tripling
quadruple = multiplier(4)    # Multiplier function for quadrupling

# Using the multiplier functions
print(double(5))       # Prints 10
print(triple(5))       # Prints 15
print(quadruple(5))    # Prints 20

# Creating and using another multiplier
times_ten = multiplier(10)
print(times_ten(5))    # Prints 50

# Verifying independence
print(double(10))      # Prints 20