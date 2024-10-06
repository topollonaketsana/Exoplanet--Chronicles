import streamlit as st


# Set up the page configuration
st.set_page_config(page_title="Exoplanet Explorer", layout="wide")

#Titles and sub-headings sections
st.title("The Fascinating World of Exoplanets")

#HTML and CSS custom styling
st.markdown("""
    <style>
    .styled-subheader {
        font-size: 20px;
        font-weight: bolder;
        font-family:'Times New Roman'Times,serif;
        color: black;
    }
    .styled-content {
        position:relative;
        color: black;
        line-height:20px;
        font-size: 18px;
        font-style:oblique;
        font-family:'Times New Roman', Times, serif;
    }
    </style>
    <div class="styled-content">
        On this page, you’ll discover how astronomers detect planets beyond our solar system, learn about the types of exoplanets we’ve uncovered, and dive into the fascinating concept of habitability. Through engaging visuals, we explore key methods used to find exoplanets, like the transit and radial velocity techniques, as well as examples of exotic worlds like Hot Jupiters and Super-Earths. With stunning images and videos, you'll gain insights into how atmospheres play a crucial role in supporting life, why exoplanet research is so important, and what the future holds with advanced missions like NASA’s TESS and the James Webb Space Telescope. Enjoy exploring and expanding your understanding of the universe!
    </div>  
    <br>
""", unsafe_allow_html=True)

st.markdown("<p class='styled-subheader'>The images below provide information about detection methods,habitability and types of exoplanets</p>", unsafe_allow_html=True)
# creating 3 images per row
cols = st.columns(3)

#Setting up first image and its information
with cols[0]:
    st.subheader("Detection methods of exoplanets")
    st.image("https://science.nasa.gov/wp-content/uploads/2023/09/TRAPPIST_transit.gif?w=1280&format=webp",
             caption="Artist's concept of detection methods of exoplanets. Source: NASA")
    st.markdown("""
    ### What You’re Seeing:
This image shows the **transit method** of detecting exoplanets. In simple terms: A planet passes in front of its star, causing the star to dim a little. Scientists can measure this dimming to determine if a planet is there, even though they can't see it directly. This method helps us find planets around distant stars.
The planet is like a small shadow passing in front of a big light. When it moves across the star, we see a tiny dip in the star’s brightness, which tells us a planet might be there!
### Other Detection Methods:
1. **Radial Velocity (Doppler) Method**: Planets cause their stars to wobble a little due to their gravity. By measuring this wobble, scientists can detect the presence of a planet.  
2. **Direct Imaging**: Sometimes, astronomers block out a star's light to take pictures of the planets around it.
3. **Gravitational Microlensing**: This method observes how a planet’s gravity bends the light from a distant star, helping scientists spot planets.
### Key Points:
- **Dips in Starlight**: We look for tiny dips in brightness to find planets.
- **Star Wobble**: We measure the star's movement to see if a planet is nearby.
These methods allow us to discover exoplanets without seeing them directly!
""")  
#Setting up second image and its informations
with cols[1]:
    st.subheader("Habitability of exoplanets")
    st.image('https://science.nasa.gov/wp-content/uploads/2023/09/illustration_of_planets_inside_and_outside_the_Habitable_Zone.jpeg?w=1280&format=webp',
             caption="Artist's concept of habitability of exoplanets. Source: NASA")
    st.markdown("""
    ### What You’re Seeing:
This image shows a star surrounded by different planets, each one at varying distances from the star. These distances are important for understanding where life might exist.
### Habitable Zone (Goldilocks Zone)
In this picture, notice the area around the star where it’s neither too hot nor too cold. This region is called the **Habitable Zone**, often referred to as the **Goldilocks Zone**. It’s just right for liquid water to exist, which is essential for life as we know it. For example, **Proxima Centauri b** is a planet that sits in this habitable zone. It’s a great candidate for supporting life because it could have the right conditions for water to be liquid.
### Atmospheric Composition
Now, look at the planets in this image. Scientists also study the **atmospheric composition** of these planets to see if they could be habitable. If a planet has gases like **oxygen**, **water vapor**, or **methane**, it might be a sign that the planet could support life or has had biological activity in the past. These gases are important because they are often produced by living organisms. So, when scientists find them, it raises exciting possibilities about what might be happening on that planet!
Together, the location of a planet in the habitable zone and the gases in its atmosphere give scientists clues about the potential for life beyond Earth. Understanding these factors is key in the search for extraterrestrial life.
""")
#Setting up third image and its information
with cols[2]:
    st.subheader("Types of exoplanets")
    st.image('https://science.nasa.gov/wp-content/uploads/2023/09/Exoplanets-REV-2-labels_highres.jpg',
             caption="Artist's concept of types of exoplanets. Source: NASA")
    st.markdown("""
    Exoplanets come in many different types, with unique characteristics that set them apart from planets in our solar system. 
Scientists have discovered a variety of exoplanets, each with its own fascinating traits. Here are some of the most interesting types:
### Hot Jupiters
Imagine a planet like Jupiter, but much closer to its star. These planets are huge gas giants that orbit very close to their stars, which makes them incredibly hot. Because of their closeness, the temperatures on these planets are extremely high. An example is **51 Pegasi b**, a giant planet that’s much too hot for life as we know it.
### Super-Earths
These planets are bigger than Earth, but smaller than Neptune. They might be rocky like our Earth, but with stronger gravity. Some could have water or even a thick atmosphere, making them interesting for scientists. An example is **Kepler-22 b**, which is larger than Earth and orbits in its star's habitable zone, where liquid water might exist.
### Puffy Planets
These are large planets with very low density. Even though they are big, they are “puffed up” with thick atmospheres that make them look like giant balloons in space. One example is **WASP-17 b**, which is one of the least dense planets ever discovered.
### Water Worlds
These planets could have vast amounts of water, either on the surface or trapped in a thick, steamy atmosphere. They might look like giant oceans in space! An example is **Gliese 1214 b**, a planet that may be covered with water or have a thick steam layer surrounding it.
""")

#Explanation of the images below
st.markdown("<p class='styled-subheader'>The images below provide information about the atmospheres and life of exoplanets,Importance of exoplanets research and futre Explorations of exoplanets</p>", unsafe_allow_html=True)

# Creating another 3 images per row
cols = st.columns(3)

#Setting up 1st image and its information
with cols[0]:
    st.subheader("Atmospheres and life of exoplanets")
    st.image("https://science.nasa.gov/wp-content/uploads/2023/04/heic1916a-jpg.webp?w=1280&format=webp",
             caption="Artist's concept of atmosphere's and life of exoplanets. Source: NASA")
    st.markdown("""
    ### What You're Seeing:
Look at this image of a distant planet. What you’re seeing is a world that might have an atmosphere, just like Earth. But why is an atmosphere so important for life?
### Importance of Atmospheres
In this picture, imagine the planet’s atmosphere as a protective blanket. It does several important things:  
- It **regulates surface temperatures** by trapping heat, making sure the planet doesn’t get too hot or too cold, similar to how Earth's atmosphere keeps us warm.  
- It **protects the planet from harmful radiation** coming from its star, just like Earth's atmosphere shields us from the sun's ultraviolet rays.  
- Most importantly for scientists, an atmosphere could **support life**. If we find water vapor, oxygen, or other gases that living things produce (called **biosignatures**), it’s a sign that the planet could have—or could have had—life. This makes studying atmospheres really exciting for astrobiologists, who are looking for clues of life beyond Earth.
### Challenges to Habitability
But not every planet with an atmosphere is a good place for life. In this picture, you might notice some harsh conditions. Some planets are bombarded by **solar flares**, which are intense bursts of radiation from their star. These flares can strip away the atmosphere or make the surface too dangerous for life.  
Other planets might lose their atmosphere completely, in a process called **atmospheric loss**, leaving them unprotected from the harsh environment of space.  
Additionally, some planets have **extreme temperatures**, either too hot or too cold, making it hard for any form of life to survive. These are the challenges scientists think about when they search for habitable planets.
""")
#Setting up second image and its information
with cols[1]:
    st.subheader("Importance of exoplanets research")
    st.image('https://images-assets.nasa.gov/image/PIA15258/PIA15258~large.jpg?w=1920&h=853&fit=clip&crop=faces%2Cfocalpoint',
             caption="Artist's concept of importantance of exoplanet research. Source: NASA")
    st.markdown("""
    ### What You’re Seeing:
Take a look at this image. What you see is a glimpse into the vast universe of exoplanets—planets that exist outside our solar system. This picture highlights why studying exoplanets is so important:
### Understanding Planetary Diversity
As you observe the different planets in this image, notice how varied they are. Some are massive gas giants, while others are smaller, rocky worlds. The image showcases how scientists have discovered thousands of exoplanets, each one unique. These discoveries have shown us that planetary systems can be incredibly diverse, and some planets are so different that they challenge what we thought we knew about how planets form and behave.
### Search for Life
Now, focus on the planets that are in the "habitable zone," which means they are just the right distance from their star for liquid water to exist. These are the planets that excite scientists the most because they could potentially support life. The ultimate goal of exoplanet research is to find planets like these that could either host life or give us clues about life beyond Earth.
### Technological Advances
Finally, notice the clarity and detail in this image. This level of detail is possible because of the incredible advancements in technology. Powerful telescopes and advanced data analysis techniques allow scientists to discover and study smaller, Earth-like planets more closely than ever before. These breakthroughs are helping us learn more about distant planets and pushing us closer to answering big questions, like whether life exists elsewhere in the universe.
""")
#Setting up 3rd image and its information
with cols[2]:
    st.subheader("Future Exploration of exoplanets")
    st.image('https://blogs.nasa.gov/webb/wp-content/uploads/sites/326/2022/08/STSCI-J-p2022-HIP65426b-f-1528x1130-1-1024x757.png',
             caption="Artist's concept of future exploration of exoplanets. Source: NASA")
    st.markdown("""
    ### What You’re Seeing:
This image shows the exciting future of exoplanet exploration. In the picture, you can see telescopes in space that are working to discover new worlds and understand their atmospheres.
### James Webb Space Telescope (JWST)
The large telescope in this image is the **James Webb Space Telescope (JWST)**, one of the most powerful tools we have for studying distant planets. JWST is helping us learn more about exoplanets by looking closely at their **atmospheres**—the gases surrounding them. By studying the light from these planets, JWST can detect important chemicals like water vapor and even search for **signs of life**. This is an important step in understanding which planets might be habitable.
### Space Missions
In the background, you can see other space missions dedicated to discovering and studying exoplanets. One of them is **NASA’s TESS (Transiting Exoplanet Survey Satellite)**. TESS looks for small dips in a star's brightness, which happens when a planet crosses in front of the star. This helps scientists find **new exoplanets** that might be similar to Earth.
Another important mission is **CHEOPS**, run by the **European Space Agency**. CHEOPS focuses on understanding the **size and composition** of already-known exoplanets. By learning more about these planets, scientists can figure out what they’re made of, how they formed, and whether they could be habitable.
These missions, along with JWST, are helping us explore more about the universe and get closer to answering the big question: Are we alone in the universe?
""")
#Creating the videos section
st.markdown("<h3 style='color:black;'>Video Explanations</h3>",unsafe_allow_html=True)
st.markdown("<p class='styled-subheader'>These video contain information about detection methods,habitability and types of exoplanets!</p>", unsafe_allow_html=True)
 # 3 videos per row
cols = st.columns(3) 
with cols[0]:
    st.subheader("Detection methods of exoplanets")
    st.markdown("""
**Citation:** NASA, *Distant Exoplanet Transiting Its Star* [Video]. Retrieved from [YouTube](https://youtu.be/BFi4HBUdWkk?si=A-Qe7aobsbI6-3F5).
""")    
with cols[1]:
    st.subheader("Habitability of exoplanets")
    st.markdown("""
**Citation:** NASA, *What Is the Habitable Zone* [Video]. Retrieved from [YouTube](https://youtu.be/J04YN9azln8?si=Gr4VGz2R2mrdttZq).
""")
with cols[2]:
    st.subheader("Types of exoplanets")
    st.markdown("""
    **Citation:** National Geographic, *Exoplanets 101* [Video]. Retrieved from [YouTube](https://youtu.be/EUU0-ZpFoK4?si=dmH5TGnlBX6MUOfO).
""")
    
st.markdown("<p class='styled-subheader'>Below are videos explaining atmospheres and life of exoplanets, importance of explanets research as well as future exploration of exoplanets</p>", unsafe_allow_html=True)
# 3 videos per row
cols = st.columns(3)  
with cols[0]:
    st.subheader("Atmospheres and life of exoplanets")
    st.markdown("""
**Citation:** NASA, *Exoplanets Weird, Wondorous Worlds* [Video]. Retrieved from [YouTube](https://youtu.be/4IXYp9Fse44?si=8THb_beh9QSGxl3A).
""") 
with cols[1]:
    st.subheader("Importance of exoplanets research")
    st.markdown("""
**Citation:** NASA, *Importance of exoplanet research* [Video]. Retrieved from [YouTube](https://youtu.be/wd-M417Z5g4?si=9dTkZDsdHtTWBq39).
""")
with cols[2]:
    st.subheader("Future Exploration of exoplanets")
    st.markdown("""
**Citation:** NASA, *Future Explorations of Exoplanets* [Video]. Retrieved from [YouTube](https://youtu.be/3ILVuU1gekc?si=aVCfPu1Z2h6zwFtZ).
""")

# Sidebar for Additional Information or Navigation
st.sidebar.title("Popular Exoplanets Quiz Page")
st.sidebar.success('select pages above to learn more about exoplanets')
st.sidebar.write("Use the sidebar to check out more information about exoplanets")
st.sidebar.success('For more information on exoplanets and the latest discoveries, explore NASA dedicated exoplanet page:[NASA Exoplanet Exploration](https://exoplanets.nasa.gov/).')

st.markdown("""
For more information on exoplanets and the latest discoveries, explore NASA's dedicated exoplanet page:
[NASA's Exoplanet Exploration](https://exoplanets.nasa.gov/).
""")
