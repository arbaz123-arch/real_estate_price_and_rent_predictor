# src/data_preprocessing.py

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def load_data(file_path):
    """
    Load CSV data into a pandas DataFrame
    """
    df = pd.read_csv(file_path)
    return df

def handle_missing_values(df):
    """
    Fill missing numerical values with median
    Fill missing categorical values with mode
    """
    for column in df.columns:
        if df[column].dtype == 'object':
            df[column].fillna(df[column].mode()[0], inplace=True)
        else:
            df[column].fillna(df[column].median(), inplace=True)
    return df

def encode_categorical(df):
    """
    Encode all categorical columns using LabelEncoder
    """
    le = LabelEncoder()
    for column in df.columns:
        if df[column].dtype == 'object':
            df[column] = le.fit_transform(df[column])
    return df

def preprocess_data(file_path):
    """
    Full preprocessing pipeline:
    1. Load data
    2. Handle missing values
    3. Encode categorical columns
    """
    df = load_data(file_path)
    df = handle_missing_values(df)
    df = encode_categorical(df)
    return df

# Example usage:
if __name__ == "__main__":
    house_df = preprocess_data("data/house_data.csv")
    flat_df = preprocess_data("data/flat_data.csv")
    
    print("House Data Sample:")
    print(house_df.head())
    
    print("\nFlat Data Sample:")
    print(flat_df.head())
