import streamlit as st
from send_email import  send_email

st.header("Contact me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your Emil Address")
    raw_message =st.text_area("your message")
    message=f"""\
Subject : New email from {user_email}


from : {user_email}
{raw_message}
"""
    button = st.form_submit_button()
    if button:
        send_email(message)
        st.info("Your message sent sucessfully")

