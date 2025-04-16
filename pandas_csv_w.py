import pandas as pd

# Data to write
data = {
    "Product": ["Product A", "Product B"],
    "Category": ["Electronics", "Furniture"],
    "Units Sold": [100, 50],
    "Revenue ($)": [5000, 7500],
    "Date of Sale": ["2025-01-01", "2025-01-02"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Write to a CSV file
df.to_csv('sales_data.csv', index=False)

print("CSV file created successfully!")
