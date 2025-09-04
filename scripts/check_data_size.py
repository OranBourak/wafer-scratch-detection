import pandas as pd

# Load the CSV file
df = pd.read_csv('./data/wafers_train.csv')  # Replace with your actual file name

# Count number of unique wafers
num_wafers = df['WaferName'].nunique()
print(f"Number of unique wafers: {num_wafers}")

# Count how many dies each wafer has
dies_per_wafer = df.groupby('WaferName').size()
print("\nNumber of dies per wafer:")
print(dies_per_wafer)
