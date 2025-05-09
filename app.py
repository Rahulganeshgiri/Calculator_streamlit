import streamlit as st
import math
import numpy as np

st.set_page_config(page_title="Advanced Calculator", page_icon="🧮", layout="centered")

# UI Styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    div.stButton > button:first-child {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        height: 3em;
        width: 100%;
        border-radius: 10px;
    }
    div.stTextInput > label {
        font-size: 20px;
        font-weight: bold;
    }
    .footer {
        position: fixed;
        bottom: 10px;
        right: 20px;
        font-size: 14px;
        color: gray;
    }
    .creator {
        position: fixed;
        top: 10px;
        left: 20px;
        font-size: 16px;
        color: gray;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Creator credit at the top-left corner
st.markdown('<div class="creator">Created by Rahul</div>', unsafe_allow_html=True)

st.title("🧮 Advanced Calculator")
st.write("Enter a mathematical expression to evaluate. Supports basic arithmetic, trigonometry, logs, roots, and more.")

expression = st.text_input("Expression", value="")

# Safe evaluation
allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
allowed_names.update({"np": np, "pi": math.pi, "e": math.e})

if st.button("Calculate"):
    try:
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        st.success(f"Result: {result}")
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Tip section
with st.expander("📘 Supported Functions"):
    st.markdown("""
    - Basic: `+`, `-`, `*`, `/`, `**`
    - Trigonometric: `sin()`, `cos()`, `tan()`, `asin()`, `acos()`, `atan()`
    - Logarithmic: `log(x, base)`, `log10(x)`, `log2(x)`, `ln(x)` (use `log(x)` for natural log)
    - Roots: `sqrt(x)`
    - Constants: `pi`, `e`
    - Numpy also supported: e.g., `np.exp(1)`, `np.mean([1,2,3])`
    """)

# Footer with author credit
st.markdown('<div class="footer">App created by Rahul Giri</div>', unsafe_allow_html=True)
