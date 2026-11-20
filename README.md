# -HclTech-Carrer-Shaper-Python-Project :Bank Transcation Pattern Analysis
 Title: Analysis of Bank Transactions using Python.
 
Objective:
The main aim of this practical is to analyse bank transactions data. We have to clean the data, check missing values and duplicates, and then find out total credit/debit, transaction by channel and city, flagged transactions, and top 10 largest transactions.

Tools Used:
Python Pandas library - for working with data 
Numpy library - for numbers and bins
Excel file - bank_transactions.csv.xlsx4.

Dataset Used:
The dataset contains columns like Transaction_ID, Transaction_Type, Amount_INR, Channel, City and Flagged. 
Some values in Amount_INR were missing.

Steps Followed:
Step 1: First we imported pandas and numpy and loaded the Excel file using read_excel.

Step 2: We checked first few rows using head() and full info using info() to understand the data.

Step 3: We found missing values in Amount_INR and filled them with median value. Median is used because it is not affected by very large values.

Step 4: We checked duplicate Transaction_IDs to see if any transaction is repeated.

Step 5: We calculated total credit and total debit using groupby.

Step 6: We calculated mean, median and standard deviation of Amount_INR.

Step 7: We checked transaction volume by Channel using value_counts and total value by City using groupby.

Step 8: We counted flagged transactions and found flagged percentage.

Step 9: We found top 10 largest transactions using nlargest.

Step 10: At last we made amount bands like Low, Medium, High, Very High using pd.cut and counted how many transactions are in each band.


Output:
After running we get total credit/debit, average amount, most used channel, city with highest transactions, flagged percentage, top 10 transactions and count of each amount band.

8. Conclusion:
From this analysis we can understand how customers are using bank services, which channel is most popular, and which transactions are flagged. This type of analysis is useful for banks to find fraud and to improve services.
