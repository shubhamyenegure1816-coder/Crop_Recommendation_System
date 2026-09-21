import pandas as pd

print("Data preprocessing started")

# Load the dataset
df = pd.read_csv("dataset/Crop_recommendation.csv")

print("Dataset loaded successfully!")
print(df.head())

print("Dataset shape:", df.shape)
print("Columns:", df.columns.tolist())