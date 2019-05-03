#PyPoll
#Imort necessary modules
import os
import csv

# Get election_data.csv
csvpathPyPoll = os.path.join("..", "Resources", "election_data.csv")

# Store data in lists
votes []
candidates []

# Open & Read csv file
with open(csvpathPyRoll, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
     # To skip header line
    header = next(csvreader)

#Analyze the votes and calculate each of the following:

#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.
