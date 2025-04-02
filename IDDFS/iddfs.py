import pandas as pd

# Load dataset
dataset_path = "../US_Crime_DataSet.csv"
df = pd.read_csv(dataset_path, low_memory=False)

# Required columns
required_columns = ["State", "Victim Race"]
if not all(col in df.columns for col in required_columns):
    print("Error: Required columns not found in dataset.")
    exit()

# Step 1: Build Stack (State -> Victim Races)
state_stack = []
for state, race in zip(df["State"], df["Victim Race"]):
    state_stack.append((state.strip(), race.strip()))

# Step 2: Depth-Limited DFS (DLS)
def depth_limited_dfs(stack, target_state, target_race, depth_limit):
    visited = set()
    current_depth = 0

    while stack:
        state, race = stack.pop()

        # Respect depth limit
        if current_depth > depth_limit:
            continue

        print(f"Visiting: {state}, Race: {race}, Depth: {current_depth}")

        # Check condition
        if state == target_state and race == target_race:
            print(f"Found '{target_race}' in '{target_state}' at depth {current_depth}!")
            return True

        visited.add((state, race))
        current_depth += 1  # Increment depth

    print("Target not found within depth limit.")
    return False

# Step 3: Run DLS
target_state = "Alaska"
target_race = "Black"
depth_limit = 3

depth_limited_dfs(state_stack, target_state, target_race, depth_limit)
