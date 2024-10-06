import streamlit as st
import streamlit.components.v1 as components

# Set up the page configuration
st.set_page_config(page_title="Exoplanet Explorer", layout="wide")
#Inserting a backgrond image on the page
page_bg_img= """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://c4.wallpaperflare.com/wallpaper/137/686/415/exoplanet-4k-interesting-hd-wallpaper-preview.jpg");
background-size:cover;
}

[data-testid="stHeader"] {
background-color: rgba(0,0,0,0);
}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)

# Title and Subheading Section
st.markdown("""
    <style>
    .styled-title {
        padding: 10px 10px;
        background: linear-gradient(to right, white, blue);
        -webkit-background-clip: text;
        color: transparent;
        font-size: 65px;
        text-align: center;
        font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
        font-style: oblique;
        font-weight: bolder;
    }
    .styled-subheader {
        font-size: 25px;
        background: linear-gradient(to right, white,blue);
        -webkit-background-clip: text;
        font-weight: bolder;
        font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
        color: transparent;
    }
    .styled-content {
        position:relative;
        color: white;
        line-height:20px;
        font-size: 18px;
        font-style:oblique;
        font-family:'Times New Roman', Times, serif
    }
    .quiz-subheader {
        color: #FFFFFF;  /* Color for quiz subheader */
        font-size:20px;
    }
    .image-info {
        color: #FFFFFF;  /* Color for image information */
        font-size:15px;
    }
    .styled-caption {
        background: linear-gradient(to right, white, purple);
        -webkit-background-clip: text;
        font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
        color: transparent;
        font-weight: bold;
        font-size: 20px;  /* Adjust font size as needed */
        text-align: center;
    }
    .styled-info {
        color: white;
        font-weight: bold;
    }
    .custom-label {
        color: white;
        font-weight: bold;
    }
    div[data-testid="stTextInput"] label {
        color: white;
    }
    </style>
    <h1 class="styled-title">Exoplanets</h1>
    <h2 class="styled-subheader">In Case You're Wondering What are Exoplanets???</h2>
    <div class="styled-content">
        Exoplanets, or planets that orbit stars beyond our solar system, are some of the most exciting discoveries in modern astronomy. They're called "exoplanets" because the prefix "exo-" means "outside" or "beyond," signifying that these planets exist outside our solar system. Unlike the planets orbiting our Sun, exoplanets are found in distant star systems, often with environments vastly different from what we know. Some are enormous gas giants, while others are rocky, Earth-like worlds. What makes them truly fascinating is the possibility that some may have conditions suitable for life, with oceans, clouds, and even strange weather patterns. Each new exoplanet we discover expands our understanding of the universe, revealing just how diverse and mysterious other worlds can be!
    </div>  
     
    """, unsafe_allow_html=True)

# Exoplanet Image Section
st.markdown("<h3 style='color:white;' id='popular-exoplanets'>Popular Exoplanets</h3>",unsafe_allow_html=True)

# Creating 3 images per row
cols = st.columns(3)  

with cols[0]:
    st.image("images/What-Is-Proxima-Centauri-b.png")
    st.markdown("<div class='styled-caption'>Proxima Centauri b</div>", unsafe_allow_html=True)
    st.markdown("<div class='styled-info'>Proxima Centauri b is one of the most promising candidates for potentially harboring life. It is located just over 4 light-years away, making it the closest known exoplanet to Earth. Proxima b orbits in the habitable zone of its host star, Proxima Centauri, a red dwarf, at a distance that might allow for liquid water to exist on its surface. With a mass similar to that of Earth, Proxima Centauri b’s discovery generated excitement due to the proximity of its star, which makes detailed studies of the planet more feasible. However, Proxima Centauri is an active star with frequent solar flares that could pose challenges for habitability, as high-energy radiation might strip the planet’s atmosphere or hinder the development of life. Despite these challenges, Proxima b remains an important target for future exploration.</div>", unsafe_allow_html=True)
    
with cols[1]:
    st.image('images/1200px-Osiris_(HD209458b)_planet_illustration.jpeg')
    st.markdown("<div class='styled-caption'>HD 209458 b</div>", unsafe_allow_html=True)
    st.markdown("<div class='styled-info'>HD 209458 b, often referred to as Osiris, is a well-known exoplanet that was one of the first to be discovered transiting its host star. Located approximately 159 light-years away in the constellation Pegasus, it was the first exoplanet where astronomers detected an atmosphere, specifically containing water vapor, hydrogen, carbon monoxide, and other elements. HD 209458 b is a gas giant with a mass about 0.69 times that of Jupiter, and it orbits extremely close to its host star, completing a full orbit in just about 3.5 days. Due to this proximity, the planet experiences extreme temperatures, and material from its atmosphere is being stripped away by the intense stellar radiation, leading to a comet-like tail of gas escaping into space. This *blow-off* effect is a major factor in understanding atmospheric loss in exoplanets.</div>", unsafe_allow_html=True)

with cols[2]:
    st.image('images/WASP-17b.jpg')
    st.markdown("<div class='styled-caption'>WASP-17 b</div>", unsafe_allow_html=True)
    st.markdown("<div class='styled-info'>WASP-17 b is notable for being one of the largest and least dense exoplanets discovered, categorized as a *puffy planet.* It orbits its host star in the constellation Scorpius, around 1,000 light-years away from Earth. What makes WASP-17 b unique is that it orbits its star in a retrograde direction, opposite to the star's rotation. This retrograde orbit challenges our understanding of planet formation and dynamics, as it implies a significant gravitational interaction with another celestial body or some other disruption during its history. WASP-17 b is also remarkable for its low density, which is only about 0.1 grams per cubic centimeter—less dense than water—likely due to its proximity to its star and the corresponding intense heating, which expands its gaseous envelope.</div>", unsafe_allow_html=True)

# Create another row for more images
cols = st.columns(3)

with cols[0]:
    st.image('images/images.jpg')
    st.markdown("<div class='styled-caption'>Kepler-22 b</div>", unsafe_allow_html=True)
    st.markdown("<div class='styled-info'>Kepler-22 b is one of the earliest exoplanets found in the habitable zone of its host star, which means it orbits at a distance where conditions could potentially support liquid water. It is located about 600 light-years away in the constellation Cygnus. Kepler-22 b has a radius about 2.4 times that of Earth, classifying it as a *super-Earth.* While its exact composition remains uncertain, Kepler-22 b’s discovery fueled excitement about the possibility of finding habitable environments outside our solar system. Its star, slightly smaller and cooler than our Sun, provides a stable environment that could, in theory, support the presence of water on the planet’s surface, although its actual habitability is still a matter of speculation.</div>", unsafe_allow_html=True)
    
with cols[1]:
    st.image('images/image_11907e-Gliese-1214b.jpg')
    st.markdown("<div class='styled-caption'>Gliese 1214 b</div>", unsafe_allow_html=True)
    st.markdown("<div class='styled-info'>Gliese 1214 b, also known as GJ 1214 b, is a well-studied super-Earth located approximately 48 light-years away in the constellation Ophiuchus. With a mass about 6.6 times that of Earth, it is considered an intermediate between rocky planets and gas giants. Gliese 1214 b is of great interest because it is thought to have a thick atmosphere, possibly rich in water vapor, which gives it the nickname *water world*. Observations suggest that the planet could be enveloped by a massive water layer or a dense steam atmosphere, which makes it a key target in studying exoplanetary atmospheres. However, the planet's proximity to its host star means temperatures are quite high, which might affect its potential habitability.</div>", unsafe_allow_html=True)

with cols[2]:
    st.image('images/images (1).jpg')
    st.markdown("<div class='styled-caption'>51 Pegasi b</div>", unsafe_allow_html=True)
    st.markdown("<div class='styled-info'>51 Pegasi b, also known as Dimidium, holds historical importance as the first exoplanet discovered orbiting a Sun-like star, back in 1995. It is located around 50 light-years away in the constellation Pegasus. 51 Pegasi b is classified as a *hot Jupiter* due to its size and close proximity to its host star, which results in high temperatures and rapid orbital movement—it completes an orbit in about 4 days. This discovery marked a significant milestone in exoplanet research, confirming that other stars have planets, and it earned Michel Mayor and Didier Queloz the 2019 Nobel Prize in Physics. The planet’s atmosphere likely contains significant amounts of hydrogen and helium, and its extreme environment paved the way for the study of other similar exoplanets.</div>", unsafe_allow_html=True)


# Sidebar for Additional Information or Navigation
st.sidebar.title("main page")
st.sidebar.success('select pages above to learn more about exoplanets')
st.sidebar.write("Use the sidebar to check out more information about exoplanets")
st.sidebar.success('For more information on exoplanets and the latest discoveries, explore NASA dedicated exoplanet page:[NASA Exoplanet Exploration](https://exoplanets.nasa.gov/).')

# HTML/CSS for custom styling 
st.markdown("""
    <style>
    .stTextInput input {
        padding: 10px;
        border-radius: 5px;
        border: 2px solid #ccc;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white
        border-radius: 5px;
        padding: 10px;
        font-size: 26px;
    }
    .stRadio>div {
        padding-left: 20px;
    }
    .stRadio label{
        color:white;
    }
    </style>
""", unsafe_allow_html=True)
