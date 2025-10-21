import pandas as pd
import random

# -------------------------
# Step 1: Define parameters
# -------------------------
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

floors_range = [1, 2, 3, 4, 5,6,7]   # Number of floors
bathrooms_range = [1, 2, 3,4]
total_sqft_range = {
    1: (400, 800),
    2: (800, 1200),
    3: (1200, 2000),
    4: (2000, 3500),
    5: (2500, 4000),
    5: (3000, 5000)
}
furnishing_options = ["Furnished", "Semi-Furnished", "Unfurnished"]
age_range = (0, 30)  # years

# Price and Rent multipliers per sq.ft (rough realistic values)
price_per_sqft = {
    "MP Nagar": 8000,
    "Bittan Market": 7000,
    "Arera Colony": 7500,
    "Kolar Road": 5000,
    "Habibganj": 5500,
    "Shivaji Nagar": 6000,
    "Bawadiya Kalan": 4500,
    "Indrapuri": 4000,
    "Nizamuddin colony": 6500,
    "Lalghati": 4800,
    "Ashoka garden": 5200,
    "Narela": 4300,
    "Ayodhya nagar": 6200,
    "Anand nagar": 5800,
    "Ratnagiri": 4700,
    "Sonagiri": 4600,
    "Piplani": 7000,
    "Karond": 4900,
    "Vijay nagar": 7200,
    "Saket nagar": 6800,
    "Barkheda": 4400,
    "Govindpura": 5300,
    "Hoshangabad Road": 5100,
    "Bairagarh": 4500,
    "Misrod": 4200,
    "Arjun Nagar": 6000,
    "Chuna Bhatti": 4700,
    "Gulmohar": 6400,
    "Shyamla Hills": 7500,
    "Service road": 5800,
    "Prabhat petrol pump": 4900,
    "jahangirabad": 4600,
    "ibrahimpura": 4300,
    "sultaniya road": 5200,
    "New market": 7000,
    "Roshanpura": 4800,
    "kohefiza": 4500,
    "eidgah hills": 6000,
    "Tajul masjid": 5500,
    "Gandhi nagar": 6200,
    "Ayodhya bypass": 5300,
    "Minal": 4700,
    "Vikas Nagar": 6800,
    "Shanti Nagar": 5900,
    "Kamla Nagar": 5200,
    "Avadhpuri": 4400,
    "Kolar hills": 5000,
    "char Imli": 6600,
    "chuna bhatti": 4700,
    "VIP road": 6500 
}
rent_per_sqft = {
    "MP Nagar": 25,
    "Bittan Market": 22,
    "Arera Colony": 24,
    "Kolar Road": 15,
    "Habibganj": 18,
    "Shivaji Nagar": 20,
    "Bawadiya Kalan": 12,
    "Indrapuri": 10,
    "Nizamuddin colony": 21,
    "Lalghati": 14,
    "Ashoka garden": 16,
    "Narela": 11,
    "Ayodhya nagar": 23,
    "Anand nagar": 19,
    "Ratnagiri": 13,
    "Sonagiri": 12,
    "Piplani": 22,
    "Karond": 14,
    "Vijay nagar": 24,
    "Saket nagar": 23,
    "Barkheda": 13,
    "Govindpura": 16,
    "Hoshangabad Road": 15,
    "Bairagarh": 12,
    "Misrod": 11,
    "Arjun Nagar": 20,
    "Chuna Bhatti": 13,
    "Gulmohar": 21,
    "Shyamla Hills": 25,
    "Service road": 19,
    "Prabhat petrol pump": 14,
    "jahangirabad": 12,
    "ibrahimpura": 11,
    "sultaniya road": 16,
    "New market": 22,
    "Roshanpura": 14,
    "kohefiza": 12,
    "eidgah hills": 20,
    "Tajul masjid": 18,
    "Gandhi nagar": 23,
    "Ayodhya bypass": 16,
    "Minal": 13,
    "Vikas Nagar": 23,
    "Shanti Nagar": 19,
    "Kamla Nagar": 16,
    "Avadhpuri": 13,
    "Kolar hills": 15,
    "char Imli": 21,
    "chuna bhatti": 13,
    "VIP road": 21

}

# -------------------------
# Step 2: Generate Data
# -------------------------
num_samples = 10000 # number of rows
data = []

for _ in range(num_samples):
    location = random.choice(locations)
    # floors = random.choice(floors_range)
    floors = random.choice(list(total_sqft_range.keys()))
    washroom = random.choice(bathrooms_range)
    total_sqft = random.randint(*total_sqft_range[floors])
    furnishing = random.choice(furnishing_options)
    age = random.randint(*age_range)
    
    price = total_sqft * price_per_sqft[location] + random.randint(-100000, 100000)
    rent = total_sqft * rent_per_sqft[location] + random.randint(-2000, 2000)
    
    data.append([
        location, floors, washroom, total_sqft, furnishing, age, price, rent
    ])

# -------------------------
# Step 3: Create DataFrame
# -------------------------
columns = ["location", "floors", "washroom", "total_sqft", "furnishing", "age", "price", "rent"]
df = pd.DataFrame(data, columns=columns)

# -------------------------
# Step 4: Save CSV
# -------------------------
df.to_csv("house_data.csv", index=False)
print("house_data.csv generated successfully!")
