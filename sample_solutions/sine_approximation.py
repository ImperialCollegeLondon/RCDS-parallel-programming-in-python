from multiprocessing import Pool
from math import factorial, pi, sin

def sine_term(x, k):
    # This function calculates the nth term of the Taylor series expansion of sine(x)
    # x is the value at which to evaluate the sine function
    # k is the index of the term to calculate

    # Calculate and return the term
    return ((-1) ** k) * (x ** (2 * k + 1)) / factorial(2 * k + 1)

def sine_approx(x, n_terms):
    # This function calculates an approximation of the sine function at x using n_terms terms of the Taylor series expansion

    # Create a list of inputs for the sine_term function
    inputs = [(x, k) for k in range(n_terms)]
    print(inputs)

    # Create a pool of two threads to calculate the terms in parallel
    with Pool(2) as p:
        # Calculate the terms in parallel and store the results in a list
        terms = p.starmap(sine_term, inputs)

    # Return the sum of the terms
    return sum(terms)

# Test the sine_approx function
x = 0.5
n_terms = 3
print(sine_approx(x, n_terms), sin(x))

x = pi
n_terms = 5
print(sine_approx(x, n_terms), sin(x))