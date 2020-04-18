# import modules
import csv
import pathlib

# set path for file budget_data.csv
dataset = pathlib.Path("./Resources/budget_data.csv")

# create variables and lists
month_count = 0
current_pl = 0
last_pl = 0
monthly_pl_change = 0
month = []
pl_total = []
monthly_pl_changes = []

# open csv
with open(dataset, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # skip over header
    csv_header = next(csvreader)

    # loop through rows to gather month to month data
    for row in csvreader:

        # count months    
        month_count = month_count + 1

        # gather date and p&l lists
        month.append(row[0])
        pl_total.append(int(row[1]))

        # calculate monthly pl change
        current_pl = int(row[1])

        if last_pl != int():
            monthly_pl_change = current_pl - last_pl
            monthly_pl_changes.append(monthly_pl_change)

        last_pl = current_pl

# make calculations for total revenue and average of changes
revenue_total = sum(pl_total)

# calculate monthly changes average
total_monthly_pl_changes = sum(monthly_pl_changes)
average_change = total_monthly_pl_changes / (month_count - 1)

# calculate monthly change max/date and min/date
max_pl = max(monthly_pl_changes)
min_pl = min(monthly_pl_changes)
max_index = monthly_pl_changes.index(max_pl)
min_index = monthly_pl_changes.index(min_pl)
max_month = month[max_index+1] 
min_month = month[min_index+1]

# print to terminal
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${revenue_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_month} (${max_pl})")
print(f"Greatest Decrease in Profits: {min_month} (${min_pl})")

# write to text file
output_path = pathlib.Path("./Analysis/PyBank_Analysis.txt")

text_file = open(output_path, "w")

lines_of_text = [
    "Financial Analysis" + "\n",
    "-----------------------------" + "\n",
    f"Total Months: {month_count}" + "\n",
    f"Total: ${revenue_total}" + "\n",
    f"Average Change: ${average_change:.2f}" + "\n",
    f"Greatest Increase in Profits: {max_month} (${max_pl})" + "\n",
    f"Greatest Decrease in Profits: {min_month} (${min_pl})" + "\n"
    ]

text_file.writelines(lines_of_text)

text_file.close()