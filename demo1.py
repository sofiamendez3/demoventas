import streamlit as st
import pandas as pd

try:
  df = pd.read_excel('SalidaFinal.xlsx', engine='openpyxl')
  st.dataframe(df) # Use st.dataframe to display in Streamlit
except FileNotFoundError:
  st.error("Error: 'SalidaFinal.xlsx' not found. Please make sure the file exists and is in the correct location.")
except Exception as e:
  st.error(f"An error occurred: {e}")
import plotly.express as px

# Assuming 'Region' and 'Sales' are column names in your DataFrame
if 'Region' in df.columns and 'Sales' in df.columns:
    fig = px.bar(df, x='Region', y='Sales', title='Ventas por Región')
 st.plotly_chart(fig)
with st.sidebar:
else:
    st.error("Error: 'Region' or 'Sales' columns not found in the DataFrame.")
# prompt: Usando el dataframe df, crea un filtro con la columna Region

region_filter = st.selectbox("Select Region", df['Region'].unique())
filtered_df = df[df['Region'] == region_filter]
st.dataframe(filtered_df)
