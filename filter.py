import pandas as pd
import os

# Define input and output directories
input_dir = "initial_dataset"
output_dir = "filtered_datasets"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# List of all US state abbreviations
states = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA",
    "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NC", "ND", "NY", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", 
    "VA", "WA", "WV", "WI", "WY"
]

# Read original dataset
input_file = os.path.join(input_dir, "US_Accidents_March23.csv")
df = pd.read_csv(input_file)

# Iterate through each state and filter
for state in states:
    filtered_df = df[df["State"] == state]
    output_file = os.path.join(output_dir, f'traffic-accident-filtered_{state}.csv')
    filtered_df.to_csv(output_file, index=False)
    print(f"Filtered CSV file for state {state} created.")

print("All filtered files have been created.")
