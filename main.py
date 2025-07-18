import streamlit as st

print("hello, I am Shiney")

s = st.text_input("Enter your name")

if s:
    st.write(f"{s}, nice to meet you")
