import pandas as pd

# 1. Load the data
file_name = "train.csv" 
df = pd.read_csv(file_name)

# 2. Clean the column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# 3. Convert dates to actual date formats
df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True)
df['ship_date'] = pd.to_datetime(df['ship_date'], dayfirst=True)

# 4. Quick check to see if it worked
print("--- Cleaned Column Names ---")
print(df.columns.tolist())

print("\n--- First 3 rows ---")
print(df[['order_date', 'region', 'sales']].head(3))

# 5. Save the cleaned data to a new file
df.to_csv("clean_superstore.csv", index=False)
print("\n✅ Cleaned data saved as clean_superstore.csv!")