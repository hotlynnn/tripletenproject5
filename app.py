import pandas as pd
import plotly.express as px
import streamlit as st

# Load data
car_data = pd.read_csv('vehicles_us.csv')

# Header
st.header('Car Advertisement Data Dashboard')

# Graph 1: Basic Visualizations ---
st.subheader('General Exploration')

# Histogram check box
build_histogram = st.checkbox('Show Odometer Histogram')
if build_histogram:
    st.write('Distribution of car mileage (odometer)')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Scatter plot check box
build_scatter = st.checkbox('Show Price vs Odometer Scatter Plot')
if build_scatter:
    st.write('Relationship between Price and Odometer')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

# Graph 2: Manufacturer Comparison ---
st.header('Compare price distribution between manufacturers')

# Extract manufacturer from model
car_data['manufacturer'] = car_data['model'].apply(lambda x: x.split()[0])
manufacturers = sorted(car_data['manufacturer'].unique())

col1, col2 = st.columns(2)

with col1:
    manuf_1 = st.selectbox('Select manufacturer 1', manufacturers, index=0)

with col2:
    manuf_2 = st.selectbox('Select manufacturer 2', manufacturers, index=1)

normalize = st.checkbox('Normalize histogram (show percentages)', value=True)

# Filter data
df_filtered = car_data[car_data['manufacturer'].isin([manuf_1, manuf_2])]

histnorm = 'percent' if normalize else None

fig_comp = px.histogram(df_filtered, 
                       x="price", 
                       color="manufacturer", 
                       barmode='overlay',
                       histnorm=histnorm,
                       title=f"Price Distribution: {manuf_1} vs {manuf_2}",
                       color_discrete_sequence=['#EF553B', '#636EFA']) # Red and Blue

st.plotly_chart(fig_comp, use_container_width=True)

# Graph 3: Condition vs Year ---
st.header('Histogram of condition vs model_year')

# Filter out rows with missing year or condition for a cleaner plot
condition_data = car_data.dropna(subset=['model_year', 'condition'])

fig_cond = px.histogram(condition_data, 
                       x="model_year", 
                       color="condition",
                       title="Vehicle Condition by Model Year",
                       color_discrete_sequence=px.colors.qualitative.Prism)

st.plotly_chart(fig_cond, use_container_width=True)
