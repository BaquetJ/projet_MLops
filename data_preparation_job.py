# Data Preparation Job
# This script handles data cleaning and preparation for the workflow.

import pandas as pd

def load_data(file_path):
    """Load the dataset from a CSV file."""
    return pd.read_csv(file_path)

def clean_data(data):
    """Perform data cleaning operations."""
    data = data.dropna()
    return data

def save_data(data, output_path):
    """Save the cleaned data to a CSV file."""
    data.to_csv(output_path, index=False)

if __name__ == "__main__":
    input_path = "./DATA/pokemon.csv"
    output_path = "./DATA/cleaned_pokemon.csv"

    data = load_data(input_path)
    cleaned_data = clean_data(data)
    save_data(cleaned_data, output_path)
    print("Data preparation completed.")