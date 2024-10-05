import React, { useRef, useState, useEffect } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { OrbitControls, Text, Stars } from '@react-three/drei';
import * as d3 from 'd3';
import * as THREE from 'three';

// Load the actual Kepler data CSV
const ExoplanetSimulation = () => {
    const [selectedSystem, setSelectedSystem] = useState(""); // Initialize as an empty string
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true); // State for loading indicator

    useEffect(() => {
        // Load CSV file and convert it to the desired structure
        d3.csv('C:/Users/topol/Exoplanet--Chronicles/exoplanet-simulation/public/data/kepler.csv')
            .then((rawData) => {
                const formattedData = rawData.map((d) => ({
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
                <sphereGeometry args={[planet.koi_srad * 0.1, 32, 32]} />
                <meshStandardMaterial color="blue" />
                <Text position={[0, planet.koi_srad * 0.15, 0]} fontSize={0.5} color="white">
                    {`Mag: ${planet.koi_kepmag}`}
                </Text>
            </mesh>
        );
    };

    const Star = ({ radius }) => (
        <mesh>
            <sphereGeometry args={[radius, 32, 32]} />
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
        <div className="w-full h-screen bg-black">
            <Canvas camera={{ position: [0, 20, 20], fov: 60 }}>
                <ambientLight intensity={0.5} />
                <pointLight position={[10, 10, 10]} />
                <Stars radius={100} depth={50} count={5000} factor={4} fade />

                {data.map((system, idx) => (
                    <React.Fragment key={idx}>
                        <Star radius={system.koi_srad || 1} />
                        <Exoplanet planet={system} orbitRadius={(idx + 1) * 5} />
                        <OrbitLine radius={(idx + 1) * 5} />
                    </React.Fragment>
                ))}

                <OrbitControls />
            </Canvas>

            {/* User selection for the data visualization */}
            <div className="absolute top-4 left-4 bg-gray-800 text-white p-4 rounded">
                <h2 className="text-xl mb-2">Kepler Data Visualization</h2>
                <select
                    className="bg-gray-700 p-2 rounded"
                    value={selectedSystem}
                    onChange={(e) => {
                        const index = e.target.value; // Get selected index
                        setSelectedSystem(index); // Set the selected index
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
};

export default ExoplanetSimulation;
