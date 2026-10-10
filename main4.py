import streamlit as st

st.title("User Information Form")

with st.form(key="user_info_form"):
    name = st.text_input("Enter your name: ")
    age = st.number_input("Enter your age: ")

    print(name, age)

    st.form_submit_button("Submit")

    