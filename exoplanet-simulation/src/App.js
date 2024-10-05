import React, { useRef, useState, useEffect, startTransition } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { OrbitControls, Text, Stars } from '@react-three/drei';
import * as d3 from 'd3';
import * as THREE from 'three';

const App = () => {
  const [selectedSystem, setSelectedSystem] = useState(""); // Initialize to an empty string
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true); // State for loading indicator

  useEffect(() => {
    // Load CSV file and convert it to the desired structure
    d3.csv('/data/kepler.csv')
      .then((rawData) => {
        // Take only the first 100 records
        const formattedData = rawData.slice(0, 100).map((d) => ({
          koi_period: +d.koi_period, // Orbital period
          koi_srad: +d.koi_srad,     // Stellar radius
          koi_kepmag: +d.koi_kepmag, // Stellar magnitude (brightness)
          koi_time0bk: +d.koi_time0bk, // Epoch
          ra: +d.ra,   // Right ascension
          dec: +d.dec, // Declination
        }));
        setData(formattedData);
        setLoading(false); // Set loading to false after data is loaded
      })
      .catch((error) => {
        console.error('Error loading CSV:', error); // Error handling
        setLoading(false); // Set loading to false on error
      });
  }, []);

  const Exoplanet = ({ planet, orbitRadius }) => {
    const ref = useRef(null);

    useFrame(({ clock }) => {
      const t = clock.getElapsedTime();
      const angle = (t * Math.PI * 2) / planet.koi_period;
      ref.current.position.x = Math.cos(angle) * orbitRadius;
      ref.current.position.z = Math.sin(angle) * orbitRadius;
    });

    return (
      <mesh ref={ref}>
        <sphereGeometry args={[planet.koi_srad * 0.2, 32, 32]} /> {/* Adjusted size for visibility */}
        <meshStandardMaterial color="red" /> {/* Changed color to red for better visibility */}
        <Text position={[0, planet.koi_srad * 0.2, 0]} fontSize={0.2} color="white">
          {`Mag: ${planet.koi_kepmag}`}
        </Text>
      </mesh>
    );
  };

  const Star = ({ radius }) => (
    <mesh>
      <sphereGeometry args={[radius * 2, 60, 60]} />
      <meshBasicMaterial color="yellow" />
    </mesh>
  );

  const OrbitLine = ({ radius }) => (
    <mesh rotation={[-Math.PI / 2, 0, 0]}>
      <ringGeometry args={[radius, radius + 0.01, 64]} />
      <meshBasicMaterial color="white" opacity={0.2} transparent side={THREE.DoubleSide} />
    </mesh>
  );

  if (loading) {
    return <div>Loading...</div>; // Loading indicator
  }

  return (
    <div className="w-full h-full bg-black flex flex-col"> {/* Adjusted to full height */}
      <div className="h-full"> {/* Adjusted to take up full height */}
        <Canvas camera={{ position: [0, 50, 50], fov: 60 }}>
          <ambientLight intensity={0.5} />
          <pointLight position={[10, 10, 10]} />
          <Stars radius={200} depth={50} count={8000} factor={4} fade />

          {selectedSystem !== "" && data[selectedSystem] && (
            <>
              <Star radius={data[selectedSystem].koi_srad * 0.5 || 1} /> {/* Adjusted star size */}
              <Exoplanet planet={data[selectedSystem]} orbitRadius={(selectedSystem + 1) * 5} />
              <OrbitLine radius={(selectedSystem + 1) * 5} />
            </>
          )}

          <OrbitControls />
        </Canvas>
      </div>

      {/* User selection for the data visualization */}
      <div className="absolute top-4 left-4 bg-gray-800 text-white p-4 rounded z-10"> {/* Repositioned */}
        <h2 className="text-xl mb-2">Kepler Data Visualization</h2>
        <select
          className="bg-gray-700 p-2 rounded"
          value={selectedSystem}
          onChange={(e) => {
            const selectedIndex = e.target.value;
            startTransition(() => {
              setSelectedSystem(selectedIndex); // Update the state with the selected index
            });
          }}
        >
          <option value="">Select a Kepler Object</option> {/* Default option */}
          {data.map((system, index) => (
            <option key={index} value={index}>
              Kepler Object {index + 1} (Period: {system.koi_period} days)
            </option>
          ))}
        </select>
      </div>
    </div>
  );
}

export default App;

