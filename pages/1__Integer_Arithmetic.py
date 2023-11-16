import streamlit as st

def integer_arithmetic_page():
    st.title("Integer Arithmetic Explorer")
    st.write("Explore basic arithmetic operations with integers. Input two numbers and select an operation to see the result.")

    with st.form("arithmetic_form"):
        num1 = st.number_input("Enter the first integer", value=0, key='num1')
        num2 = st.number_input("Enter the second integer", value=0, key='num2')
        operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"], key='operation')
        submit_button = st.form_submit_button("Calculate")

        if submit_button:
            result = None
            if operation == "Add":
                result = num1 + num2
            elif operation == "Subtract":
                result = num1 - num2
            elif operation == "Multiply":
                result = num1 * num2
            elif operation == "Divide":
                if num2 != 0:
                    result = num1 / num2
                else:
                    st.error("Cannot divide by zero.")

            if result is not None:
                st.write(f"Result: {result}")

    # Additional sections for advanced operations can be added here

# Assuming this function is called in your main app file
integer_arithmetic_page()
