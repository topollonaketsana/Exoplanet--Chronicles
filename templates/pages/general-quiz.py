import streamlit as st
import streamlit.components.v1 as components


# Set up the page configuration
st.set_page_config(page_title="Exoplanet Explorer", layout="wide")
#Set up page background
page_bg_img= """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://static.vecteezy.com/system/resources/previews/011/301/802/non_2x/blur-background-plain-with-space-free-photo.jpg");
background-size:cover;
}

[data-testid="stHeader"] {
background-color: rgba(0,0,0,0);
}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)

# HTML and CSS custom styling
st.markdown("""
    <style>
    .styled-title {
        padding: 10px 10px;
        background: linear-gradient(to right, blue, pink);
        -webkit-background-clip: text;
        color: transparent;
        font-size: 65px;
        text-align: center;
        font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
        font-style: oblique;
        font-weight: bolder;
    }
    .styled-content {
        position:relative;
        color: black;
        line-height:20px;
        font-size: 18px;
        font-style:oblique;
        font-family:'Times New Roman', Times, serif;
    }
    .quiz-subheader {
        color: Blue;  /* Color for quiz subheader */
        font-size:20px;
    }
    .quiz-subheader2 {
        color: White;  /* Color for quiz subheader */
        font-size:20px;
        font-weight: bold;
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
    .custom-label {
        color: white;
        font-weight: bold;
    }
    div[data-testid="stTextInput"] label {
        color: blue;
    }
    </style>
    <h1 class="styled-title">Welcome to Exoplanets (General) Quiz!!!</h1>
    <div class="styled-content">
        Are you ready to embark on an out-of-this-world adventure? Dive into the fascinating universe of exoplanets—those mysterious worlds orbiting stars far beyond our own! From gas giants to rocky havens, each question will take you deeper into the cosmos, sparking your curiosity and expanding your knowledge. Join us on this cosmic journey where learning meets fun! Challenge yourself, explore the wonders of the universe, and discover what makes each exoplanet unique. Don’t worry; it’s not just about getting the answers right—it's all about having a great time while learning something new! So buckle up, and let’s see how many cosmic secrets you can uncover!
    </div>  
     
    """, unsafe_allow_html=True)
st.markdown("<h3 style='color:blue;' id='exoplanets -Knowledge-quiz'>Exoplanets Knowledge Quiz</h3>",unsafe_allow_html=True)
st.markdown("<p class='quiz-subheader'>Test your knowledge of exoplanets!</p>", unsafe_allow_html=True)
st.markdown("<p class='quiz-subheader2'>Note: This quiz comprises of 12 questions. After clicking the next question button, click it once more to move on to the next question. You cannot return to the previous question but at the end of the last question, you'll be able to restart the quiz. You can restart as many times as you like.</p>", unsafe_allow_html=True)

# Get user's name
name = st.text_input("Enter your name")
if name:
    st.markdown(f"<p style='color:blue;font-size:20px; font-family:'Times New Roman', Times, serif;font-style:oblique;'>Welcome, {name}! Let's begin the quiz.</p>", unsafe_allow_html=True)

# Define the questions, options, and correct answers
questions = [
    {"question": "What are exoplanets?", 
     "options": ["Planets that orbit only red dwarf stars.", "Planets outside our galaxy", "Planets that orbit stars outside our solar system", "Planets that orbit within our solar system"],
     "correct": 2,
     "explanation": "Exoplanets are planets that orbit stars other than our Sun, expanding our knowledge beyond the solar system."},
    
    {"question": "What is the most common method for detecting exoplanets?", 
     "options": ["Radial velocity method", "Direct imaging", "Transit method", "Gravitational microlensing"],
     "correct": 2,
     "explanation": "The transit method is the most common detection technique, observing the dimming of a star's light as an exoplanet passes in front of it."},
    
    {"question": "Which exoplanet type orbits very close to its host star?", 
     "options": ["Super-Earths", " Hot Jupiters", "Water Worlds", "Puffy Planets"],
     "correct": 1,
     "explanation": "Hot Jupiters are gas giants that orbit extremely close to their host stars, experiencing high temperatures."},
    
    {"question": "Which method detects exoplanets by measuring a star’s *wobble*?", 
     "options": ["Transit method", "Radial velocity method", "Direct imaging", "Gravitational microlensing"],
     "correct": 1,
     "explanation": "The radial velocity method measures a star’s wobble caused by the gravitational pull of an orbiting exoplanet."},
    
    {"question": "What is the “Goldilocks Zone”?", 
     "options": ["The region of space where all planets are the same size", "The area where stars form planets", "The distance from a star where liquid water can exist", "A zone where planets cannot support life"],
     "correct": 2,
     "explanation": "The habitable zone, or *Goldilocks Zone,* is where temperatures allow liquid water, increasing the chance for life."},
    
    {"question": "What is an example of a *Water World*?", 
     "options": ["51 Pegasi b", "Gliese 1214 b", "WASP-17 b", "Proxima Centauri b"],
     "correct": 1,
     "explanation": " Gliese 1214 b is a *Water World,* believed to have a thick atmosphere possibly rich in water vapor."},
    
    {"question": "Why is the presence of an atmosphere important for life on exoplanets?", 
     "options": ["It helps the planet stay cold", "It protects the planet from radiation and regulates temperatures", "It makes the planet larger", "It shortens the planet’s orbital period"],
     "correct": 1,
     "explanation": "A planet’s atmosphere can protect life from harmful radiation and help maintain stable surface conditions."},
    
    {"question": "Which space telescope is crucial for studying exoplanet atmospheres?", 
     "options": ["Hubble Space Telescope", "James Webb Space Telescope", "Spitzer Space Telescope", "Kepler Space Telescope"],
     "correct": 1,
     "explanation": "The James Webb Space Telescope (JWST) is designed to study exoplanet atmospheres, looking for signs of life."},
    
    {"question": "Which exoplanet has a retrograde orbit, meaning it moves opposite to its star's rotation?", 
     "options": ["WASP-17 b", "Kepler-22 b", " Proxima Centauri b", " Gliese 1214 b"],
     "correct": 0,
     "explanation": "WASP-17 b orbits in a retrograde direction, challenging our understanding of planetary formation."},
    
    {"question": "What is the ultimate goal of exoplanet research?", 
     "options": ["To discover the largest planet", "To find planets with active volcanoes", "To discover planets that could support life", "To find planets that orbit red dwarf stars"],
     "correct": 2,
     "explanation": "The ultimate goal of exoplanet research is to discover planets that might support life or show signs of biological activity."},
    
    {"question": "What is the primary advantage of direct imaging in exoplanet detection?", 
     "options": ["It shows the planet's magnetic field", " It provides an actual picture of the exoplanet", "It detects planets based on their size", "It identifies the planet's temperature"],
     "correct": 1,
     "explanation": "Direct imaging involves capturing a picture of the exoplanet by blocking out the light of its star."},
    
    {"question": "Which mission focuses on discovering and characterizing exoplanets?", 
     "options": ["Mars Perseverance Rover", "NASA’s TESS mission", "Voyager 1", "Apollo 11"],
     "correct": 1,
     "explanation": "NASA’s TESS mission (Transiting Exoplanet Survey Satellite) is specifically designed to discover and study exoplanets."},
    
]

# Initialize session state variables
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'answered' not in st.session_state:
    st.session_state.answered = False

# Display current question
if st.session_state.current_question < len(questions):
    current_question = questions[st.session_state.current_question]
    
    # Radio buttons for answer selection
    answer = st.radio("Question: " + current_question["question"], current_question["options"])
    
    # Submit button
    if st.button('Submit'):
        # Check if the answer is correct
        if answer == current_question["options"][current_question["correct"]]:
            st.success("Correct!")
            st.session_state.score += 1
        else:
            st.error("Incorrect.")
        
        # Show explanation
        st.write("Explanation:", current_question["explanation"])
        
        # Mark question as answered
        st.session_state.answered = True

    # Button to proceed to the next question
    if st.session_state.answered:
        if st.button("Next Question"):
            st.session_state.current_question += 1
            st.session_state.answered = False
            
else:
    st.write(f"Quiz completed! Your score is {st.session_state.score}/{len(questions)}.")
    
    # Restart quiz button
    if st.button("Restart Quiz"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.answered = False

# Sidebar for Additional Information or Navigation
st.sidebar.title("General Quiz Page")
st.sidebar.success('select pages above to learn more about exoplanets')
st.sidebar.write("Use the sidebar to check out more information about exoplanets")
st.sidebar.success('For more information on exoplanets and the latest discoveries, explore NASA dedicated exoplanet page:[NASA Exoplanet Exploration](https://exoplanets.nasa.gov/).')
