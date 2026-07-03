# Import necessary libraries
import pandas as pd
import plotly.express as px
import streamlit as st

# Read the data
car_data = pd.read_csv('vehicles_us.csv')

# Create a manufacturer column
car_data['manufacturer'] = car_data['model'].apply(lambda x: x.split()[0])

st.header('Car Advertisement Data Dashboard')

# Graph 1: Basic Visualizations ---
st.write('### Basic Exploratory Data Analysis')

# Checkbox for Histogram
build_histogram = st.checkbox('Show Odometer Histogram')
if build_histogram:
    st.write('Creating a histogram for the odometer column')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Checkbox for Scatterplot
build_scatter = st.checkbox('Show Price vs Odometer Scatterplot')
if build_scatter:
    st.write('Creating a scatterplot for price vs odometer')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)


# Graph 2: Manufacturer Comparison ---
st.header('Compare price distribution between manufacturers')

# Get list of unique manufacturers
manuf_list = sorted(car_data['manufacturer'].unique())

# Dropdowns for manufacturers
manuf_1 = st.selectbox('Select manufacturer 1', manuf_list, index=manuf_list.index('chevrolet') if 'chevrolet' in manuf_list else 0)
manuf_2 = st.selectbox('Select manufacturer 2', manuf_list, index=manuf_list.index('ford') if 'ford' in manuf_list else 1)

# Filter the data
df_filtered = car_data[car_data['manufacturer'].isin([manuf_1, manuf_2])]

# Checkbox for normalization
normalize = st.checkbox('Normalize histogram', value=True)
histnorm_val = 'percent' if normalize else None

# Create the histogram
fig_compare = px.histogram(df_filtered, 
                           x='price', 
                           color='manufacturer', 
                           histnorm=histnorm_val, 
                           barmode='overlay',
                           color_discrete_sequence=['#EF553B', '#636EFA'], # Red and Blue for contrast
                           title=f"Price distribution: {manuf_1} vs {manuf_2}")

# Display the chart
st.plotly_chart(fig_compare, use_container_width=True)

# Graph 3: Condition vs Model Year ---
st.header('Histogram of condition vs model_year')

# Create a histogram for condition vs model_year
# We use a distinct color sequence for the conditions
fig_condition = px.histogram(car_data, 
                             x='model_year', 
                             color='condition',
                             title='Distribution of car conditions by model year',
                             color_discrete_sequence=px.colors.qualitative.Prism)

# Display the chart
st.plotly_chart(fig_condition, use_container_width=True)
