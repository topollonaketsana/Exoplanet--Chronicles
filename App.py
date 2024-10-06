import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import time

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv('C:/Users/topol/Exoplanet--Chronicles/data/kepler.csv').head(50)

data = load_data()

# Generate options for the dropdown
options = ['None'] + [f"KOI-{i+1}" for i in range(len(data))]

# Set up layout with selection bar on the left
st.sidebar.title("Select Kepler Objects")
selected_systems = st.sidebar.multiselect('Select Kepler Objects', options)

# Fixed stars in the background
np.random.seed(42)
stars_x = np.random.uniform(-400, 400, size=1000)  # Increased canvas size
stars_y = np.random.uniform(-400, 400, size=1000)
stars_z = np.random.uniform(-400, 400, size=1000)

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

    for selected_system in selected_systems:
        system_index = int(selected_system.split('-')[1]) - 1
        system_data = data.iloc[system_index]

        # Parent star with large radius (yellow)
        star_radius = system_data['koi_srad'] * 20  # scale up for visibility
        fig.add_trace(go.Scatter3d(
            x=[0], y=[0], z=[0],
            mode='markers',
            marker=dict(size=star_radius, color='yellow'),
            name=f"Star KOI-{system_index+1}"
        ))

        # Exoplanet data: orbital speed, size, and position
        orbital_period_days = system_data['koi_period']
        orbital_period_seconds = orbital_period_days * 24 * 3600  # Convert to seconds
        angular_speed = 2 * np.pi / orbital_period_seconds  # radians per second

        exoplanet_radius = (system_data['koi_depth'] / 100) * 15  # Scale size (make it smaller)
        exoplanet_size = max(exoplanet_radius, 3)  # Minimum size

        # Ensure exoplanet radius is smaller than star radius
        if exoplanet_size >= star_radius:
            exoplanet_size = star_radius / 2  # Ensure exoplanet is smaller

        # Orbit radius based on stellar radius
        orbit_radius = system_data['koi_srad'] * 50  # Increase the scale

        # Calculate planet position based on the current angle
        planet_x = orbit_radius * np.cos(current_angle)
        planet_y = orbit_radius * np.sin(current_angle)
        planet_z = 0

        fig.add_trace(go.Scatter3d(
            x=[planet_x], y=[planet_y], z=[planet_z],
            mode='markers',
            marker=dict(size=exoplanet_size, color='red'),
            name=f"Exoplanet KOI-{system_index+1}"
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
        width=1000,  # Increased canvas size
        height=1000
    )

    return fig

# Simulate the movement of the planets over time
current_angle = 0

# Create a placeholder to hold the plot
plot_placeholder = st.empty()

# Control animation with selected systems
if selected_systems:
    # Set the refresh rate for the animation
    refresh_rate = st.slider("Animation Speed (seconds)", min_value=0.01, max_value=1.0, value=0.1)
    
    # Run the animation loop for a few seconds
    start_time = time.time()
    while True:
        fig = create_3d_plot(selected_systems, current_angle)
        plot_placeholder.plotly_chart(fig)

        # Update angular speed for the animation
        angular_speeds = []
        for selected_system in selected_systems:
            system_index = int(selected_system.split('-')[1]) - 1
            orbital_period_days = data.iloc[system_index]['koi_period']
            orbital_period_seconds = orbital_period_days * 24 * 3600
            angular_speeds.append(2 * np.pi / orbital_period_seconds)

        # Increment angle based on average angular speed
        current_angle += np.mean(angular_speeds) * 0.1
        
        # Control the refresh rate
        time.sleep(refresh_rate)  # Use the slider value for control

        # Stop the loop after 10 seconds for analysis
        if time.time() - start_time > 10:
            break

    # Allow user to interact and analyze the plot before resuming
    st.write("You can now analyze the plot. Adjust the selections or parameters, and click 'Run' to resume.")
    
else:
    st.write("Please select at least one Kepler Object to visualize.")
    plot_placeholder.empty()  # Clear the plot placeholder if no selection
