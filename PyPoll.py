#What we need

import csv
import os

#Create a file that will be written on
file_to_save = os.path.join("analysis","election_analysis.txt")

#Assigning a variable to the results path
file_to_load = os.path.join("Resources","election_results.csv")


#Use with statment to open file

#Total Votes DEF
total_votes = 0

#New Candidate List
candidate_options = []

#Dictonary of votes
candidate_votes = {}

#Tracking Winner and Winning Margin
winning_candidate = ""

winning_count = 0

winning_percentage = 0

#Open results and read
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read header row
    headers = next(file_reader)
    
    #Print each row
    for row in file_reader:

        #Incrementally add votes
        total_votes += 1

        #Find candidate name
        candidate_name = row[2]

        #Add name to options
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1    

    #Find percentage of votes
    for candidate_name in candidate_votes:
    
        votes = candidate_votes[candidate_name]

        vote_percentage = float(votes)/float(total_votes) * 100


        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


        if (votes > winning_count) and (vote_percentage > winning_percentage):

            winning_count = votes

            winner_percent = vote_percentage
        
        winning_candidate = candidate_name

    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    
print(winning_candidate_summary)