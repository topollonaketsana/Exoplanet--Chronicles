import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv('data/kepler.csv')

data = load_data()

# Add a "None" option to the dropdown for no preselection
options = ['None'] + [f"KOI-{i+1}" for i in range(len(data))]

# Title and Dropdown
st.title("Kepler Exoplanet Visualization with Orbital Motion")
selected_system = st.selectbox('Select a Kepler Object', options)

if selected_system != 'None':
    system_index = int(selected_system.split('-')[1]) - 1

    st.write(f"Selected Kepler Object: KOI-{system_index+1}")
    st.write("Orbital Period (days):", data['koi_period'][system_index])
    st.write("Stellar Radius (solar radii):", data['koi_srad'][system_index])
    st.write("Transit Depth:", data['koi_depth'][system_index])
    st.write("Right Ascension:", data['ra'][system_index])
    st.write("Declination:", data['dec'][system_index])

    # Function to calculate planet radius from transit depth
    def calculate_planet_radius(stellar_radius, transit_depth):
        if np.isnan(transit_depth) or stellar_radius == 0:
            return 0
        return stellar_radius * np.sqrt(transit_depth / 100)  # Depth in percentage

    # Function to calculate orbital velocity (v_r = 2 * pi * R / P)
    def calculate_velocity(orbit_radius, period):
        if period == 0:
            return 0
        period_seconds = period * 24 * 3600  # Convert period to seconds
        return (2 * np.pi * orbit_radius) / period_seconds

    # Create the 3D plot
    def create_3d_plot(system_data):
        fig = go.Figure()

        # Add the central yellow star
        star_radius = system_data['koi_srad']  # Stellar radius (solar radii)
        fig.add_trace(go.Scatter3d(
            x=[0], y=[0], z=[0],
            mode='markers',
            marker=dict(size=star_radius * 30, color='yellow'),  # Scaled for visibility
            name="Star"
        ))

        # Transit depth and planet radius calculation
        transit_depth = system_data['koi_depth']
        planet_radius = calculate_planet_radius(star_radius, transit_depth)

        # Check if planet radius is valid (Rp < Rs)
        if planet_radius >= star_radius:
            st.error("Invalid planet radius: Exceeds stellar radius. Cannot visualize this system.")
            return fig

        # Orbit radius (scaled down for visualization purposes)
        orbit_radius = system_data['koi_period'] * 0.5  # Arbitrary scaling factor to fit on canvas

        # Create orbit path for the planet
        angle = np.linspace(0, 2 * np.pi, 100)
        x_orbit = orbit_radius * np.cos(angle)
        y_orbit = orbit_radius * np.sin(angle)
        z_orbit = np.zeros_like(angle)

        # Planet velocity calculation
        velocity = calculate_velocity(orbit_radius, system_data['koi_period'])
        st.write(f"Orbital Velocity: {velocity:.2f} m/s")

        # Orbit path (white line)
        fig.add_trace(go.Scatter3d(
            x=x_orbit, y=y_orbit, z=z_orbit,
            mode='lines', line=dict(color='white', width=3),
            name='Orbit'
        ))

        # Initial position of planet on orbit
        current_angle = np.pi / 4
        planet_x = orbit_radius * np.cos(current_angle)
        planet_y = orbit_radius * np.sin(current_angle)
        planet_z = 0

        fig.add_trace(go.Scatter3d(
            x=[planet_x], y=[planet_y], z=[planet_z],
            mode='markers',
            marker=dict(size=planet_radius * 30, color='red'),  # Scaled for visibility
            name='Exoplanet'
        ))

        # Generate random stars in the background (Fixed)
        np.random.seed(42)
        stars_x = np.random.uniform(-200, 200, size=500)
        stars_y = np.random.uniform(-200, 200, size=500)
        stars_z = np.random.uniform(-200, 200, size=500)
        fig.add_trace(go.Scatter3d(
            x=stars_x, y=stars_y, z=stars_z,
            mode='markers',
            marker=dict(size=2, color='white', opacity=0.9),
            name="Stars"
        ))

        # Hide axes and background grid
        fig.update_layout(
            scene=dict(
                xaxis=dict(visible=False),
                yaxis=dict(visible=False),
                zaxis=dict(visible=False)
            ),
            paper_bgcolor="black",
            scene_bgcolor="black",
            title=f"KOI-{system_index+1} System",
            margin=dict(l=0, r=0, b=0, t=40),
            width=900,
            height=900
        )

        return fig

    # Plot the system
    fig = create_3d_plot(data.iloc[system_index])
    st.plotly_chart(fig)

else:
    st.write("Please select a Kepler Object to visualize.")
