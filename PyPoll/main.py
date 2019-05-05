# import modules
import os
import csv

# define path
path_election_data = os.path.join('..','Resources','election_data.csv')

# initialize variables
candidate_votes = {}  # key: cand name, val: vote count
total_votes = 0
candidate_list = []

# read the csv
with open(path_election_data,'r') as file_election_data:
    reader_csv = csv.reader(file_election_data, delimiter=',')
    skip_header = next(reader_csv)

    # Loop through data
    for row in reader_csv:
        total_votes = total_votes + 1
        #find name of candidate
        candidate_name = row[2]
        # add name to list if not seen before
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)

        # put count in correct entry
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 1
        else: # seen this candidate alreday
            candidate_votes[candidate_name] += 1

CR = '\n'  #named '\n' with variable name

# open output file
fout_name = 'votes_results.txt'
fout = open(fout_name, 'w')

s = 'Election Results'
print(s); fout.write(s + CR)
s = '-'*20
print(s); fout.write(s + CR)

#The total number of votes cast
s = f"Total Votes: {total_votes}"
print(s); fout.write(s + CR)
s = '-'*20
print(s); fout.write(s + CR)

# results
winner = None
for cand, count in sorted(candidate_votes.items(), key=lambda t: t[1], reverse=True):
    if winner == None:
        winner = cand
    pct = (count / total_votes)*100
    s = f"{cand:10}: {pct:.3f}% ({count})"
    print(s); fout.write(s + CR)
s = '-'*20
print(s); fout.write(s + CR)
s = f"Winner: {winner}"
print(s); fout.write(s + CR)
s = '-'*20
print(s); fout.write(s + CR)
fout.close()


