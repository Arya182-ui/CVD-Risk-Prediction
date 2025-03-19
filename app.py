from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

with open('cardio_risk_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        gender = 1  
        age = float(request.form['age'])
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        heart_rate = 72 
        body_temp = 36.5  
        calories = 2000 
        bmi = weight / ((height / 100) ** 2) 
        systolic_bp = float(request.form['systolic_bp'])
        diastolic_bp = float(request.form['diastolic_bp'])
        smoking = int(request.form['smoking'])
        diabetes = int(request.form['diabetes'])

        feature_names = ['Gender', 'Age', 'Height', 'Weight', 'Heart_Rate', 
                         'Body_Temp', 'Calories', 'BMI', 'Systolic_BP', 
                         'Diastolic_BP', 'Smoking', 'Diabetes']

        input_data = pd.DataFrame([[gender, age, height, weight, heart_rate, 
                                    body_temp, calories, bmi, systolic_bp, 
                                    diastolic_bp, smoking, diabetes]], columns=feature_names)

        # Prediction
        risk_score = model.predict_proba(input_data)[0][1]  # Probability of High Risk

        # Risk Categorization
        if risk_score < 0.3:
            risk_category = "Low Risk"
        elif risk_score < 0.6:
            risk_category = "Medium Risk"
        else:
            risk_category = "High Risk"

        return render_template('index.html', prediction_text=f"CVD Risk Level: {risk_category} ({round(risk_score * 100, 2)}%)")

    except Exception as e:
        return render_template('index.html', prediction_text="Error: " + str(e))

if __name__ == '__main__':
    app.run(debug=True)
