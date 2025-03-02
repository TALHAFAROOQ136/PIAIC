import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Create two columns
col1, col2 = st.columns(2)

# Input fields in the first column
with col1:
    st.header("Input")
    num1 = st.number_input("Enter the first number", value=0.0)
    num2 = st.number_input("Enter the second number", value=0.0)
    operation = st.radio("Select an operation", ["Add", "Subtract", "Multiply", "Divide"])

# Calculate button and result in the second column
with col2:
    st.header("Output")
    if st.button("Calculate"):
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                st.error("Division by zero is not allowed!")
                result = None
            else:
                result = num1 / num2

        # Display the result
        if result is not None:
            st.success(f"Result: {result}")
