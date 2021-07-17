#!/usr/bin/env python
# coding: utf-8

# In[21]:


#PyBank

#Dependencies
import csv
import os

#Files to load and output
files_to_load = os.path.join("budget_data.csv")
files_to_output = os.path.join("budget_analysis.txt")

# Track various financial parameters
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999999]
total_net = 0

#Read the csv and convert it into a list dictionaries
with open(files_to_load) as financial_data:
    reader = csv.reader(financial_data)
    
    #Read the header row
    header = next(reader)
    #print(header)
    
    #Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    #print(first_row)
    total_months = total_months + 1
    
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])
    # print(total_net)
    # print(prev_net)
    
    print("Loop Starts Here")
    #loop your data
    for row in reader:
        
        #track the total
        total_months = total_months + 1
        total_net = total_net + int(row[1])
        #print(total_net)
        
        #Track the new change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]
        #print(net_change_list)
        #print(month_of_change)
        
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
            
    #Calculate the Average Net Change
    net_monthly_avg = sum(net_change_list) / len(net_change_list)
    
    output = (
        f"\nFinancial Analysis\n"
        f"======================\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_net}\n"
        f"Average Change: ${net_monthly_avg:.2f}\n"
        f"Greatest Increase In Profits {greatest_increase[0]}, (${greatest_increase[1]})\n"
        f"Greatest Decrease In Profits {greatest_decrease[0]}, (${greatest_decrease[1]})\n"
    )
    
    print(output)
    
    with open(files_to_output, "w") as txt_file:
        txt_file.write(output)
        


# In[ ]:




