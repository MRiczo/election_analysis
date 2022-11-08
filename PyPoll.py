#What we need

import csv
import os

#Create a file that will be written on
file_to_save = os.path.join("analysis","election_analysis.txt")

#Assigning a variable to the results path
file_to_load = os.path.join("Resources","election_results.csv")


#Use with statment to open file

#Open results and read
with open(file_to_load) as election_data:

    #Analysis of election_data
    file_reader = csv.reader(election_data)

    #Read and Print header row
    headers = next(file_reader)
    print(headers)

    

with open(file_to_save,"w") as outfile:


    #Write on election_analysis.txt
    outfile.write("Counties in the Election\n-----------------------\nArapahoe\nDenver\nJefferson")

    #Total number of votes cast

    #A complete list of candidates who received votes

    #Total number of votes each candidate received

    #Percentage of votes each candidate won

    #The winner of the election based on popular vote
