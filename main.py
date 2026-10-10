import streamlit as st

st.title("Super Simple Title")
st.header("This is a header")
st.subheader('Subheader')
st.markdown("This is _Markdown_")
st.caption("small text")
code_example = """
def greet(name):
    print('hello', name)
"""
st.code(code_example, Language="python")
st.divider()