import pandas as pd

# Read CSV file
file_name = "data.csv"

df = pd.read_csv(file_name)

# Display complete data
print("Original Data:")
print(df)

# 1. Display dimensions
print("\nDimensions of dataset:")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 2. Display data types
print("\nData Types:")
print(df.dtypes)

# 3. Display summary statistics
print("\nSummary Statistics:")
print(df.describe())

# 4. Filter rows according to a condition
# Example: select rows where Age is greater than 18
filtered_data = df[df["Age"] > 18]

print("\nFiltered Data (Age > 18):")
print(filtered_data)

# 5. Remove missing values
cleaned_data = filtered_data.dropna()

print("\nCleaned Data:")
print(cleaned_data)

# 6. Save cleaned data into a new CSV file
cleaned_data.to_csv("cleaned_data.csv", index=False)

# 7. Save cleaned data into Excel file
cleaned_data.to_excel("cleaned_data.xlsx", index=False)

print("\nFiles exported successfully!")