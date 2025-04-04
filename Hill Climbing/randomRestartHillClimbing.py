# we are randomly restarting to find the golabal maxima
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

# Step 4: Define the Random-Restart Hill Climbing function
def random_restart_hill_climbing(max_restarts=5):
    best_city = None
    best_crime_count = 0

    for restart in range(max_restarts):  # Allow multiple restarts
        print(f"\nRestart {restart + 1} / {max_restarts}")

        # Step 5: Pick a random starting city
        current_city = random.choice(list(crime_data.keys()))
        current_crime_count = crime_data.get(current_city, 0)
        print(f"Starting at: {current_city} with {current_crime_count} crimes")

        while True:
            # Step 6: Select random neighbors
            neighbors = random.sample(list(crime_data.keys()), min(5, len(crime_data)))  # Pick 5 random neighbors
            best_neighbor = current_city
            best_neighbor_crime_count = current_crime_count

            for neighbor in neighbors:
                neighbor_crime_count = crime_data.get(neighbor, 0)
                if neighbor_crime_count > best_neighbor_crime_count:  # Move to a city with higher crime rate
                    best_neighbor = neighbor
                    best_neighbor_crime_count = neighbor_crime_count

            # Step 7: If no better neighbor is found, stop (local maximum reached)
            if best_neighbor == current_city:
                print(f"Local maximum reached at: {current_city} with {current_crime_count} crimes")
                break

            # Step 8: Move to the best neighbor
            print(f"Moving to: {best_neighbor} with {best_neighbor_crime_count} crimes")
            current_city = best_neighbor
            current_crime_count = best_neighbor_crime_count

        # Step 9: Keep track of the best solution found across all restarts
        if current_crime_count > best_crime_count:
            best_city = current_city
            best_crime_count = current_crime_count

    print("\nBest overall city found:", best_city, "with", best_crime_count, "crimes")

# Step 10: Run the Random-Restart Hill Climbing Algorithm
random_restart_hill_climbing(max_restarts=5)
