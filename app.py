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
    # Get features from the form
    size = request.form.get('size')
    period = request.form.get('period')
    # Add other features

    # Create a DataFrame for the model prediction
    input_data = pd.DataFrame([[size, period]], columns= ['pl_rade', 'pl_orbper'])
    
    # Make prediction
    prediction = model.predict(input_data)

    return render_template('results.html', prediction= prediction)

if __name__ == '__main__':
    app.run(debug=True)
