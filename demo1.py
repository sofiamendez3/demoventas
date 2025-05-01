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
else:
    st.error("Error: 'Region' or 'Sales' columns not found in the DataFrame.")
# prompt: Usando el dataframe df, crea un filtro con la columna Region

region_filter = st.selectbox("Select Region", df['Region'].unique())
filtered_df = df[df['Region'] == region_filter]
st.dataframe(filtered_df)
# prompt: usando el dataframe df, crear 2 filtros con streamlit, uno con la columna de Region y otro con la columna State e imprimir un solo resultado

import pandas as pd
import streamlit as st
import plotly.express as px

# Install openpyxl if you haven't already


try:
  df = pd.read_excel('SalidaFinal.xlsx', engine='openpyxl')
except FileNotFoundError:
  st.error("Error: 'SalidaFinal.xlsx' not found. Please make sure the file exists and is in the correct location.")
  st.stop() # Stop execution if the file is not found
except Exception as e:
  st.error(f"An error occurred: {e}")
  st.stop()


# Streamlit UI elements
st.title("Data Filtering")

# Region filter
region_filter = st.selectbox("Select Region", df['Region'].unique())

# State filter
state_filter = st.selectbox("Select State", df['State'].unique())


# Apply both filters and display the result
filtered_df = df[(df['Region'] == region_filter) & (df['State'] == state_filter)]

# Display the filtered data
if not filtered_df.empty:
    st.dataframe(filtered_df)
    # Display only the first row if you want a single result
    st.write("First result:")
    st.write(filtered_df.iloc[0])
else:
    st.write("No data found for the selected filters.")
