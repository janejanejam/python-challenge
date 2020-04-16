# import modules
import csv
import pathlib

# set path for file budget_data.csv
dataset = pathlib.Path("./Resources/budget_data.csv")

#create lists for date and profit/loss
date = []
month_count = 0
# pl_total = 0
current_pl = 0
# last_pl = 0
current_pl = []
monthly_pl_change = []

# open csv
with open(dataset, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # skip over header
    csv_header = next(csvreader)

    # loop through rows to gather month to month data
    for row in csvreader:

        # gather date and p&l lists
        date.append(row[0])
        current_pl.append(int(row[1]))

        # count months    
        month_count = month_count + 1

        # calculate monthly pl change
        #current_pl = int(row[1])
        #last_pl = int(row - 1, [1])
        #monthly_pl_change.append(current_pl - last_pl)

        # find month to month greatest increase (p&l, date) 
        # and greatest decrease (p&l, date)
        # increase_pl = max(monthly_pl_change)
        # decrease_pl = min(monthly_pl_change)
        # increase_index = monthly_pl_change.index(increase_pl)
        # decrease_index = monthly_pl_change.index(decrease_pl)
        # increase_month = date(increase_index)
        # decrease_month = date(decrease_index)


    print(month_count)

    # make calculations for total revenue and average of changes
    revenue_total = sum(current_pl)
    print(revenue_total)
    # average_change = sum(monthly_pl_change) / (month_count - 1)





    

    # loop through proft & loss list
    #for i in profit_loss:
        #pl_total = pl_total + int(i)

    #print(pl_total)
    
    # print analysis to terminal and text file