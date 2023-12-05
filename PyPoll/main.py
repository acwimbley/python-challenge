import os
import csv

# Read the CSV file
file_path = "PyPoll\Resources\election_data.csv"

# Initialize variables
total_votes = 0
candidates_votes = {}

with open(file_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Skipping header row 

    # Looping through rows in the CSV
    for row in csv_reader:
        candidate = row[2]  
        total_votes += 1

        # Update candidate votes
        if candidate in candidates_votes:
            candidates_votes[candidate] += 1
        else:
            candidates_votes[candidate] = 1

# Calculating total votes and percentage by candidate
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print("Candidates who received votes:")
for candidate, votes in candidates_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {votes} votes ({percentage:.2f}%)")
print("-------------------------")

# Identify the candidate with the most votes
winner = max(candidates_votes, key=candidates_votes.get)
print(f"Winner: {winner}")
print("-------------------------")

# Exporting the results to a text file
output_file_path = "election_results.txt"
with open(output_file_path, 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-----------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    output_file.write("Candidates who received votes:")
    for candidate, votes in candidates_votes.items():
     percentage = (votes / total_votes) * 100
    output_file.write(f"{candidate}: {votes} votes ({percentage:.2f}%)")
    output_file.write(f"{candidate}: {votes} votes ({percentage:.2f}%)")
    

print(f"Results exported to {output_file_path}")