"""
InvestmentReport
GitHub: [JeffAllen714](https://github.com/JeffAllen714)

* * * * * * * * * * * * * * * * * * * * * * * * * * * *

## Description ##
This is a basic investment report tool that utilizes Pandas and Tabulate to provide a clean look.*

## Features ##

- Collects user information such as investment amount, number of years, and interest rate.
- Calculates and displays the ending balance and total interest earned for each period.
- Utilizes Pandas for efficient data handling and Tabulate for creating visually appealing tables.

## How to Use ##

1. Run the script.
2. Enter the investment amount, investment duration, and interest rate when prompted.
3. Marvel at the neatly formatted investment report.

* * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""

import pandas as pd
from tabulate import tabulate


# Variables
InvAmt = float(input("Enter the investment amount: "))
InvDur = int(input("Enter the number of periods: "))
IntRate = int(input("Enter the rate as a %: "))
EndBal = InvAmt * (1 + (IntRate / 100))
InterestAmt = InvAmt * (IntRate / 100)
StartAmt = InvAmt

# Initialize data list for DataFrame
data = []

# Loop that creates the dividend report via the user inputs (investment amount, number of periods, rate as a %)
for period in range(1, InvDur + 1):
    # Years Until Last Period
    if period > 1:
        # Change the Variables for the following years
        InvAmt = EndBal
        EndBal = InvAmt * (1 + (IntRate / 100))
        InterestAmt = InvAmt * (IntRate / 100)
    # Append each variable to the data list
    data.append([period, InvAmt, InterestAmt, EndBal])

# Creating a DataFrame
columns = ["Year", "Starting Balance", "Interest", "Ending Balance"]
df = pd.DataFrame(data, columns=columns)

# Set "Year" as the index
df = df.set_index("Year")

# Modify the formatting of float columns in the DataFrame
df["Starting Balance"] = df["Starting Balance"].apply(lambda x: "{:.2f}".format(x))
df["Interest"] = df["Interest"].apply(lambda x: "{:.2f}".format(x))
df["Ending Balance"] = df["Ending Balance"].apply(lambda x: "{:.2f}".format(x))

# Printing the DataFrame with two decimal places for floats using tabulate
print(tabulate(df, headers='keys', tablefmt='pretty'))

# Show the final ending balance & Total Interest Earned
TIE = EndBal - StartAmt
print("\nEnding Balance:", "{:.2f}".format(EndBal))
print("Total Interest Earned:", "{:.2f}".format(TIE))
