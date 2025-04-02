import pandas as pd

# Load the dataset  
dataset_path = "../US_Crime_DataSet.csv"
df = pd.read_csv(dataset_path, low_memory=False) 
 # Store the content in df

# Displaying my data set Columns
print("Dataset Columns:", df.columns)

# Creating a dictionary where key is city and values are the crimes that occured in that city
crimeDictionary = {}
 
# Implementing bfs using Queue First come first served 
# our dictionary is looking like {
  #  "Los Angeles": ["Murder", "Burglary"],
 #   "Chicago": ["Fraud"]
 

if "City" in df.columns and "Crime Type" in df.columns:
    for _, row in df.iterrows():
        city = str(row["City"]).strip()
        crime_type = str(row["Crime Type"]).strip()
        
        # Ensure we only add edges between city and its crime types, NOT between cities
        if city and crime_type and city.lower() != crime_type.lower():
            if city not in crimeDictionary:
                crimeDictionary[city] = []
            crimeDictionary[city].append(crime_type)

# Breadth-First Search (BFS) Implementation using a Queue
def bfsSearch(graph, start_node):
    visited = set()
    queue = [start_node]
    
    print(f"Finding all crimes linked to {start_node} using BFS:")
    
    while queue:
        node = queue.pop(0)  # Dequeue first element
        if node not in visited:
            print("Exploring:", node)
            visited.add(node)
            
            #  Exploring neighbors Level by Level
            if node in graph:
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

# We will search the city Los Angeles
startCity = "Anchorage"

if startCity in crimeDictionary:
    bfsSearch(crimeDictionary, startCity)
else:
    print("Error ! The requested City not found in Record.",startCity )

