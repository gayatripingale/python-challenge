import os
import csv

poll_dict = {}
total_votes = 0

csv_file = os.path.join(".","election_data_1.csv")
with open(csv_file,newline="") as election_data:
    reader = csv.reader(election_data,delimiter=",")
    next(reader) # This is to skip the firsr i.e header row
    
    # To count the total number of votes, count voter_id column
    # voters=[] #intialize the list voter_id[] before appending it
    for row in reader:
        # voters.append(row[0])
        poll_dict[row[2]] = (poll_dict).get(row[2],0) + 1

for element in poll_dict:
    total_votes += poll_dict[element]

print(" Election Results:")
print("______________________")
print("Total votes: " + str(total_votes))
print("______________________")

for element in poll_dict:
    percent_vote = (poll_dict[element]/total_votes)*100
    print(element, ": ", percent_vote, "% (", str(poll_dict[element]), ")")

print("______________________")


# To get the the winner, we need to find the "Key" corrosponding to the max votes
# to find max of values..her max of votes
max_votes = 0
max_votes = max(poll_dict.values())

# Now finding the winner who got max votes.
# There might be more than one person who got sme max votes
# So, we need to create the list of winners
winner=[k for k,v in poll_dict.items() if v == max_votes]

print("Winner is: ",winner)
print("______________________")