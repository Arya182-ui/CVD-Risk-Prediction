import pickle

# Model Load Karo
with open('cardio_risk_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Check Model Feature Order
print(model.feature_names_in_)  # Ye check karega training ke feature names
