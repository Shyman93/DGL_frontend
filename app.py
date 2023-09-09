import folium
import streamlit as st
from folium.plugins import Draw

from streamlit_folium import st_folium

# Set the title of your Streamlit app
st.title("Forest Detection App")

# Add introductory text
st.write(
    "Welcome to the Forest Detection App! This app allows you to select an area on the map "
    "and detect whether there is a forest present or not. You can also provide a date for "
    "the satellite image you'd like to analyze."
)

# Create a Folium map
m = folium.Map(location=[39.949610, -75.150282], zoom_start=10)

# Add the Draw control to the map
Draw(export=True).add_to(m)

# Display the map in Streamlit
c1, c2 = st.columns(2)
with c1:
    output = st_folium(m, width=700, height=500)

with c2:
    st.write("Map Output")


    lst = [output["bounds"]["_southWest"]["lat"], output["bounds"]["_southWest"]["lng"], output["bounds"]["_northEast"]["lat"], output["bounds"]["_northEast"]["lng"]]
    st.write(lst)
# Add a date input for satellite image analysis
selected_date = st.date_input("Select a date for satellite image analysis")

# Add a button to initiate analysis
if st.button("Analyze"):
    # Replace this section with your forest detection logic
    st.write(f"Analyzing satellite image for {selected_date}...")
    # You can add code here to analyze the selected area for the presence of a forest.
