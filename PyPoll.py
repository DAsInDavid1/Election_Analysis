# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Data Bootcamp", "Module 3 PyPoll with Python", "Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("Data Bootcamp", "Module 3 PyPoll with Python", "analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)


# Read and print the header Row
    headers = next(file_reader)
    print(headers)