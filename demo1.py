# prompt: Imprimir dataframe usando streamlit

import streamlit as st
import pandas as pd

# Install openpyxl if you haven't already
# !pip install openpyxl # This should be done only once in the notebook environment


try:
  df = pd.read_excel('SalidaFinal.xlsx', engine='openpyxl')
  st.dataframe(df) # Use st.dataframe to display in Streamlit
except FileNotFoundError:
  st.error("Error: 'SalidaFinal.xlsx' not found. Please make sure the file exists and is in the correct location.")
except Exception as e:
  st.error(f"An error occurred: {e}")
  # prompt: Arma una grafica de las ventas por region del dataframe df usando streamlit

import plotly.express as px

# Assuming 'Region' and 'Sales' are column names in your DataFrame
if 'Region' in df.columns and 'Sales' in df.columns:
    fig = px.bar(df, x='Region', y='Sales', title='Ventas por Región')
    st.plotly_chart(fig)
else:
    st.error("Error: 'Region' or 'Sales' columns not found in the DataFrame.")
# prompt: Usando el dataframe df, crea un filtro con la columna Region

region_filter = st.selectbox("Select Region", df['Region'].unique())
filtered_df = df[df['Region'] == region_filter]
st.dataframe(filtered_df)
# prompt: Usando el dataframe df, crear 2 filtros con streamlit, uno con la columna Region y otro con la columna State e imprimir el dataframe. Tambien crear una gráfica de pastel con la columna Category

# Assuming 'Category' is a column in your DataFrame
if 'Category' in df.columns:
    fig_pie = px.pie(df, names='Category', title='Distribución por Categoría')
    st.plotly_chart(fig_pie)
else:
    st.error("Error: 'Category' column not found in the DataFrame.")
