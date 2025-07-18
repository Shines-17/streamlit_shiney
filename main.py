import streamlit as st
print("hello, i am shiney")
s=st.text_input("enter your name")
if s:
st.write(f"{s}, nice to meet you")
