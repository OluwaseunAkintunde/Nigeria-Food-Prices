import pandas as pd 
import streamlit as st
import numpy as np

st.markdown('''
# Nigeria food prices from 2017
''')


df = pd.read_csv("./Nigeria Food Prices From 2017.csv") 
st.write(df)

z= df["produce"].value_counts().head()
st.title("Top 5 most purchased produce")

st.bar_chart(z)

temp=pd.pivot_table(df,index=["produce"], values="price")
st.title("Price  ranges of produce")
st.bar_chart(temp)

temp2=pd.pivot_table(df,index=["state", "produce"], values=["price"])
st.title("Price  ranges of produce in various states")
st.write(temp2)