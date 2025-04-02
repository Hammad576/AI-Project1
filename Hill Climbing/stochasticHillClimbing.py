#Schotastic moves randomly of the availible paths to introduce randomness
import pandas as pd
import random

# Step 1: Load the dataset
dataset_path = "../US_Crime_DataSet.csv"  # Adjust the path if needed
df = pd.read_csv(dataset_path, low_memory=False)

# Step 2: Ensure required columns exist
if "City" not in df.columns or "Crime Type" not in df.columns:
    print("Error: Required columns (City, Crime Type) not found in dataset.")
    exit()

# Step 3: Create a dictionary where cities are mapped to their crime count
crime_data = df.groupby("City")["Crime Type"].count().to_dict()

# Step 4: Define the Stochastic Hill Climbing function
def stochastic_hill_climbing(start_city):
    current_city = start_city
    current_crime_count = crime_data.get(current_city, 0)

    print(f"Starting at: {current_city} with {current_crime_count} crimes")

    while True:
        # Step 5: Select random neighbors
        neighbors = random.sample(list(crime_data.keys()), min(5, len(crime_data)))  # Pick 5 random neighbors
        
        # Step 6: Assign probabilities based on crime count (higher crime → higher probability)
        neighbors_with_probabilities = [
            (neighbor, crime_data.get(neighbor, 0)) for neighbor in neighbors
        ]
        neighbors_with_probabilities.sort(key=lambda x: x[1], reverse=True)  # Sort by crime count

        # Step 7: Choose a neighbor based on weighted probability
        best_neighbor = random.choices(neighbors_with_probabilities, weights=[n[1] for n in neighbors_with_probabilities])[0][0]
        best_crime_count = crime_data.get(best_neighbor, 0)

        # Step 8: Move if the selected neighbor has higher crime count
        if best_crime_count > current_crime_count:
            print(f"Moving to: {best_neighbor} with {best_crime_count} crimes")
            current_city = best_neighbor
            current_crime_count = best_crime_count
        else:
            print(f"Local maximum reached at: {current_city} with {current_crime_count} crimes")
            return current_city, current_crime_count

# Step 9: Pick a random starting city
random_start_city = random.choice(list(crime_data.keys()))
stochastic_hill_climbing(random_start_city)
