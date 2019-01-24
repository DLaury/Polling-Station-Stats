#calling modules
import csv
import os
import sys

#initializing variables
numVotes = 0
candidates = {}
prev = 0

#opening file election_data.csv and reading it
electionData = os.path.join('PyPoll', 'Resources', 'election_data.csv')
with open(electionData, 'r', newline = "") as csvfile:
    readData = csv.reader(csvfile,delimiter = ',')
    
    #excluding header
    header = next(readData)

    #iterating over whole document
    for row in readData:
        
        #adding to numVotes and totChange for total values
        numVotes += 1
        
        #adding candidates as keys and initializing a list of values for that key
        if row[2] not in candidates:
            candidates[row[2]] = [0,""]

        #adding votes to the specific key's vote total
        candidates[row[2]][0] += 1

#formatting output
print(f"\nElection Results\n"
        f"---------------------------\n"
        f"Total Votes: {numVotes}\n"
        f"---------------------------")

#running through dictionary for anonymity
for names in candidates:

    #calculating percentage of votes and placing it in the key
    percentage = candidates[names][0] / numVotes * 100
    candidates[names][1] = format(percentage,'.3f')

    #calculating winner
    if candidates[names][0] > prev:
        prev = candidates[names][0]
        winner = names
    
    #outputting each nominee, their percentage of the vote, and total number of votes
    print(f"{names}: {candidates[names][1]}% ({candidates[names][0]})")

#outputting the winner
print(f"---------------------------\n"
        f"Winner: {winner}\n"
        f"---------------------------")

#formatting output for text file
txtOut = open(os.path.join('PyPoll', 'Output', 'election_results.txt'), 'w')
sys.stdout = txtOut
print(f"\nElection Results\n"
        f"---------------------------\n"
        f"Total Votes: {numVotes}\n"
        f"---------------------------")

#running through dictionary for anonymity
for names in candidates:
    
    #calculating percentage of votes and placing it in the key
    percentage = candidates[names][0] / numVotes * 100
    candidates[names][1] = format(percentage, '.3f')

    #calculating winner
    if candidates[names][0] > prev:
        prev = candidates[names][0]
        winner = names
    
    #outputting each nominee, their percentage of the vote, and total number of votes
    print(f"{names}: {candidates[names][1]}% ({candidates[names][0]})")

#outputting the winner
print(f"---------------------------\n"
        f"Winner: {winner}\n"
        f"---------------------------")

#closing the .txt file I have open
txtOut.close()