# 📌 ML Project: Full Breakdown (146 Cells)

## 🔹 Step 1: Import Libraries
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
```
✅ Pandas, Numpy → Data handling  
✅ Matplotlib, Seaborn → Data visualization  
✅ Scikit-Learn → ML model training  

## 🔹 Step 2: Load Dataset
```python
df = pd.read_csv("data.csv")
df.head()
```
✅ Data import kiya CSV file se  
✅ `df.head()` → Pehle 5 rows dekhi  

## 🔹 Step 3: Data Cleaning & Processing

### 📌 Convert Height to Meters
```python
df['Height_m'] = df['Height'] / 100
```
✅ Height cm → meters me convert kiya  

### 📌 BMI Calculation
```python
df['BMI'] = df['Weight'] / (df['Height_m'] ** 2)
```
✅ BMI calculate kiya  
✅ BMI = Weight (kg) / (Height (m)²)  

### 📌 Smoking Prediction
```python
def assign_smoking(age):
    if age < 20:
        return 0  
    elif 20 <= age < 35:
        return np.random.choice([0, 1], p=[0.7, 0.3])  
    else:
        return np.random.choice([0, 1], p=[0.5, 0.5])  

df['Smoking'] = df['Age'].apply(assign_smoking)
```
✅ Smoking probability set ki age ke basis pe  

### 📌 Diabetes Prediction
```python
def assign_diabetes(age, bmi):
    if age > 45 and bmi > 30:
        return 1  
    elif age > 35 and bmi > 27:
        return np.random.choice([0, 1], p=[0.6, 0.4])  
    else:
        return 0  

df['Diabetes'] = df.apply(lambda row: assign_diabetes(row['Age'], row['BMI']), axis=1)
```
✅ Diabetes ka risk calculate kiya age + BMI se  

### 📌 Systolic & Diastolic Blood Pressure
```python
df['Systolic_BP'] = 90 + (df['Age'] * 0.5) + (df['BMI'] * 0.2) + np.random.randint(-10, 10, df.shape[0])
df['Diastolic_BP'] = 60 + (df['BMI'] * 0.1) + np.random.randint(-5, 5, df.shape[0])
```
✅ BP ka estimation kiya age aur BMI ke basis pe  

## 🔹 Step 4: Drop Unnecessary Columns
```python
df.drop(['User_ID', 'Duration'], axis=1, inplace=True)
```
✅ User_ID aur Duration remove kiya (model ke liye useless tha)  

## 🔹 Step 5: Save Updated Dataset
```python
df.to_csv("Updated_Dataset.csv", index=False)
```
✅ Naya cleaned dataset save kiya  

## 🔹 Step 6: Data Visualization

### 📌 1. BMI Distribution
```python
sns.histplot(df['BMI'], bins=30, kde=True)
plt.show()
```
✅ BMI distribution dekha histogram se  

### 📌 2. Diabetes Countplot
```python
sns.countplot(x='Diabetes', data=df)
plt.show()
```
✅ Kitne log diabetes-positive aur negative hain, wo dikhaya  

### 📌 3. BP vs Age Line Plot
```python
plt.plot(df['Age'], df['Systolic_BP'], label='Systolic BP', color='red')
plt.plot(df['Age'], df['Diastolic_BP'], label='Diastolic BP', color='blue')
plt.legend()
plt.show()
```
✅ BP aur Age ka relation dekha  

## 🔹 Step 7: Train ML Model (Calories Prediction)
```python
X = df.drop(['Calories'], axis=1)
y = df['Calories']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
```
✅ Calories prediction ke liye RandomForest model train kiya  
✅ Train-Test split 80-20 ratio me kiya  

## 🔹 Step 8: Model Evaluation
```python
y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print(f"Updated R² Score: {r2}")
print(f"Updated Mean Squared Error: {mse}")
```
✅ Model ki accuracy check ki (R² Score, MSE)  

## 🎯 Final Summary  
✔️ Data Cleaning & Feature Engineering (BMI, Smoking, BP, Diabetes)  
✔️ Data Visualization (Histograms, Countplots, Line plots)  
✔️ ML Model Training (Calories Prediction using new features)  
✔️ Model Evaluation (R² Score, MSE)  
✔️ Updated Dataset Save Kiya (`Updated_Dataset.csv`)  
