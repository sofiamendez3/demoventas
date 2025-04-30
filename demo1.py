import streamlit as st
import pandas as pd

try:
  df = pd.read_excel('SalidaFinal.xlsx', engine='openpyxl')
  st.dataframe(df) # Use st.dataframe to display in Streamlit
except FileNotFoundError:
  st.error("Error: 'SalidaFinal.xlsx' not found. Please make sure the file exists and is in the correct location.")
except Exception as e:
  st.error(f"An error occurred: {e}")
import matplotlib.pyplot as plt

# Assuming 'Region' and 'Sales' are column names in your DataFrame
try:
  sales_by_region = df.groupby('Region')['Sales'].sum()
  plt.figure(figsize=(10, 6))  # Adjust figure size as needed
  sales_by_region.plot(kind='bar')
  plt.title('Sales by Region')
  plt.xlabel('Region')
  plt.ylabel('Total Sales')
  plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
  plt.tight_layout() # Adjust layout to prevent labels from overlapping
  plt.show()
except KeyError as e:
  print(f"Error: Column '{e}' not found in the DataFrame. Please check your column names.")
except Exception as e:
  print(f"An error occurred while plotting: {e}")
