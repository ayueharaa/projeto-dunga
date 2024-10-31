import streamlit as st
import seaborn as sns
from sklearn import datasets
import pandas as pd

df = sns.load_dataset('iris')

st.title("Titulo")
st.write(df.head())

st.subheader("Subtitulo2")
st.write("Visualização das caracter´sticas das espécies de Iris")
scatter_plot = sns.scatterplot(data=df, x='sepal_length', y= 'sepal_width', hue='species')
st.pyplot(scatter_plot.figure)

st.subheader("Subtitulo2")
st.write("Distribuição do comprimento da pétala")
hist_plot = sns.histplot(data=df, x='petal_length', hue='species', multiple='stack')
st.pyplot(hist_plot.figure)
