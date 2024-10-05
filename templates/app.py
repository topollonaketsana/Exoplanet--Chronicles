import streamlit as st
import pandas as pd
from src.transit_plot import create_transit_plot
from src.data_processing import load_data, load_model, predict_exoplanet

# Load data and model
try:
    df = load_data('C:/Users/topol/Exoplanet--Chronicles/data/data_TOI.csv')
    model = load_model('C:/Users/topol/Exoplanet--Chronicles/notebooks/model.pkl')
except Exception as e:
    st.error(f"Error loading data or model: {e}")
    st.stop()  # Stop execution if loading fails

# Sidebar inputs
star_magnitude = st.sidebar.slider('Star Brightness (Magnitude)', min_value=10.0, max_value=16.0)
planet_radius = st.sidebar.slider('Planet Radius (Relative to Earth)', min_value=0.5, max_value=2.5)
orbital_period = st.sidebar.slider('Orbital Period (Days)', min_value=1, max_value=365)

# Display transit plot
st.write("### Transit Light Curve")
create_transit_plot(orbital_period, planet_radius, star_magnitude)

# Machine learning prediction
st.write("### Exoplanet Detection")
prediction = predict_exoplanet(model, star_magnitude, planet_radius, orbital_period, df)

# Display prediction result
if prediction == 1:
    st.success("Prediction: Exoplanet Detected!")
else:
    st.warning("Prediction: No Exoplanet Detected.")




import numpy as np
import matplotlib.pyplot as plt

# Define parameters for the star and planet
star_radius = 1.0  # Star radius (arbitrary units)
planet_radius = 0.1  # Planet radius (arbitrary units)
transit_duration = 0.1  # Duration of transit (arbitrary time units)
time = np.linspace(0, 1, 500)  # Time array from 0 to 1

# Create a model for the light curve
def light_curve(t):
    # Basic light curve with a dip during the transit
    dip = np.where((t >= 0.4) & (t <= 0.4 + transit_duration), 1 - (planet_radius / star_radius), 1)
    return dip

# Generate light curve data
brightness = light_curve(time)

# Plot the light curve
plt.figure(figsize=(10, 5))
plt.plot(time, brightness, color='blue')
plt.title('Light Curve of Star with Transiting Exoplanet')
plt.xlabel('Time (arbitrary units)')
plt.ylabel('Relative Brightness')
plt.ylim(0.8, 1.1)  # Set y-limits for better visualization

# Add a visual representation of the star and planet
plt.scatter(0.4 + transit_duration / 2, 1 - (planet_radius / star_radius), color='black', s=100, label='Exoplanet')  # Planet
plt.scatter(0.5, 1, color='yellow', s=1000, label='Star')  # Star
plt.legend()

# Show the plot
plt.grid()
plt.axhline(1, color='gray', linestyle='--', lw=0.5)  # Line at normal brightness
plt.show()
