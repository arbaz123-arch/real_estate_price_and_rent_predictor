import pandas as pd
import random

# ✅ Locations of Bhopal
locations = [ 
    "MP Nagar", "Bittan Market", "Arera Colony", "Kolar Road",
    "Habibganj", "Shivaji Nagar", "Bawadiya Kalan", "Indrapuri","Nizamuddin colony","Lalghati",
    "Ashoka garden", "Narela", "Ayodhya nagar", "Anand nagar", "Ratnagiri", "Sonagiri", "Piplani",
    "Karond", "Vijay nagar", "Saket nagar", "Barkheda", "Govindpura", "Hoshangabad Road",
    "Bairagarh", "Misrod", "Arjun Nagar", "Chuna Bhatti", "Gulmohar", "Shyamla Hills",
    "Service road", "Prabhat petrol pump", "jahangirabad", "ibrahimpura", "sultaniya road", 
    "New market", "Roshanpura", "kohefiza", "eidgah hills", "Tajul masjid", "Gandhi nagar",
    "Ayodhya bypass", "Minal","Vikas Nagar", "Shanti Nagar", "Kamla Nagar","Avadhpuri", "Kolar hills",
    "char Imli", "chuna bhatti", "VIP road"
]

# ✅ Define possible BHK values
bhk_values = [1, 2, 3, 4, 5]

# ✅ Furnishing types
furnishings = ["Fully Furnished", "Semi Furnished", "Unfurnished"]

# ✅ Age options
ages = ["New", "1-5 years", "5-10 years", "10+ years"]

# ✅ Mapping for total sqft based on BHK
sqft_range = {
    1: (400, 800),
    2: (700, 1200),
    3: (1000, 1600),
    4: (1400, 2200),
    5: (2000, 3000)
}

# ✅ Function to generate random flat data
def generate_flat_data(n=10000):
    data = []
    for _ in range(n):
        location = random.choice(locations)
        bhk = random.choice(bhk_values)
        washroom = bhk if bhk <= 3 else bhk - 1
        total_sqft = random.randint(*sqft_range[bhk])
        furnishing = random.choice(furnishings)
        age = random.choice(ages)

        # Price (in lakhs)
        price = round(total_sqft * random.uniform(4000, 7000) / 100000, 2)

        # Rent (per month)
        rent = round(price * random.uniform(800, 1200), 2)

        data.append({
            "location": location,
            "bhk": bhk,
            "washroom": washroom,
            "total_sqft": total_sqft,
            "furnishing": furnishing,
            "age": age,
            "price": price,
            "rent": rent
        })
    return pd.DataFrame(data)

# ✅ Generate and save CSV
df_flats = generate_flat_data(10000)
df_flats.to_csv("data/flat_data.csv", index=False)
print("✅ Flat data generated successfully and saved to 'data/flat_data.csv'")
print(df_flats.head())
