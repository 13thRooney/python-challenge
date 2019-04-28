# import the os module
import os

#import module for reading CVS

import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

## PyPoll file is TOO BIG, need to ZIP!

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

#CALCULATE
#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The average of the changes in "Profit/Losses" over the entire period

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in losses (date and amount) over the entire period

# As an example, your analysis should look similar to the one below:

#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $38382578
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.