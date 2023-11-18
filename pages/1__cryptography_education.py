# Import necessary libraries
import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Topic 1: Integer Arithmetic

def integer_arithmetic_calculator():
    st.subheader("Integer Arithmetic Calculator")
    num1 = st.number_input("Enter first integer", value=0)
    num2 = st.number_input("Enter second integer", value=0)
    base = st.selectbox("Select Base for Calculation", [10, 2, 8, 16], index=0)  # Default to base 10

    if st.button("Calculate"):
        #results = perform_arithmetic_operations(num1, num2, base)
        st.table(perform_arithmetic_operations(num1, num2, base))

def perform_arithmetic_operations(num1, num2, base):
    operations = {
        f"{num1} + {num2}": num1 + num2,
        f"{num1} - {num2}": num1 - num2,
        f"{num1} * {num2}": num1 * num2,
        f"{num1} / {num2}" if num2 != 0 else "Division by Zero": "Error" if num2 == 0 else num1 / num2
    }


    def convert_to_base(number, base):
        if base == 10:
            return number
        else:
            return np.base_repr(int(number), base=base)

    # Convert results to the selected base
    converted_operations = {op: convert_to_base(val, base) if val != "Error" else "Error" for op, val in operations.items()}
    
    return converted_operations


def digit_polynomials_calculator():
    """Visualizes a number as digit polynomials for different bases."""
    st.subheader("Digit Polynomials Visualization")

    # User inputs
    number = st.number_input("Enter a number", min_value=0, value=0, format='%d')
    base_options = [2, 8, 10, 16]  # Common bases, can be expanded
    base = st.selectbox("Select Base", options=base_options, index=2)  # Default to base 10

    # Visualization
    if st.button("Visualize"):
        visualize_digit_polynomials(number, base)


def visualize_digit_polynomials(number, base):
    """Converts a number to its digit polynomial representation and plots it."""
    # Convert the number to the specified base
    if base == 10:
        digits = [int(d) for d in str(number)]
    else:
        digits = np.base_repr(number, base=base)
        digits = [int(d, base=base) for d in digits[::-1]]  # Reverse for correct order

    # Polynomial representation
    polynomial = np.poly1d(digits[::-1])  # Reverse again for poly1d representation

    # Create x and y values for plotting
    x = np.linspace(-base, base, 400)
    y = polynomial(x)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=f"Base {base} Polynomial of {number}")
    plt.title(f"Digit Polynomial Representation of {number} in Base {base}")
    plt.xlabel("x")
    plt.ylabel("Polynomial Value")
    plt.grid(True)
    plt.legend()
    plt.show()

    # Display using Streamlit
    st.pyplot(plt)

def change_of_base_calculator():
    """Calculator for changing the base of a number."""
    st.subheader("Change of Base Calculator")

    # User inputs for number and bases
    number_input = st.number_input("Enter the number", min_value=0, value=0, format='%d')
    from_base = st.selectbox("From Base", options=[2, 8, 10, 16], index=2)
    to_base = st.selectbox("To Base", options=[2, 8, 10, 16], index=0)

    if st.button("Convert"):
        converted_number = convert_base(number_input, from_base, to_base)
        st.write(f"{number_input} in base {from_base} is {converted_number} in base {to_base}")

def convert_base(number, from_base, to_base):
    """Converts a number from one base to another."""
    if from_base != 10:
        # Convert from the original base to base 10
        number = int(str(number), from_base)
    if to_base == 10:
        return number
    else:
        # Convert from base 10 to the new base
        return np.base_repr(number, base=to_base)


# Topic 2: Prime Numbers

def prime_number_checker():
    st.subheader("Prime Number Checker")
    number = st.number_input("Enter a number", min_value=1, value=2)
    if st.button("Check Prime"):
        if sympy.isprime(number):
            st.success(f"{number} is a prime number.")
        else:
            st.error(f"{number} is not a prime number.")


def prime_factorization_calculator():
    st.subheader("Prime Factorization Calculator")
    number = st.number_input("Enter a number for factorization", min_value=1, value=2)
    if st.button("Factorize"):
        factors = sympy.factorint(number)
        st.write(f"Prime factors of {number}: {dict(factors)}")


def prime_number_generator():
    st.subheader("Prime Number Generator")
    start = st.number_input("Enter start of range", min_value=0, value=0)
    end = st.number_input("Enter end of range", min_value=0, value=10)
    if st.button("Generate Primes"):
        primes = list(sympy.primerange(start, end))
        st.write(f"Prime numbers between {start} and {end}: {primes}")


def sieve_of_eratosthenes_visualization():
    st.subheader("Sieve of Eratosthenes Visualization")
    limit = st.number_input("Enter a limit for prime number generation", min_value=10, value=30)
    if st.button("Visualize Sieve"):
        primes, sieve = run_sieve_of_eratosthenes(limit)
        st.write(f"Prime numbers up to {limit}: {primes}")
        # Visualization logic to be implemented

def run_sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    primes = []
    for current in range(2, limit + 1):
        if sieve[current]:
            primes.append(current)
            for multiple in range(current * 2, limit + 1, current):
                sieve[multiple] = False
    return primes, sieve


# Topic 3: Modular Arithmetic

def modular_arithmetic_calculator():
    st.subheader("Modular Arithmetic Calculator")
    num1 = st.number_input("Enter first number", value=0)
    num2 = st.number_input("Enter second number", value=0)
    modulus = st.number_input("Enter modulus", value=1, min_value=1)

    if st.button("Calculate"):
        mod_results = perform_modular_arithmetic(num1, num2, modulus)
        st.table(mod_results)

def perform_modular_arithmetic(num1, num2, modulus):
    mod_operations = {
        f"({num1} + {num2}) mod {modulus}": (num1 + num2) % modulus,
        f"({num1} - {num2}) mod {modulus}": (num1 - num2) % modulus,
        f"({num1} * {num2}) mod {modulus}": (num1 * num2) % modulus,
        f"({num1} ^ {num2}) mod {modulus}": pow(num1, num2, modulus)
    }
    return mod_operations

# Topic 4: Greatest Common Divisor and Euclidean Algorithm

def gcd_calculator():
    """Placeholder for the GCD Calculator"""
    pass

def extended_euclidean_algorithm():
    """Placeholder for the Extended Euclidean Algorithm Calculator"""
    pass

# Topic 5: Euler's Totient Function

def eulers_totient_calculator():
    """Placeholder for Euler's Totient Calculator"""
    pass

# Topic 6: Exponentiation

def exponentiation_calculator():
    """Placeholder for the Exponentiation Calculator"""
    pass

# Topic 7: Logarithms

def logarithm_calculator():
    """Placeholder for the Logarithm Calculator"""
    pass

# Main function to run the Streamlit app

def main():
    st.title("Cryptic: An Interactive Cryptography Education Tool")

    # Navigation
    topic = st.sidebar.selectbox("Choose a topic", 
                                 ["Integer Arithmetic", "Prime Numbers", 
                                  "Modular Arithmetic", "GCD and Euclidean Algorithm", 
                                  "Euler's Totient Function", "Exponentiation", "Logarithms"])

    # Topic 1: Integer Arithmetic
    if topic == "Integer Arithmetic":
        st.header("Integer Arithmetic")
        integer_arithmetic_calculator()
        change_of_base_calculator()
        digit_polynomials_calculator()
        prime_number_generator()
        sieve_of_eratosthenes_visualization()
        modular_arithmetic_calculator()

    # Other topics with similar structure...
    
if __name__ == "__main__":
    main()
