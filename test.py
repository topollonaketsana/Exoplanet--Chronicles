import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import time

# Set page configuration at the very beginning
st.set_page_config(layout="wide")

# Load Data
@st.cache_data
def load_data():
    data = pd.read_csv('C:/Users/topol/Exoplanet--Chronicles/data/kepler.csv')
    return data.head(50)  # Limit to first 50 exoplanets

data = load_data()

# Title
st.title("Kepler Exoplanet Interactive Visualization")
st.markdown("Explore the first 50 exoplanets discovered by the Kepler mission in this interactive 3D visualization.")

# Sidebar for system selection
st.sidebar.header("Select Kepler Objects of Interest (KOI)")
selected_systems = st.sidebar.multiselect('Choose multiple systems:', 
                                          options=data.index.tolist(),
                                          default=[])

# Visualization settings
st.sidebar.header("Visualization Settings")
time_multiplier = st.sidebar.slider("Time Speed", 0.1, 10.0, 1.0)

# Constants
G = 6.67430e-11  # Gravitational constant
M_sun = 1.989e30  # Mass of the Sun in kg
R_earth = 6371  # Radius of Earth in km
AU = 149597870.7  # 1 AU in km

# Generate background stars
np.random.seed(42)
num_stars = 10000
stars_x = np.random.uniform(-100, 100, size=num_stars)
stars_y = np.random.uniform(-100, 100, size=num_stars)
stars_z = np.random.uniform(-100, 100, size=num_stars)

# Create the 3D plot
def create_3d_plot(selected_systems, time):
    fig = go.Figure()

    # Background stars
    fig.add_trace(go.Scatter3d(
        x=stars_x, y=stars_y, z=stars_z,
        mode='markers',
        marker=dict(size=0.5, color='white', opacity=0.8),
        name="Background Stars"
    ))

    for system_index in selected_systems:
        system_data = data.iloc[system_index]

        # Calculate star size relative to Earth
        star_radius = system_data['koi_srad'] * 109.2  # 1 Solar radius = 109.2 Earth radii
        star_size = max(star_radius, 5)  # Ensure minimum visibility

        # Add the central star (yellow)
        fig.add_trace(go.Scatter3d(
            x=[0], y=[0], z=[0],
            mode='markers',
            marker=dict(size=star_size, color='yellow'),
            name=f"Star KOI-{system_index+1}"
        ))

        # Calculate planet properties
        planet_radius = system_data['koi_prad']  # Already in Earth radii
        planet_size = max(planet_radius * 2, 2)  # Scale up for visibility, ensure minimum size
        orbital_period = system_data['koi_period'] * 24 * 3600  # seconds
        
        # Calculate semi-major axis using Kepler's Third Law
        semi_major_axis = ((orbital_period**2 * G * M_sun) / (4 * np.pi**2))**(1/3) / 1000  # km

        # Calculate current position
        angular_speed = 2 * np.pi / orbital_period
        current_angle = (angular_speed * time) % (2 * np.pi)
        planet_x = semi_major_axis * np.cos(current_angle) / AU
        planet_y = semi_major_axis * np.sin(current_angle) / AU
        planet_z = 0

        # Add the planet
        fig.add_trace(go.Scatter3d(
            x=[planet_x], y=[planet_y], z=[planet_z],
            mode='markers',
            marker=dict(size=planet_size, color='red'),
            name=f'Exoplanet KOI-{system_index+1}'
        ))

        # Add orbit path
        theta = np.linspace(0, 2*np.pi, 100)
        x = (semi_major_axis / AU) * np.cos(theta)
        y = (semi_major_axis / AU) * np.sin(theta)
        z = np.zeros(100)
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z,
            mode='lines',
            line=dict(color='white', width=1),
            name=f'Orbit KOI-{system_index+1}'
        ))

    # Update layout for better visualization
    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False, range=[-2, 2]),
            yaxis=dict(visible=False, range=[-2, 2]),
            zaxis=dict(visible=False, range=[-2, 2]),
            aspectmode='cube'
        ),
        paper_bgcolor="black",
        scene_bgcolor="black",
        title="Kepler Exoplanet Systems",
        margin=dict(l=0, r=0, b=0, t=40),
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01,
            font=dict(color="white")
        ),
        updatemenus=[{
            'buttons': [
                {'args': [None, {'frame': {'duration': 0, 'redraw': False},
                                 'fromcurrent': True, 'transition': {'duration': 0}}],
                 'label': 'Play',
                 'method': 'animate'},
                {'args': [[None], {'frame': {'duration': 0, 'redraw': False},
                                   'mode': 'immediate',
                                   'transition': {'duration': 0}}],
                 'label': 'Pause',
                 'method': 'animate'}
            ],
            'direction': 'left',
            'pad': {'r': 10, 't': 87},
            'showactive': False,
            'type': 'buttons',
            'x': 0.1,
            'xanchor': 'right',
            'y': 0,
            'yanchor': 'top'
        }]
    )

    return fig

# Create a placeholder to hold the plot
plot_placeholder = st.empty()

# Function to run the animation
def run_animation(selected_systems, duration=10):
    start_time = time.time()
    while time.time() - start_time < duration:
        current_time = (time.time() - start_time) * 86400 * time_multiplier  # Convert to seconds
        fig = create_3d_plot(selected_systems, current_time)
        plot_placeholder.plotly_chart(fig, use_container_width=True)
        time.sleep(0.1)  # Small delay to control frame rate

# Initial plot and animation
if selected_systems:
    run_animation(selected_systems)
else:
    st.write("Please select at least one Kepler Object to visualize.")

# Display system information
if selected_systems:
    st.subheader("Selected System Information")
    for system_index in selected_systems:
        system_data = data.iloc[system_index]
        st.write(f"**KOI-{system_index+1}**")
        st.write(f"Orbital Period: {system_data['koi_period']:.2f} days")
        st.write(f"Planet Radius: {system_data['koi_prad']:.2f} Earth radii")
        st.write(f"Star Radius: {system_data['koi_srad']:.2f} Solar radii")
        
        # Calculate orbital speed
        orbital_period = system_data['koi_period'] * 24 * 3600  # seconds
        semi_major_axis = ((orbital_period**2 * G * M_sun) / (4 * np.pi**2))**(1/3)  # meters
        orbital_speed = 2 * np.pi * semi_major_axis / orbital_period  # m/s
        st.write(f"Orbital Speed: {orbital_speed/1000:.2f} km/s")
        
        st.write("---")

# Add a button to restart the animation
if st.button("Restart Animation"):
    run_animation(selected_systems)