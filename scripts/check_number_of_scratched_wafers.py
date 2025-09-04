import pandas as pd
import zipfile

# Load the training data
zf = zipfile.ZipFile('data.zip') 
df = pd.read_csv(zf.open('wafers_train.csv'))


# Identify wafers with at least one scratch
scratched = df.loc[df['IsScratchDie'] == True, 'WaferName'].unique()

# Output the count and list
print(f"Number of wafers containing scratches: {len(scratched)}")
print("Wafers with scratches:")
# for w in scratched:
#     print(f" - {w}")
