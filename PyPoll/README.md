# Import the os and csv
import os
import csv

# Set the output - I spent a ton of time trying to get the results to show via print () the normal way and 
# was not sure if it was easier to have the outcomes stored somewhere else then re-referenced. 

output_file = r'C:\Users\kadye\Documents\GitHub\python-challenge\PyPoll\analysis\electionoutcome.txt'

# This is most similar to our graduation rates activity

# Open and read the csv file accounting for the header
datafile=r'C:\Users\kadye\Documents\GitHub\python-challenge\PyPoll\Resources\election_data.csv'
with open(datafile) as file:
    # Opened as a dictionary instead of the normal reader
    reader=csv.DictReader(file) 
    # Skipping the first line
    header=next(reader)
    #print(header)
    
    # Set the variables
    total_votes = 0 
    candidates = []
    candidate_votes = {} # dictionary to store for each candidate
    winner = "" # name of the winner
    winning_votes = 0
    
    for row in reader:
        total_votes = total_votes + 1 # adding one as we read down the data
        candidate_name = row["Candidate"] # pulling the name on the ballot of each row

        if candidate_name not in candidates: # if the name is not already in the array
            candidates.append(candidate_name) # then add to the list (like adding the profit/loss change to PyBank)
            candidate_votes[candidate_name] = 0 # add that vote to the votes for that candidate
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# This part took a lot of researching, but I think this is the best way to display the information after all the sorting above
with open(output_file,"w") as txt_file:
    
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    )
    
    print(election_results)

    txt_file.write(election_results) # saves this to a text file to retrived and fill the formatted block above

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate) # pull the amount of votes
        voter_percentage = float(votes) / float(total_votes) * 100 # calculate the percent of the total votes for the candidate

        if (votes > winning_votes): # if the tally is more than current winning tally
            winning_votes = votes # set the votes equal to the winner number
            winner = candidate # make that candidate the winner

            voter_output = f"{candidate}: {voter_percentage:.3f}% ({candidate_votes})\n" # print each candidate's voter percentage and votes
            print(voter_output)

            #Save to the txt_file
            txt_file.write(voter_output)

        # Print the election outcome
        winner_outcome = (
            f"-------------------------\n"
            f"Winner: {winner}\n"
            f"-------------------------\n"
         )
        print(winner_outcome)

        # Save again
        txt_file.write(winner_outcome)
