Data Analytics Project: Sales Analysis with pandas

Overview
This project demonstrates the basics of data analytics using the pandas library. You will analyze a dataset containing product sales information, clean the data, calculate summaries, and visualize trends.
Objectives
- Load and explore the dataset.
- Clean and preprocess the data.
- Perform calculations like total sales per product, average sales, and overall statistics.
- Visualize trends using pandas built-in plotting features.

Prerequisites
- Python 3.10 installed in your data_analytics Conda environment.
- pandas library installed.
- Git Bash for running scripts.

Dataset
Download the sample dataset file sales_data.csv or create it with the following structure: | Product | Category | Units Sold | Revenue ($) | Date of Sale | |---------|----------|------------|-------------|--------------| | Product A | Electronics | 100 | 5000 | 2025-01-01 | | Product B | Furniture | 50 | 7500 | 2025-01-02 |
Save this file in the same directory as your script.
Steps
1. Load the Dataset
import pandas as pd

# Load the dataset
data = pd.read_csv('sales_data.csv')

# Preview the first few rows
print(data.head())


2. Clean the Data
- Handle missing values.
- Standardize column names.

# Check for missing values
print(data.isnull().sum())

# Fill missing values or drop rows
data = data.dropna()

# Standardize column names
data.columns = [col.strip().lower().replace(' ', '_') for col in data.columns]
print(data.columns)

3. Perform Analysis
- Total sales per product:

total_sales = data.groupby('product')['revenue_($)'].sum()
print(total_sales)


- Average units sold:

average_units_sold = data['units_sold'].mean()
print(f"Average Units Sold: {average_units_sold}")


4. Visualize the Data
import matplotlib.pyplot as plt

# Sales trend over time
data['date_of_sale'] = pd.to_datetime(data['date_of_sale'])
data.groupby('date_of_sale')['revenue_($)'].sum().plot(kind='line')
plt.title("Revenue Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue ($)")
plt.show()


5. Save the Cleaned Data
data.to_csv('cleaned_sales_data.csv', index=False)
print("Cleaned data saved!")


Project Completion
Once you've completed the steps above:
- Commit your changes to GitHub.
- Open a pull request if working collaboratively.



