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

# Title and Definition Section
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
        color: black;
        font-weight: bold;
    }
    .custom-label {
        color: white;
        font-weight: bold;
    }
    div[data-testid="stTextInput"] label {
        color: blue;
    }
    </style>
    <h1 class="styled-title">Welcome to Popular Exoplanets Quiz!!!</h1>
    <div class="styled-content">
        Get ready to journey beyond our solar system and dive into the fascinating world of exoplanets—those mysterious planets that orbit stars far, far away! These cosmic wonders are popular for a reason: some are rocky and could be home to alien oceans, while others are scorching gas giants with wild, swirling atmospheres. From planets orbiting the closest stars to Earth, to those in the "habitable zone" where life might exist, these exoplanets are full of surprises. So, put on your space helmets, and let's see how well you know the most exciting worlds beyond our own!
    </div>  
     
    """, unsafe_allow_html=True)
st.markdown("<h3 style='color:blue;' id='exoplanets -Knowledge-quiz'>Popular Exoplanets Knowledge Quiz</h3>",unsafe_allow_html=True)
st.markdown("<p class='quiz-subheader'>Test your knowledge on popular exoplanets!</p>", unsafe_allow_html=True)
st.markdown("<p class='quiz-subheader2'>Note: This quiz comprises of 12 questions. After clicking the next question button, click it once more to move on to the next question. You cannot return to the previous question but at the end of the last question, you'll be able to restart the quiz. You can restart as many times as you like.</p>", unsafe_allow_html=True)
# Get user's name
name = st.text_input("Enter your name")
if name:
    st.markdown(f"<p style='color:blue;font-size:20px; font-family:'Times New Roman', Times, serif;font-style:oblique;'>Welcome, {name}! Let's begin the quiz.</p>", unsafe_allow_html=True)
    #st.write(f"Welcome, {name}! Let's begin the quiz. Note: After clicking the next question button, click it once more to move to the next question")

# Define the questions, options, and correct answers
questions = [
    {"question": "What makes HD 209458 b (Osiris) unique among exoplanets?", 
     "options": ["It is the first exoplanet discovered in the habitable zone.", "It has a comet-like tail of gas.", " It has an ice-covered surface.", "It is a rocky planet similar to Earth."],
     "correct": 1,
     "explanation": "HD 209458 b (Osiris) was the first exoplanet where astronomers observed material being blown off its atmosphere due to extreme stellar radiation, forming a comet-like tail of gas. This phenomenon helps scientists understand atmospheric loss in exoplanets."},
    
    {"question": "What was the first element detected in HD 209458 b’s atmosphere?", 
     "options": [" Oxygen", "Nitrogen", "Water vapor", "Methane"],
     "correct": 2,
     "explanation": "HD 209458 b is notable for being the first exoplanet with a detected atmosphere, specifically containing water vapor along with other gases. This discovery paved the way for studying exoplanet atmospheres in detail."},

    {"question": "How close is Proxima Centauri b to Earth?", 
     "options": ["159 light-years", " 4 light-years", "1,000 light-years", "48 light-years"],
     "correct": 1,
     "explanation": "Proxima Centauri b is located just over 4 light-years from Earth, making it the closest known exoplanet. Its proximity is why it has been a key target for studying potentially habitable exoplanets."},

    {"question": "Why is Proxima Centauri b considered a promising candidate for habitability?", 
     "options": ["It orbits in the habitable zone of its star.", "It has a dense atmosphere of methane.", "It has large ice caps and oceans.", "It is a gas giant with many moons."],
     "correct": 0,
     "explanation": "Proxima Centauri b orbits within the habitable zone of its star, Proxima Centauri, where conditions might allow for liquid water to exist on its surface—one of the primary factors for potential habitability."},

    {"question": "What is the biggest challenge for life on Proxima Centauri b?", 
     "options": ["Extreme cold temperatures", "Frequent solar flares from its host star", "Lack of atmosphere", "Excessive distance from its star"],
     "correct": 1,
     "explanation": "Proxima Centauri, the star Proxima b orbits, is known for frequent solar flares. These flares can emit harmful radiation that may strip away the planet's atmosphere, making it difficult for life to thrive."},

    {"question": "Which exoplanet is known for its retrograde orbit?", 
     "options": ["Proxima Centauri b", "HD 209458 b", "WASP-17 b", "Kepler-22 b"],
     "correct": 2,
     "explanation": "WASP-17 b is unique because it orbits in the opposite direction of its star’s rotation. This unusual retrograde orbit suggests that the planet may have experienced significant gravitational interactions or disruptions during its formation."},

    {"question": "What category does WASP-17 b fall under due to its large size and low density??", 
     "options": ["Super-Earth", "Water world", "Hot Jupiter", "Puffy planet"],
     "correct": 3,
     "explanation": "WASP-17 b is considered a “puffy planet” because of its very low density. Its gaseous envelope is expanded due to intense heat from its nearby star, making it less dense than water and giving it a puffed-up appearance."},

    {"question": "Kepler-22 b is most exciting because it was one of the first exoplanets found where?", 
     "options": ["In a retrograde orbit", "In the habitable zone", "With a rocky surface", "In a binary star system"],
     "correct": 1,
     "explanation": "Kepler-22 b is located in the habitable zone of its star, meaning it is at a distance where conditions could allow liquid water to exist, making it a strong candidate for potential habitability."},

    {"question": "What is the main feature of Gliese 1214 b that makes it intriguing for study?", 
     "options": ["It has a rocky surface.", "It has an atmosphere possibly rich in water vapor.", "It has frequent volcanic activity.", "It orbits two stars at once."],
     "correct": 1,
     "explanation": "Gliese 1214 b is thought to have a thick atmosphere rich in water vapor, earning it the nickname “water world.” This makes it a key target for studying the atmospheres of super-Earths and the potential for water-based environments."},

    {"question": "How far away is Gliese 1214 b from Earth?", 
     "options": ["50 light-years", "48 light-years", " 4 light-years", "159 light-years"],
     "correct": 1,
     "explanation": "Gliese 1214 b is located approximately 48 light-years away from Earth, relatively close on a cosmic scale. This proximity allows astronomers to study the planet in greater detail."},      

    {"question": "What is 51 Pegasi b’s claim to fame?", 
     "options": [" It was the first exoplanet discovered orbiting a Sun-like star.", "It is the closest exoplanet to Earth.", "It is the first exoplanet with moons.", "It is the first exoplanet where life was discovered."], 
     "correct": 0,
     "explanation": "51 Pegasi b, discovered in 1995, was the first exoplanet found orbiting a star similar to our Sun. Its discovery revolutionized our understanding of planetary systems and proved that other stars have planets."},

    {"question": "What classification does 51 Pegasi b fall under?", 
     "options": ["Water world", "Gas giant", "Super-Earth", "Hot Jupiter"],
     "correct": 3,
     "explanation": "51 Pegasi b is classified as a “hot Jupiter” due to its large size (comparable to Jupiter) and close orbit around its star, resulting in extremely high surface temperatures."}
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
st.sidebar.title("Popular Exoplanets Quiz Page")
st.sidebar.success('select pages above to learn more about exoplanets')
st.sidebar.write("Use the sidebar to check out more information about exoplanets")
st.sidebar.success('For more information on exoplanets and the latest discoveries, explore NASA dedicated exoplanet page:[NASA Exoplanet Exploration](https://exoplanets.nasa.gov/).')
