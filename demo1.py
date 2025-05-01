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
# prompt: Crear una grafica de pastel de las categorias de los productos y agregarle filtros, tener en cuenta que los estados tienen que cambiar conforme la region 

import pandas as pd
import streamlit as st
import plotly.express as px

# Install openpyxl if you haven't already
# !pip install openpyxl  # This should be done only once in the notebook environment

try:
    df = pd.read_excel('SalidaFinal.xlsx', engine='openpyxl')
except FileNotFoundError:
    st.error("Error: 'SalidaFinal.xlsx' not found. Please make sure the file exists and is in the correct location.")
    st.stop()  # Stop execution if the file is not found
except Exception as e:
    st.error(f"An error occurred: {e}")
    st.stop()

st.title("Interactive Sales Data Visualization")

# Region filter
selected_region = st.selectbox("Select Region", df['Region'].unique())

# Dynamic State filter based on selected region
filtered_df_region = df[df['Region'] == selected_region]
selected_state = st.selectbox("Select State", filtered_df_region['State'].unique())

# Apply filters
filtered_df = df[(df['Region'] == selected_region) & (df['State'] == selected_state)]

# Display filtered data (optional)
#st.dataframe(filtered_df)

# Create pie chart of categories
if 'Category' in filtered_df.columns:
    fig_pie = px.pie(filtered_df, names='Category', title=f'Product Category Distribution in {selected_state}, {selected_region}',
                     hole=0.3) # Add a hole to make it a donut chart
    st.plotly_chart(fig_pie)
else:
    st.error("Error: 'Category' column not found in the DataFrame.")
