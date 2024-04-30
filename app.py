import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

# URL of the image to display
image_url = "https://1000logos.net/wp-content/uploads/2023/04/Japanese-Car-Brands-manufacturer-car-companies-logos.png"

# Display the image using st.image()
st.image(image_url, width=700)

#Load the dataset

def load_data(csv):
    data = pd.read_csv(csv)
    return data

df = load_data('data/FuelConsumption.csv')
df.head(5)

st.markdown("""
## Fuel Consumption Analysis: Know Your Car's Appetite!
Welcome to the ultimate fuel consumption analysis app! :bar_chart: Ever wondered how much your car is really guzzling? :thinking_face: Well, buckle up and get ready to dive deep into the world of MPGs, fuel efficiency, and saving money at the pump! :money_with_wings:
With this app, you'll gain insights that will make you the envy of all your car-loving friends. From interactive charts :chart_with_upwards_trend: to personalized recommendations :dart:, we've got you covered.
So, rev up your engines and let's explore the fascinating world of fuel consumption together! :checkered_flag:
""")

vehicle_class_filter = st.selectbox("Choose a Vehicle Class", df['VEHICLE CLASS'].unique())
filtered_df = df[
                 (df['VEHICLE CLASS'] == vehicle_class_filter) 
                #  (df['ENGINE SIZE'] == engine_size) & 
                 ]
# st.write(filtered_df.columns)

tab1, tab2 = st.tabs(["Distributions", "Comparisons"])

with tab1:

   # Create a filter box for vehicle class
   bar_chart = alt.Chart(filtered_df).mark_bar().encode(
    x='MAKE',  # Use the column name for the x-axis
    y='FUEL CONSUMPTION',  # Use the column name for the y-axis
    color='VEHICLE CLASS',  # Use the column name for the color encoding
    tooltip=[
        alt.Tooltip('VEHICLE CLASS', title='Vehicle Class'),
        alt.Tooltip('MAKE', title='Car Make'),
        alt.Tooltip('FUEL CONSUMPTION', title='Mean Fuel Consumption', format='.2f')
    ]
).properties(
    title=f'Fuel Consumption by Car Make for {vehicle_class_filter}'
)

# Display the bar chart in Streamlit
   st.altair_chart(bar_chart, use_container_width=True)
   scatter_chart = alt.Chart(df).mark_circle().encode(
    x='ENGINE SIZE',  
    y='FUEL CONSUMPTION',  
    tooltip=['MAKE', 'MODEL', 'ENGINE SIZE', 'FUEL CONSUMPTION']
).properties(
    title='Scatter Plot of Engine Size vs. Fuel Consumption')
   # Display the scatter plot in Streamlit
   st.altair_chart(scatter_chart, use_container_width=True)





with tab2:
   st.header("Detailed Comparison")
   col1, col2 = st.columns(2)
   with col1:
        st.metric("Avg Fuel Consumption", round(filtered_df['FUEL CONSUMPTION'].mean(), 3), "Liters per 100 Km")
        st.markdown("***")
        make_filter01 = st.selectbox("Make", filtered_df['MAKE'].unique(), key='makefilter01')
        model_filter01 = st.selectbox("Model", filtered_df['MODEL'].where(filtered_df['MAKE'] == make_filter01).unique(), key='modelfilter01')
        filteredData01 = filtered_df[
                    (filtered_df['MAKE'] == make_filter01 ) &
                    (filtered_df['MODEL'] == model_filter01)
                    ]
        
   with col2:
        st.metric("Avg CO2 Emission", round(filtered_df['COEMISSIONS '].mean(), 3), "Grams per 100 Km")
        st.markdown("***")
        make_filter02 = st.selectbox("Make", filtered_df['MAKE'].unique(), key='makefilter02')
        model_filter02 = st.selectbox("Model", filtered_df['MODEL'].where(filtered_df['MAKE'] == make_filter02).unique() , key='modelfilter02')
        filteredData02 = filtered_df[
                    (filtered_df['MAKE'] == make_filter02 ) &
                    (filtered_df['MODEL'] == model_filter02)
                    ]
        

    # Create a Streamlit app
   st.title('Comparing Fuel Consumption and CO2 Emission of Two Vehicles')

    # Combine the dataframes
   data = pd.concat([filteredData01, filteredData02], ignore_index=True)

    # Create a bar chart
   col3, col4 = st.columns(2)
   with col3:
        bar_chart = alt.Chart(data).mark_bar().encode(
        x='MAKE',  # Use the new column name for the x-axis
        y='FUEL CONSUMPTION',
        tooltip=['MAKE', 'MODEL', 'FUEL CONSUMPTION']
    ).properties(
        title='Fuel Consumption Comparison',
        width=100, 
        height=500  
    )

    # Display the bar chart in Streamlit
        st.altair_chart(bar_chart, use_container_width=True)

   with col4:
        bar_chart2 = alt.Chart(data).mark_bar().encode(
        x='MAKE',  # Use the new column name for the x-axis
        y='COEMISSIONS ', 
        tooltip=['MAKE', 'MODEL', 'COEMISSIONS ']
    ).properties(
        title='CO2 Emissions Comparison',
        width=100, 
        height=500  
    )

        st.altair_chart(bar_chart2, use_container_width=True)





   









