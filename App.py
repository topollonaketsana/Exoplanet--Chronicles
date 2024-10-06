import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import time

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv('data/kepler.csv')

data = load_data()

# Generate options for the dropdown (with 'None' as an option)
options = ['None'] + [f"KOI-{i+1}" for i in range(len(data))]

# Title and Dropdown
st.title("Kepler Exoplanet Visualization with Orbital Motion")
selected_systems = st.multiselect('Select Kepler Objects', options)

# Fixed stars in the background
np.random.seed(42)
stars_x = np.random.uniform(-200, 200, size=500)
stars_y = np.random.uniform(-200, 200, size=500)
stars_z = np.random.uniform(-200, 200, size=500)

# Create the 3D plot
def create_3d_plot(selected_systems, current_angle):
    fig = go.Figure()

    # Background stars (static)
    fig.add_trace(go.Scatter3d(
        x=stars_x, y=stars_y, z=stars_z,
        mode='markers',
        marker=dict(size=2, color='white', opacity=0.9),
        name="Stars"
    ))

    # Average star size (fixed)
    average_star_size = 30  # Fixed size for visibility

    for selected_system in selected_systems:
        system_index = int(selected_system.split('-')[1]) - 1
        system_data = data.iloc[system_index]

        # Add the central yellow star
        fig.add_trace(go.Scatter3d(
            x=[0], y=[0], z=[0],
            mode='markers',
            marker=dict(size=average_star_size, color='yellow'),
            name=f"Star for KOI-{system_index+1}"
        ))

        # Get the orbital period and calculate angular speed
        orbital_period_days = system_data['koi_period']
        orbital_period_seconds = orbital_period_days * 24 * 3600  # Convert to seconds
        angular_speed = 2 * np.pi / orbital_period_seconds  # radians per second

        # Scale exoplanet size based on the period and assign radius
        exoplanet_radius = (system_data['koi_depth'] / 100) * 20  # Example scaling based on depth (arbitrary)
        exoplanet_size = max(exoplanet_radius, 5)  # Ensure minimum visibility

        # Orbit radius calculation (scaled down for visualization)
        orbit_radius = (system_data['koi_srad'] * 20)  # Using star radius to determine orbit radius

        # Calculate planet position based on the current angle
        planet_x = orbit_radius * np.cos(current_angle)
        planet_y = orbit_radius * np.sin(current_angle)
        planet_z = 0

        fig.add_trace(go.Scatter3d(
            x=[planet_x], y=[planet_y], z=[planet_z],
            mode='markers',
            marker=dict(size=exoplanet_size, color='red'),
            name=f'Exoplanet KOI-{system_index+1}'
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
        title="Selected Kepler Exoplanet Systems",
        margin=dict(l=0, r=0, b=0, t=40),
        width=900,
        height=900
    )

    return fig

# Simulate the movement of the planets over time
current_angle = 0

# Create a placeholder to hold the plot
plot_placeholder = st.empty()

# Control animation with selected systems
# Inside the while loop where planets are animated
if selected_systems:
    while True:
        fig = create_3d_plot(selected_systems, current_angle)
        plot_placeholder.plotly_chart(fig)

        # Update angular speed based on the current selection
        angular_speed = []
        for selected_system in selected_systems:
            system_index = int(selected_system.split('-')[1]) - 1
            orbital_period_days = data.iloc[system_index]['koi_period']
            orbital_period_seconds = orbital_period_days * 24 * 3600  # Convert to seconds
            angular_speed.append(2 * np.pi / orbital_period_seconds)  # radians per second

        # Increment angle based on the average angular speed of selected exoplanets
        current_angle += np.mean(angular_speed) * 0.1  # Average for all selected systems
        time.sleep(0.1)  # Delay to control speed of motion
else:
    st.write("Please select at least one Kepler Object to visualize.")
