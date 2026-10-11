import streamlit as st

st.sidebar.title("This is the sidebar")
st.sidebar.write("You can place elements like sliders, buttons, and text here")
sidebar_input = st.sidebar.text_input("Enter text")

#Tabs layout
tab1, tab2, tab3 = st.tabs(["Tab1", "Tab2", "Tab3"])
with tab1:
    st.write("You are in tab 1")

with tab2:
    st.write("You are in tab 2")

with tab3:
    st.write("You are in tab 3")

col1, col2 = st.columns(2)

with col1:
    st.header("Column 1")
    st.write("Content for column 1")

with col2:
    st.header("Column 2")
    st.write("Content for column 2")

with st.container(border=True):
    st.write("You are inside a container")
    st.write("Container can be very useful for grouping of elements")
    st.write("It is also very helpful for sections of page")

# Empty placeholder
placeholder = st.empty()
placeholder.write("This is an empty placeholder, useful for dynamic content.")

if st.button("Update Placeholder"):
    placeholder.write("The content of this placeholder has been updated.")

# Expander
with st.expander("Expand for more details"):
    st.write("This is additional information that is hidden by default.")
    st.write("You can use expanders to keep your interface cleaner.")

# Popover (Tooltip)
st.write("Hover over this button for a tooltip")
st.button("Button with Tooltip", help="This is a tooltip or popover on hover.")

# Sidebar input handling
if sidebar_input:
    st.write(f"You entered in the sidebar: {sidebar_input}")
