import streamlit as st
def app():
	st.title("Admission Form")
	form=st.form("My Form")
	with form:
		col1,col2=st.beta_columns(2)
		col1.selectbox("Title",("Ms","Mr","Mrs"))
		col2.text_input("Enter your name")
	address=form.text_input("Enter your address")
	number=form.text_input("Enter Contact Number")
	slider=form.slider("Age",2,15)
	gender=form.radio("Gender",("Male","Female"))
	sports=form.multiselect("Choose a Sport",("Soccer","Swim","Track","Basketball"))
	submit=form.form_submit_button("Submit")
	if submit:
		st.success("Your form successfully submitted")
