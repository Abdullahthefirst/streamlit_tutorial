import streamlit as st

if "step" not in st.session_state:
    st.session_state.step = 1

if "info" not in st.session_state:
    st.session_state.info = {}
#if we used it as a button, we first would have entered the data and pressed the enter, then \
#the page would rerun, now with button return as true, then set the variables
#and then we would have to again rerun to take the actions of step2 if step2 was under elif
def go_to_step2(name):
    st.session_state.info["name"]= name
    st.session_state.step = 2

def go_to_step1():
    st.session_state.step = 1
    

if st.session_state.step == 1:
    st.header("Part 1:")
    name = st.text_input("Name",value=st.session_state.info.get("name", "") )
    #the thing here is that now we are implementing callbacks i.e. the function on_click acts
    #before rerunning the page
    st.button("Next", on_click=go_to_step2 , args=(name,))

elif st.session_state.step  == 2:
    st.header("Part 2:")
    st.subheader("Please review this:")
    st.write(f"**Name** ={st.session_state.info.get("name", "Error")}")
    if st.button("Submit"):
        st.write("Great")
        st.balloons()
        st.session_state.info = {}
    st.button("Back", on_click=go_to_step1)
        # st.rerun()