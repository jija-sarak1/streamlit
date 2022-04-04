import streamlit as st
import pandas as pd
import numpy as np
import time

a = [1,2,3,4,5,6,7,8]
n = np.array(a)
nd = n.reshape((2,4))
dic = {
    "name":["Jija","Sarak"],
    "age" :[23,27],
    "City":["Pune","Delhi"]
}

data = pd.read_csv("/home/jija/Desktop/streamlit/Salary_data.csv")

st.dataframe(data , width = 700 , height = 700)
st.table(dic)
st.json(dic)
st.write(dic)

@st.cache
def ret_time(a):
    time.sleep(5)
    return time.time()

if st.checkbox("1"):
    st.write(ret_time(1))

if st.checkbox("2"):
    st.write(ret_time(2))
