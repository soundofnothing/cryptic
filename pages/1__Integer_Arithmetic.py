
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


# Main function to run the app
def main():
    st.title("Cryptography Concepts Explorer")
    
    # Integer Arithmetic Section
    integer_arithmetic()


if __name__ == "__main__":
    main()
