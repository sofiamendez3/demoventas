import streamlit as st
import pandas as pd

# Leer el archivo Excel
try:
  df = pd.read_excel("SalidaFinal.xlsx", engine='openpyxl')
  # Mostrar el DataFrame usando Streamlit
  st.dataframe(df)
except FileNotFoundError:
  st.error("Error: El archivo 'SalidaFinal.xlsx' no se encuentra en el directorio actual.")
except Exception as e:
  st.error(f"Ocurrió un error al leer el archivo: {e}")
