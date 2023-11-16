# Integer Arithmetic Section in Streamlit App
import streamlit as st

# TODO - variadic bases (convert numbers between bases and see results of addition and multiplication)
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

    modular_arithmetic()

if __name__ == "__main__":
    main()
