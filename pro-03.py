import pandas as pd
# Read CSV file
df = pd.read_csv("data.csv")
# Display data
print("Data:")
print(df)

# Check rows and columns
print("Rows and Columns:")
print(df.shape)

# Check data types
print("Data Types:")
print(df.dtypes)

# Summary of numerical data
print("Summary:")
print(df.describe())

# Filter data
filtered = df[df["Marks"] >= 50]

print("Filtered Data:")
print(filtered)

# Remove missing values
cleaned = filtered.dropna()

# Save cleaned data
cleaned.to_csv("cleaned_data.csv", index=False)

print("Cleaned data saved successfully!")