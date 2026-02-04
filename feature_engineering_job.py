# Feature Engineering Job
# This script handles feature engineering for the workflow.

import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    """Load the cleaned dataset from a CSV file."""
    return pd.read_csv(file_path)

def engineer_features(data):
    """Perform feature engineering operations."""
    numerical_features = data.select_dtypes(include=['float64', 'int64']).columns
    scaler = StandardScaler()
    data[numerical_features] = scaler.fit_transform(data[numerical_features])
    return data

def save_data(data, output_path):
    """Save the engineered data to a CSV file."""
    data.to_csv(output_path, index=False)

if __name__ == "__main__":
    input_path = "./DATA/cleaned_pokemon.csv"
    output_path = "./DATA/engineered_pokemon.csv"

    data = load_data(input_path)
    engineered_data = engineer_features(data)
    save_data(engineered_data, output_path)
    print("Feature engineering completed.")