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

First we loaded the Excel file and checked it with head and info. Then we filled the missing Amount_INR values with median and checked duplicate Transaction IDs. After that we calculated total credit and debit, mean, median, standard deviation, and checked transactions by channel and city. Then we found flagged transactions percentage and top 10 largest transactions. In the end we made amount bands like Low, Medium, High and Very High and counted them.


Output:
After running we get total credit/debit, average amount, most used channel, city with highest transactions, flagged percentage, top 10 transactions and count of each amount band.


Conclusion:
From this analysis we can understand how customers are using bank services, which channel is most popular, and which transactions are flagged. This type of analysis is useful for banks to find fraud and to improve services.
