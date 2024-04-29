import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Load the dataset

def load_data(csv):
    data = pd.read_csv(csv)
    return data

df = load_data('data/FuelConsumption.csv')
df.head(5)

st.sidebar.header("Filters")

#Make filter
make_filter = st.sidebar.selectbox("Make", df['MAKE'].unique())
model_filter = st.sidebar.selectbox("Model", df['MODEL'].unique())
vehicle_class_filter = st.sidebar.selectbox("Vehicle Class", df['VEHICLE CLASS'].unique())
# engine_size = st.slider("Engine Size (cc)", df['ENGINE SIZE'].min(), df['ENGINE SIZE'].max(), df['ENGINE SIZE'].median())
transmission_type = st.selectbox("Transmission Type", df['TRANSMISSION'].unique())
fuel_type = st.selectbox("Fuel Type", df['FUEL'].unique())

filtered_df = df[(df['MAKE'] == make_filter) & 
                 (df['MODEL'] == model_filter) & 
                 (df['VEHICLE CLASS'] == vehicle_class_filter) & 
                #  (df['ENGINE SIZE'] == engine_size) & 
                 (df['TRANSMISSION'] == transmission_type) & 
                 (df['FUEL'] == fuel_type)]

st.write("Filtered Results:")
st.write(filtered_df)