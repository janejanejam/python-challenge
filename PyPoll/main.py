# import modules
import csv
import pathlib
from collections import Counter

# setup file path to csv
dataset = pathlib.Path("./Resources/election_data.csv")

# open csv file and setup reader
with open(dataset, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # skip over header
    csv_header = next(csvreader)

    # setup variables and lists
    vote_total = 0
    candidates = []
    unique_candidates = []
    vote_count = []
    vote_percentage = []


    # loop rows in data
    for row in csvreader:

        # count number of votes
        vote_total = vote_total + 1

        # unique list of candidates
        candidates.append(row[2])

# find list of candidates, number of votes per candidate, percentage of votes
for name in set(candidates):
    unique_candidates.append(name)
    votes = candidates.count(name)
    vote_count.append(votes)
    percentage = (votes/vote_total)*100
    vote_percentage.append(percentage)

# zip lists and sort to get final analysis
zipped_list = sorted(zip(vote_count, unique_candidates, vote_percentage), reverse = True)

# find winner
winning_vote_count = max(vote_count)
winner = unique_candidates[vote_count.index(winning_vote_count)]


# print to terminal
print("Election Results")
print("------------------------")
print(f"Total Votes: {vote_total}")
print("------------------------")
for vote1, name1, percentage1 in zipped_list:
    print(f"{name1}: {percentage1:.2f}% ({vote1})")
print("------------------------")
print(f"Winner: {winner}")
print("------------------------")

# write to text file
output_path = pathlib.Path("./Analysis/PyPoll_Analysis.txt")

with open(output_path, "w") as text:
    text.write("Election Results\n")
    text.write("------------------------\n")
    text.write(f"Total Votes: {vote_total}\n")
    text.write("------------------------\n")
    for vote1, name1, percentage1 in sorted(zip(vote_count, \
        unique_candidates, vote_percentage), reverse = True):
        text.write(f"{name1}: {percentage1:.2f}% ({vote1})\n")
    text.write("------------------------\n")
    text.write(f"Winner: {winner}\n")
    text.write("------------------------\n")