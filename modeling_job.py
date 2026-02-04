# Modeling Job
# This script handles model training and evaluation for the workflow.

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

def load_data(file_path):
    """Load the engineered dataset from a CSV file."""
    return pd.read_csv(file_path)

def train_model(data):
    """Train a Random Forest model."""
    X = data.drop('is_legendary', axis=1)
    y = data['is_legendary']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

    return model

if __name__ == "__main__":
    input_path = "./DATA/engineered_pokemon.csv"

    data = load_data(input_path)
    model = train_model(data)
    print("Modeling completed.")