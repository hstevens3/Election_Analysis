# 1. Open the file
# 2. Get each candidate name
# 3. Count the votes for each candidate
# 4. Count the total votes
# 5. Calculate the percentage for each candidate.
# 6. Winner of the election.

import csv
import os


# Assign a variable for the file to load and the path (direct).
file_to_load = 'resources/election_results.csv'

# Create a filename variable for the output file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#indirect path
# file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
# election_data = open(file_to_load, 'r')

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data) 

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

# Close the file. only need if use open instead of with
# election_data.close()


# Using the open() function with the "w" mode we will write data to the file.
# outfile=open(file_to_save, "w")

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

# Write three counties to the file.
#txt_file.write("nArapahoe\nDenver\nJefferson")