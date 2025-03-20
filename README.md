# 🏥 Cardiovascular Risk Prediction  

This is a **Flask-based web application** that predicts the risk of cardiovascular disease (CVD) using a **machine learning model**. The model takes user-inputted health parameters and provides a risk level (Low, Medium, or High).  

## 🚀 Features  
✅ User-friendly interface to input health parameters  
✅ Predicts **CVD risk level** based on a trained machine learning model  
✅ Provides probability-based risk categorization  
✅ Built using **Flask, Pandas, NumPy, and Pickle**  

## 📦 Tech Stack  
- **Python** (Flask, Pandas, NumPy)  
- **Machine Learning** (Pickle for model loading)  
- **HTML, CSS** (for UI templates)  

## 📂 Project Structure  

├── static/                  # CSS, JavaScript files (if any)  
├── templates/               # HTML templates  
│   ├── index.html           # Main UI  
├── cardio_risk_model.pkl    # Pre-trained ML model  
├── app.py                   # Flask application  
├── requirements.txt         # Dependencies  
├── ML_Project_Steps.md      # Steps for data cleaning and model training  
├── README.md                # Documentation  



## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Arya182-ui/CVD-Risk-Prediction.git
cd CVD-Risk-Prediction 
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv  
source venv/bin/activate  # On macOS/Linux  
venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt  
```


### 4️⃣ Run the Flask App
```bash
python app.py  
```

**The app will run on Your Loacal Host After a Sucessfull Run you can Open the link in a browser.**


## 📊 Input Features  

| Feature        | Description                    |  
|-------------- |--------------------------------|  
| **Age**       | Age in years                   |  
| **Height**    | Height in cm                   |  
| **Weight**    | Weight in kg                   |  
| **Systolic BP**  | Systolic blood pressure       |  
| **Diastolic BP** | Diastolic blood pressure      |  
| **Smoking**   | 0: No, 1: Yes                  |  
| **Diabetes**  | 0: No, 1: Yes                  |  


## 🎯 Prediction Logic
**1️⃣ User enters health parameters.**
**2️⃣ BMI is calculated automatically.**
**3️⃣ The ML model predicts the probability of cardiovascular risk.**
**4️⃣ Risk levels:**

**Low Risk: Below 30%**
**Medium Risk: 30% - 60%**
**High Risk: Above 60%**


## 🛠 Future Improvements
**🔹 Enhance UI with Bootstrap or React**
**🔹 Deploy on Heroku or Render**
**🔹 Add more health features for better accuracy**


## **👥 Contributors**

**Ayush Gangwar** - Developer

Open to contributions! 🤝


## ☕ Support Me

Do you like My projects? You can show your support by buying me a coffee! Your contributions motivate me to keep improving and building more awesome projects. 💻❤  
[![Buy Me a Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](http://buymeacoffee.com/Arya182)
