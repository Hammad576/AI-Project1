import pandas as pd
import random

#First Choice it moves as it finds a valid path. Faster
# Step 1: Load the dataset
dataset_path = "../US_Crime_DataSet.csv"  # Adjust the path if needed
df = pd.read_csv(dataset_path, low_memory=False)

# Step 2: Ensure required columns exist
if "City" not in df.columns or "Crime Type" not in df.columns:
    print("Error: Required columns (City, Crime Type) not found in dataset.")
    exit()

# Step 3: Create a dictionary where cities are mapped to their crime count
crime_data = df.groupby("City")["Crime Type"].count().to_dict()

# Step 4: Define the First-Choice Hill Climbing function
def first_choice_hill_climbing(start_city):
    current_city = start_city
    current_crime_count = crime_data.get(current_city, 0)

    print(f"Starting at: {current_city} with {current_crime_count} crimes")

    while True:
        # Step 5: Select a random neighbor
        neighbor = random.choice(list(crime_data.keys()))
        neighbor_crime_count = crime_data.get(neighbor, 0)

        # Step 6: Move to the first better neighbor found
        if neighbor_crime_count > current_crime_count:
            print(f"Moving to: {neighbor} with {neighbor_crime_count} crimes")
            current_city = neighbor
            current_crime_count = neighbor_crime_count
        else:
            print(f"Local maximum reached at: {current_city} with {current_crime_count} crimes")
            return current_city, current_crime_count

# Step 7: Pick a random starting city
random_start_city = random.choice(list(crime_data.keys()))
first_choice_hill_climbing(random_start_city)
