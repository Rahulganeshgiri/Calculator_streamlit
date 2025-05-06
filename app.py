import streamlit as st

st.title("🧮 Simple Calculator")

# Input numbers
num1 = st.number_input("Enter first number", value=0.0, format="%.2f")
num2 = st.number_input("Enter second number", value=0.0, format="%.2f")

# Operation selection
operation = st.selectbox("Choose operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform calculation on button click
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 == 0:
            st.error("Division by zero is not allowed.")
            result = None
        else:
            result = num1 / num2

    if result is not None:
        st.success(f"Result: {result:.2f}")
