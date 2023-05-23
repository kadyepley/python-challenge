# Import the os and csv
import os
import csv

# Open and read the csv file accounting for the header
datafile=r'C:\Users\kadye\Documents\GitHub\python-challenge\PyBank\Resources\budget_data.csv'
with open(datafile) as file:
    reader=csv.reader(file)
    # Skipping the first line
    header=next(reader)
    #print(header)
    
    # Set the variables
    profit_loss = []
    months = []
    change = []

    # Establish where to start reading for each variable after the header
    for rows in reader:
        profit_loss.append(int(rows[1]))
        months.append(rows[0])
    
    # Add on the change from one row to the next (i being the row that is read)
    for i in range(1, len(profit_loss)):
        change.append((int(profit_loss[i]) - int(profit_loss[i-1])))

    # Calculations for the average profit and loss and the average change in profit and loss
    avg_change = sum(change) / len(change)
    avg_profit_loss = round(avg_change, 2)
    #print (avg_profit_loss)

    # Calculate the total number of months in the data set
    total_months = len(months)
    #print (total_months)

    # Find the greatest increase in profit
    greatest_inc = max(change)
    #print (greatest_inc)

    # Find the greatest decrease in profit
    greatest_dec = min(change)
    #print (greatest_dec)

    # Print Results
    print ("Financial Analysis")

    print("----------------------------")


    print ("Total Months:" + str(total_months))

    print("Total:" + "$" + str(sum(profit_loss)))

    print ("Average Change:" + "$" + str(avg_profit_loss))

    print("Greatest Increase in Profits: " + str(months[change.index(max(change))+1]) + " " + "($" + str(greatest_inc) + ")")

    print("Greatest Decrease in Profits: " + str(months[change.index(min(change))+1]) + " " + "($" + str(greatest_dec) + ")")

