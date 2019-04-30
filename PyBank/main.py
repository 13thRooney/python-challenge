import os
import csv

budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

def print_financial_analysis(budget_data):
    month = int(budget_data[0])
    profit_loss = int(budget_data[1])

    total_months = len(month)
    total_profit_loss = sum(profit_loss)

    print(f"Total Months: {str(total_months)}")
    print(f"Total P&L: {str(total_profit_loss)}")

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Prompt the user for what wrestler they would like to search for
    month_to_check = input("What month do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if month_to_check == row[0]:
            print_financial_analysis(row)