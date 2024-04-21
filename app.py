import streamlit as st

st.title ('NASCET CALCULATOR')
x = st.number_input ('Stenosis')
y = st.number_input ('Normal diameter')

def nascet (x,y):
    result = ((y-x)/y)*100
    return round (result,2)
    
    


if st.button ('Stenosis measurement'):
    st.write ('Stenosis (in %) per **NASCET** criteria is ')
    st.success (nascet(x,y))
