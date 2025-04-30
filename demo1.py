import streamlit as st
import pandas as pd

try:
  df = pd.read_excel('SalidaFinal.xlsx', engine='openpyxl')
  st.dataframe(df) # Use st.dataframe to display in Streamlit
except FileNotFoundError:
  st.error("Error: 'SalidaFinal.xlsx' not found. Please make sure the file exists and is in the correct location.")
except Exception as e:
  st.error(f"An error occurred: {e}")
