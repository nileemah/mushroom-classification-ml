import streamlit as st
import pandas as pd
from io import StringIO
 
st.write("""
# Mushroom Classification app
""")

uploaded_file = st.file_uploader("Choose a test data file")
if uploaded_file is not None:
    # To read file as bytes:
    # bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data)
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    #st.write(stringio)
    string_data = stringio.read()
    st.write(string_data)

option = st.selectbox(
    "Select Model",
    ("Logistic Regression", "Decision Tree", "kNN", "Naive Bayes","Random Forest")
)

# Display the selected option
st.write("You selected:", option)
