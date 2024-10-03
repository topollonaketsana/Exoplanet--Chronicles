## App-like simulator
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib 


app = Flask(__name__)

# Load ML model 
model = joblib.load('C:/Users/topol/Exoplanet--Chronicles/model.pkl')

## exoplanet data
data = pd.read_csv('C:/Users/topol/Exoplanet--Chronicles/data/data_TOI.csv')

@app.route('/')
def index():
    return render_template('index.html', planets= data)

@app.route('/predict', methods= ['POST'])
def predict():
    size = request.form.get('size')
    period = request.form.get('period')


    # Create a DataFrame for the model prediction
    input_data = pd.DataFrame([[size, period]], columns= ['pl_rade', 'pl_orbper'])
    
    # Make prediction
    prediction = model.predict(input_data)
    