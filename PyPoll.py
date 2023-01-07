# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote Counter
total_votes = 0

# make a list of canidtates 
canidate_options = []

# make a dictionary of canidates to link them to thier votes
canidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)


# Read the header Row
    headers = next(file_reader)
   
# Print each row in the CSV file
    for row in file_reader:

        # add to the total vote count
        total_votes += 1

        # get the canidate name for each row
        canidate_name = row[2]

        # if the canidate does not match existing canitades...
        if canidate_name not in canidate_options:

            #add the canidate name to the canidate lsit
            canidate_options.append(canidate_name)

            # setting each canidates votes to 0 in the key
            canidate_votes[canidate_name] = 0

        # adding a vote to the canidates count.
        canidate_votes[canidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in canidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = canidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    #print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
     # 2. If true then set winning_count = votes and winning_percent =
     # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
     # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
        
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)