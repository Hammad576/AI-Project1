import numpy as np
import pandas as pd

# Load the dataset  
dataset_path = "../US_Crime_DataSet.csv"
df = pd.read_csv(dataset_path, low_memory=False)  # Store the content in df

# Display dataset structure
print(df.head())

# Check if required columns exist
required_columns = {"City", "Incident", "Crime Type", "Crime Solved"}
if not required_columns.issubset(df.columns):
    raise ValueError(f"Dataset must contain {required_columns} columns.")

# Group data by City to analyze crime frequency
crime_stats = df.groupby("City").agg(
    total_incidents=("Incident", "count"),   # Count total crimes per city
    unsolved_crimes=("Crime Solved", lambda x: (x == "No").sum())  # Count unresolved cases
).reset_index()

# Min-Max Logic: Predict criminal movement & best police response
def min_max_decision(crime_data):
    """
    - Criminals move to cities with lower police action (high unresolved crimes).
    - Police should focus on cities with highest crime occurrence.
    """
    if crime_data.empty:
        return "No data", "No data"

    least_policed_city = crime_data.loc[crime_data["unsolved_crimes"].idxmax(), "City"]
    most_crime_city = crime_data.loc[crime_data["total_incidents"].idxmax(), "City"]

    return least_policed_city, most_crime_city

# Get predictions
predicted_crime_city, police_deployment_city = min_max_decision(crime_stats)

# Display Results
print(f"Predicted Crime City (high unresolved cases): {predicted_crime_city}")
print(f"Best Police Deployment City (high crime occurrence): {police_deployment_city}")
