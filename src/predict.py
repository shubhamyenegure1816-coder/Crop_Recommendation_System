import joblib
import pandas as pd
from fertilizer import fertilizer_advice

# Load trained crop model
model = joblib.load("crop_model.pkl")

print()
print("=" * 50)
print("             CROP & FERTILIZER SYSTEM")
print("=" * 50)

# Get input from user
n = float(input("Enter Nitrogen (N): "))
p = float(input("Enter Phosphorus (P): "))
k = float(input("Enter Potassium (K): "))
temperature = float(input("Enter Temperature (°C): "))
humidity = float(input("Enter Humidity (%): "))
ph = float(input("Enter Soil pH: "))
rainfall = float(input("Enter Rainfall (mm): "))

# Prepare input
input_data = [[
    n,
    p,
    k,
    temperature,
    humidity,
    ph,
    rainfall
]]

# Predict crop
input_data = pd.DataFrame(
    input_data,
    columns=model.feature_names_in_
)

prediction = model.predict(input_data)
# Fertilizer recommendation
fertilizer = fertilizer_advice(n, p, k)

# Display final result
print()
print("=" * 50)
print("                 FINAL RESULT")
print("=" * 50)
print("Recommended Crop       :", prediction[0])
print("Recommended Fertilizer :", fertilizer)
print("=" * 50)