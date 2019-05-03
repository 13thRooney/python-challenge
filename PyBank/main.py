# Import modules
import os
import csv

# Set path for file
csvpathPyBank = os.path.join("..", "Resources", "budget_data.csv")

# Create empty lists to store 'Date', 'Profit/Loss' and 'Change in P&L'
month = []
profit_loss = []
profit_loss_change = []

# Open & Read the CSV file
with open(csvpathPyBank, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # To skip header line
    header = next(csvreader)

    # Loop through and append 'Date' and 'Profit/Loss' data to corresponding lists
    for row in csvreader:
        month.append(row[0])
        profit_loss.append(int(row[1]))
    
    # Loop through and append 'Change in P&L' data to appropriate list
    for i in range(len(profit_loss) - 1):
        profit_loss_change.append(profit_loss[i + 1] - profit_loss[i])

    # Calculate greatest increase in profits (date and amount) over the entire period
    month_greatest_increase = profit_loss_change.index(max(profit_loss_change)) + 1
    profit_loss_greatest_increase = max(profit_loss_change)

    # Calculate greatest decrease in losses (date and amount) over the entire period
    month_greatest_decrease = profit_loss_change.index(min(profit_loss_change)) + 1
    profit_loss_greatest_decrease = min(profit_loss_change)

    # Print all statements

print(f"""Financial Analysis
----------------------------
Total Month: {len(month)}
Total: ${sum(profit_loss)}
Average Change: ${round(sum(profit_loss_change)/len(profit_loss_change),2)}
Greatest Increase in Profits: {month[month_greatest_increase]} (${(str(profit_loss_greatest_increase))})
Greatest Decrease in Profits: {month[month_greatest_decrease]} (${(str(profit_loss_greatest_decrease))})
""")

# Output
output_path = os.path.join("..", "PyBank", "Financial_Analysis.txt")

# Print results to output file
with open(output_path, "w") as file:
    
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(month)}")
    file.write("\n")
    file.write(f"Total: ${sum(profit_loss)}")
    file.write("\n")
    file.write(f"Average Change: ${round(sum(profit_loss_change)/len(profit_loss_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {month[month_greatest_increase]} (${(str(profit_loss_greatest_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {month[month_greatest_decrease]} (${(str(profit_loss_greatest_decrease))})")
      