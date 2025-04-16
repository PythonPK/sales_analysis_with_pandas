import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv('sales_data.csv')

# Preview the first few rows of the DataFrame
print(data.head())

# Check dimensions
print(data.shape)

# Summary statistics
print(data.describe())

# Check for missing values
print(data.isnull().sum())

# Fill missing values (example)
data['Units Sold'] = data['Units Sold'].fillna(0)

# Standardize column names
data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')

# Convert 'Date of Sale' to a datetime object
data['date_of_sale'] = pd.to_datetime(data['date_of_sale'])

# Total sales by product
total_sales = data.groupby('product')['revenue_($)'].sum()
print(total_sales)

# Average units sold
average_units = data['units_sold'].mean()
print(f"Average Units Sold: {average_units}")

# Filter Electronics category
electronics = data[data['category'] == 'Electronics']
print(electronics)

# Plot sales trend over time
data.groupby('date_of_sale')['revenue_($)'].sum().plot(kind='line')
plt.title('Revenue Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.show()

# Save the cleaned data to a new CSV file
data.to_csv('cleaned_sales_data.csv', index=False)
print("Cleaned data saved successfully!")