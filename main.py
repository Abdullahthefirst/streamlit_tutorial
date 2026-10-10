import streamlit as st
import os

st.title("Super Simple Title")
st.header("This is a header")
st.subheader('Subheader')
st.markdown("This is _Markdown_")
st.caption("small text")
code_example = """
def greet(name):
    print('hello', name)
"""
st.code(code_example, language="python")
st.divider()

st.image(os.path.join(os.getcwd(), "static", "image1.jpg"))