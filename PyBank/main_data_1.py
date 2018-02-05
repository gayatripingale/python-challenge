import os
import csv

# File we need to load is budget_data_1.csv
# Assign a var to it---> file_to_load = budget_data_1.csv
#csv_file = budget_data_1.csv

# read the csv and convert it into the list of dictionaries

csv_file = os.path.join(".","budget_data_1.csv")
with open(csv_file, newline="") as revenue_data: #revdata is revenue data
    reader = csv.reader(revenue_data,delimiter=",")
    # using "next" to skip the forst title/header row in the data set
    next(reader)
    revenue = []
    date = []
    rev_change = []

    # Here we are reading the respective values form the reader file 
    # i.e reading dates to count the number of months form row[0] and 
    # the revenue form row[1] and then
    # adding it to "date" and "revenue" lists, using .append()
    for row in reader:
        date.append(row[0])
        revenue.append(float(row[1]))
    # calculating "total numeber of months" i.e var date[] using .append() & len()and 
    # total revenue i.e revenue using .sum()
    print("Financial Analysis")
    print("-------------------------------")
    print(" The total months: ", len(date))
    print("Total Revenue: ",sum(revenue))

# using loop to calculate the following in Green colour
    for i in range(1,len(revenue)):
        #The average change in revenue between months over the entire period 
        rev_change.append(revenue[i] - revenue[i-1])
        avg_rev_change = sum(rev_change)/len(rev_change)

        #The greatest increase in revenue (date and amount) over the entire period
        grt_incr_rev_change = max(rev_change)
        grt_incr_rev_date = str(date[rev_change.index(max(rev_change))])
    

        #The greatest decrease in revenue (date and amount) over the entire period
        grt_decr_rev_change = min(rev_change)
        grt_decr_rev_change_date = str(date[rev_change.index(min(rev_change))])
       
    print("The avergae change: $ ",str(avg_rev_change))
    print("The greatest increase in revenue is during ",grt_incr_rev_date, "( $ ",str(grt_incr_rev_change),")")
    print("The greastest deccrease in revenue is during ", grt_decr_rev_change_date,"($",str(grt_decr_rev_change),")")



