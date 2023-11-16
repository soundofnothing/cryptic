
# import numpy as np
# import matplotlib.pyplot as plt

# def plot_elliptic_curve(a, b):
#     y, x = np.ogrid[-5:5:100j, -5:5:100j]
#     plt.contour(x.ravel(), y.ravel(), y**2 - x**3 - a*x - b, levels=[0], colors='blue')
#     plt.grid()
#     plt.show()

# # Example elliptic curve: y^2 = x^3 - x + 1
# plot_elliptic_curve(-1, 1)

# Integer Arithmetic Section in Streamlit App
import streamlit as st

# TODO - variadic bases (convert numbers between bases and see results of addition and multiplication)
def integer_arithmetic():
    st.subheader("Integer Arithmetic")

    # Input fields for two integers
    num1 = st.number_input("Enter first large integer", format="%d")
    num2 = st.number_input("Enter second large integer", format="%d")

    # Operation buttons
    if st.button('Add'):
        st.write("Result: ", num1 + num2)
    if st.button('Subtract'):
        st.write("Result: ", num1 - num2)
    if st.button('Multiply'):
        st.write("Result: ", num1 * num2)
    if st.button('Divide'):
        st.write("Result: ", num1 / num2 if num2 != 0 else "Cannot divide by zero")

# Modular Arithmetic in Streamlit App

def modular_arithmetic():
    st.subheader("Modular Arithmetic")

    num1 = st.number_input("Enter first number", format="%d")
    num2 = st.number_input("Enter second number", format="%d")
    modulus = st.number_input("Enter modulus", min_value=1, step=1, format="%d")

    if st.button('Add'):
        st.write("Result: ", (num1 + num2) % modulus)
    if st.button('Subtract'):
        st.write("Result: ", (num1 - num2) % modulus)
    if st.button('Multiply'):
        st.write("Result: ", (num1 * num2) % modulus)
    if st.button('Modular Inverse'):
        try:
            inverse = pow(num2, -1, modulus)
            st.write("Modular Inverse: ", inverse)
        except ValueError:
            st.write("Modular Inverse does not exist")

# Main function to run the app
def main():
    st.title("Cryptography Concepts Explorer")
    
    # Integer Arithmetic Section
    integer_arithmetic()

    # Other sections will be added here
    modular_arithmetic()

if __name__ == "__main__":
    main()

