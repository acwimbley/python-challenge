import os

import csv

# Read the CSV file

csvpath = 'PyBank/Resources/budget_data.csv'

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header row

    # Initialize variables
    total_months = 0
    net_total = 0
    previous_profit_loss = 0
    changes = []
    dates = []

    # Loop through rows in the CSV
    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])

        # Calculate total months and net total
        total_months += 1
        net_total += profit_loss

        # Calculate change in profit/loss
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            dates.append(date)

        previous_profit_loss = profit_loss

# Calculate average of changes
average_change = sum(changes) / len(changes)

# Find the greatest increase in profits
max_increase_index = changes.index(max(changes))
max_increase_date = dates[max_increase_index]
max_increase_amount = max(changes)

# Find the greatest decrease in profits
max_decrease_index = changes.index(min(changes))
max_decrease_date = dates[max_decrease_index]
max_decrease_amount = min(changes)

# Printing the results
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase_amount:.2f})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease_amount:.2f})")


# Export the results to a text file
output_file_path = "budget_analysis_results.txt"
with open(output_file_path, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Net Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {max_increase_date} (${max_increase_amount:.2f})\n")
    output_file.write(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease_amount:.2f})\n")

print(f"Results exported to {output_file_path}")
