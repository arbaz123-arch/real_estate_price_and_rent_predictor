# src/feature_engineering.py

import pandas as pd

def create_total_rooms(df, room_col='rooms', washroom_col='washroom'):
    """
    TotalRooms = rooms + washroom
    """
    if room_col in df.columns and washroom_col in df.columns:
        df['TotalRooms'] = df[room_col] + df[washroom_col]
    return df

def create_price_per_sqft(df, price_col='price', sqft_col='total_sqft'):
    """
    Price per SqFt = price / total_sqft
    """
    if price_col in df.columns and sqft_col in df.columns:
        df['PricePerSqFt'] = df[price_col] / df[sqft_col]
    return df

def create_rent_per_sqft(df, rent_col='rent', sqft_col='total_sqft'):
    """
    Rent per SqFt = rent / total_sqft
    """
    if rent_col in df.columns and sqft_col in df.columns:
        df['RentPerSqFt'] = df[rent_col] / df[sqft_col]
    return df

def convert_age_to_numeric(df, age_col='age'):
    """
    Convert age column to numeric:
    - House: Already numeric
    - Flat: Strings like '1-5 years', '10+ years', 'New'
    """
    if age_col in df.columns:
        def age_to_num(age):
            if isinstance(age, str):
                if 'New' in age:
                    return 0
                elif '+' in age:
                    return int(age.split('+')[0])
                elif '-' in age:
                    return (int(age.split('-')[0]) + int(age.split('-')[1])) / 2
            return age
        df['age'] = df[age_col].apply(age_to_num)
    return df

def engineer_features(df, dataset_type='house'):
    """
    Full feature engineering pipeline
    """
    if dataset_type == 'house':
        df = create_total_rooms(df, room_col='rooms', washroom_col='washroom')
    else:  # flat
        df = create_total_rooms(df, room_col='bhk', washroom_col='washroom')

    df = create_price_per_sqft(df)
    df = create_rent_per_sqft(df)
    df = convert_age_to_numeric(df)
    
    return df

# Example usage:
if __name__ == "__main__":
    from data_preprocessing import preprocess_data

    house_df = preprocess_data("data/house_data.csv")
    flat_df = preprocess_data("data/flat_data.csv")

    house_df = engineer_features(house_df, dataset_type='house')
    flat_df = engineer_features(flat_df, dataset_type='flat')

    print("House Data with Features:")
    print(house_df.head())

    print("\nFlat Data with Features:")
    print(flat_df.head())
