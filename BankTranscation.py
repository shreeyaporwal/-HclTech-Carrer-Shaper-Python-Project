import pandas as pd
import numpy as np

#  Load and inspect dataset-------------------
file_name = 'bank_transactions.csv.xlsx'
df = pd.read_excel(file_name, sheet_name=0)

print("--- Dataset Preview ---")
print(df.head(3))
print(df.info())

# Handle missing transaction amounts-------------
missing_count = df['Amount_INR'].isnull().sum()
median_value = df['Amount_INR'].median()

# Fill blanks with the median amount----------------
df['Amount_INR'] = df['Amount_INR'].fillna(median_value)
print(f"\n--- Missing Values ---")
print(f"Found {missing_count} missing amounts. Filled them with median: {median_value}")

#  Check duplicate Transaction IDs-------------------
duplicates = df['Transaction_ID'].duplicated().sum()
print(f"\n-- Duplicates ---")
print(f"Duplicate Transaction IDs found: {duplicates}")

#  Calculate total credits and debits----------------
print(f"\n-- Total Credits and Debits ---")
print(df.groupby('Transaction_Type')['Amount_INR'].sum())

# Calculate mean, median, and standard deviation------------
print(f"\n---Amount Statistics ---")
print(f"Mean   : {df['Amount_INR'].mean():.2f}")
print(f"Median : {df['Amount_INR'].median():.2f}")
print(f"StdDev : {df['Amount_INR'].std():.2f}")

# . Compare transaction volume by channel-----------------
print(f"\n---Transaction Volume by Channel ---")
print(df['Channel'].value_counts())


# Compare total transaction value by city-------------------
print(f"\n-- Total Value by City ---")
print(df.groupby('City')['Amount_INR'].sum())

#  Calculate flagged transaction count and percentage-----------
flagged_counts = df['Flagged'].value_counts()
flagged_percentage = (df['Flagged'] == 'Yes').mean() * 100
print(f"\n---Flagged Summary ---")
print(flagged_counts)
print(f"Flagged Percentage: {flagged_percentage:.2f}%")


# Find the 10 largest transactions-------------------------------
print(f"\n--- Top 10 Largest Transactions ---")
print(df.nlargest(10, 'Amount_INR')[['Transaction_ID', 'Transaction_Type', 'Amount_INR', 'Channel', 'City']])

# Create transaction amount bands------------------------------
bins = [0, 1000, 5000, 10000, np.inf]
labels = ['Low (<1k)', 'Medium (1k-5k)', 'High (5k-10k)', 'Very High (>10k)']
df['Amount_Band'] = pd.cut(df['Amount_INR'], bins=bins, labels=labels, right=False)

print(f"\n---Amount Bands ---")
print(df['Amount_Band'].value_counts())