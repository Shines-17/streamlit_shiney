import streamlit as st

st.write("hello, I am Shiney")

s = st.text_input("Enter your name")

if s:
    st.write(f"{s}, Good Morning")
