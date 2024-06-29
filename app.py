import streamlit as st

st.title("Streamlit first application")
st.header("Heading of streamlit")
st.subheader("My subheader")
st.text('This is my text')
st.success("Success")
st.warning('Warning')
st.info("information")
st.error("Error")
if st.checkbox("select/Unselect"):
    st.text("User selected text box")
else:
    st.text("User not selected text box")

state =  st.radio("What is your favorit colour?",('Red','Blue','Green'))

if state=='Green':
    st.success("My favorit colour")

occupation = st.selectbox('What do you do?',["Blogger","Photograpy"])

st.text(f"Selected option is {occupation}")

clicked = st.button("example Button")

if clicked:
    st.success("You clicked button")

st.sidebar.header("Heading of sidebar")
st.sidebar.text("Created by me")