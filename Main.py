import streamlit as st
import login
import form
st.set_page_config(page_title="Sports Academy",page_icon=":ball:",layout="centered",
	initial_sidebar_state="collapsed")

st.sidebar.title("Navigator")
pages_dict={"Login":login,"Form":form}
user_choice=st.sidebar.radio("Go to",tuple(pages_dict.keys()))
if user_choice=="Form":
	form.app()
else:
	login.app()
