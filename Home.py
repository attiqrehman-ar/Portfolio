import streamlit as st
import  pandas
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)


with col1 :
    st.image("images/mypic.jpg")

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

col3, empty_col, col4 = st.columns([1.5, 0.5 , 1.5])
df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index , row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row["description"])
        st.image("images/"+ row["image"])
        st.write(f'[Source code](https://github.com/attiqrehman-ar/)')

with col4:
    for index , row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f'[Source code](https://github.com/attiqrehman-ar/)')
