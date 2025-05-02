from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib


app = Flask(__name__)


with open('predction_model.pkl', 'rb') as file:
    model = joblib.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        general_health = int(request.form['general_health'])
        checkup = int(request.form['checkup'])
        exercise = int(request.form['exercise'])
        skin_cancer = int(request.form['skin_cancer'])
        other_cancer = int(request.form['other_cancer'])
        depression = int(request.form['depression'])
        diabetes = int(request.form['diabetes'])
        arthritis = int(request.form['arthritis'])
        sex = int(request.form['sex'])
        age_category = int(request.form['age_category'])
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        bmi = float(request.form['bmi'])
        smoking_history = int(request.form['smoking_history'])
        alcohol_consumption = int(request.form['alcohol_consumption'])
        fruit_consumption = int(request.form['fruit_consumption'])
        green_vegetables_consumption = int(request.form['green_vegetables_consumption'])
        fried_potato_consumption = int(request.form['fried_potato_consumption'])

        input_data = pd.DataFrame([[
            general_health, checkup, exercise, skin_cancer, other_cancer, depression,
            diabetes, arthritis, sex, age_category, height, weight, bmi,
            smoking_history, alcohol_consumption, fruit_consumption,
            green_vegetables_consumption, fried_potato_consumption
        ]], columns=[
            'General_Health', 'Checkup', 'Exercise', 'Skin_Cancer', 'Other_Cancer',
            'Depression', 'Diabetes', 'Arthritis', 'Sex', 'Age_Category', 'Height_(cm)',
            'Weight_(kg)', 'BMI', 'Smoking_History', 'Alcohol_Consumption',
            'Fruit_Consumption', 'Green_Vegetables_Consumption',
            'FriedPotato_Consumption'
        ])

        risk_score = model.predict_proba(input_data)[0][1]

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
