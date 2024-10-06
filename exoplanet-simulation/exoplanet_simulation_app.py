import numpy as np
import matplotlib.pyplot as plt
from astroquery.nasa_exoplanet_archive import NasaExoplanetArchive

# Function to fetch exoplanet data using astroquery
def fetch_exoplanet_data():
    # Query for exoplanets with Kepler data
    planets = NasaExoplanetArchive.query_criteria(table="exoplanets", where="pl_hostname='Kepler-11'")
    return planets

# Function to calculate the position of a planet in its orbit using Kepler's laws
def calculate_orbit(semimajor_axis, eccentricity, period, time):
    # True anomaly (angle in orbit) assuming circular orbit for simplicity
    theta = (2 * np.pi * time) / period
    r = (semimajor_axis * (1 - eccentricity**2)) / (1 + eccentricity * np.cos(theta))
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

# Function to simulate the exoplanet system
def simulate_exosky():
    planets = fetch_exoplanet_data()
    
    # Initialize the plot
    fig, ax = plt.subplots()
    
    # Star at the center
    ax.plot(0, 0, 'yo', label='Host Star')
    
    # Simulate each planet
    times = np.linspace(0, 2 * np.pi, 1000)  # simulate for one orbital period
    for planet in planets:
        semimajor_axis = planet['pl_orbsmax']  # Semi-major axis (AU)
        eccentricity = planet['pl_orbeccen']   # Orbital eccentricity
        period = planet['pl_orbper']           # Orbital period (days)
        
        # Calculate orbit positions
        x_vals = []
        y_vals = []
        for time in times:
            x, y = calculate_orbit(semimajor_axis, eccentricity, period, time)
            x_vals.append(x)
            y_vals.append(y)
        
        # Plot the planet's orbit
        ax.plot(x_vals, y_vals, label=f'{planet["pl_name"]}')
    
    # Set plot properties
    ax.set_aspect('equal')
    ax.set_xlabel('X (AU)')
    ax.set_ylabel('Y (AU)')
    ax.set_title('Exoplanetary System Simulation')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    simulate_exosky()
