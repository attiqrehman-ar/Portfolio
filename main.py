import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)


with col1 :
    st.image("images/photo.png")

with col2:
    st.title("Attiq Ur Rehman")
    content = """
    Hi, i am Attiq Ur Rehman and i am recently graduated as a software engineer from University OF Gujrat and currently looking 
    for a job
    
    
    """
    st.info(content)

c = """
    below you can fine some of my apps i have built  in python. feel free to contact me!
    """
st.write(c)