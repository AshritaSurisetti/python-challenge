import os
import csv

#Initialising the variables
Total_months = 0 
net_total_amount = 0
profit_loss = 0
previous_profit_loss = 0

#creating lists to store the data
change_list = []
Dates = []

csvpath = os.path.join(".", "Resources", "budget_data.csv")

#To read the csv file with header
with open(csvpath, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter =",")
    csv_header = next(csv_reader)

    #looping through the rows
    for row in csv_reader:
        date = (row[0])
        profit_loss = int(row[1])
    
        #To calculate the total number of months
        Total_months += 1

        #To calculate the net amount
        net_total_amount += int(profit_loss)

        #conditional statement to not to consider 0 in previous_profit_loss variable
        if previous_profit_loss != 0:

            #using absolute function to make the number positive as we are already subtracting previous value
            change = profit_loss - previous_profit_loss

            #adding change values to the list 
            change_list.append(change)
            Dates.append(date)
            
        #assigning a value for next iteration
        previous_profit_loss = profit_loss

    #Calculating average change
    average_changes = sum(change_list)/len(change_list)

    #calculating the greatest increase and decrease values
    Greatest_increase_profits = max(change_list)
    Greatest_decrease_profits = min(change_list)
    
    #finding the dates of the greatest values using index values
    Greatest_increase_date = Dates[change_list.index(Greatest_increase_profits)]
    Greatest_decrease_date = Dates[change_list.index(Greatest_decrease_profits)]

#printing analysis to the terminal
print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {Total_months}")
print(f"Total: ${net_total_amount}")
print(f"Average Change: ${average_changes: .2f}")
print(f"Greatest Increase in profits: {Greatest_increase_date} (${Greatest_increase_profits})")
print(f"Greatest Decrease in Profits: {Greatest_decrease_date} (${Greatest_decrease_profits})")

#creating a new textfile
output_path = os.path.join(".", "Analysis", "output.txt")

#opening the textfile in write mode to print the analysis
with open(output_path, "w") as textfile:
    row1 = textfile.write("Financial Analysis\n")
    row2 = textfile.write("---------------------\n")
    row3 = textfile.write(f"Total Months: {Total_months}\n")
    row4 = textfile.write(f"Total: ${net_total_amount}\n")
    row5 = textfile.write(f"Average Change: ${average_changes: .2f}\n")
    row6 = textfile.write(f"Greatest Increase in profits: {Greatest_increase_date} (${Greatest_increase_profits})\n")
    row7 = textfile.write(f"Greatest Decrease in Profits: {Greatest_decrease_date} (${Greatest_decrease_profits})\n")