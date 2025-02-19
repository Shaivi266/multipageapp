import streamlit as st
def app():
	st.title("Login")
	username_list=["shaivi123","cat132","dog45"]
	pass_list=["12","23","34"]
	user_pass=dict(zip(username_list,pass_list))
	username=st.text_input("Enter your username")
	password=st.text_input("Enter your pasword")
	if st.button("Submit"):
		if username in username_list:
			if password==user_pass[username]:
				st.success("Succesfully logged in")
			else:
				st.warning("Password Incorrect")
		else:
			st.warning("Username not in the database")
