# Election Analysis

## Overview of Election Audit
### The purpose of this election audit analysis is to pull data from the results csv using python scripts for the election commission as requested. In this particular analysis the three main pieces of data that are requested are: The voter turnout for each county, The percentage of votes from each county out of the total count, and The county with the highest turnout. With this information the election commission can paint themselves a better picture of the election results.

## Election Audit Results
* ### Total Votes Cast: 369,711

* ### In Jefferson County there were 38,855 votes cast making up 10.5% of the total votes cast.

* ### In Denver County there were 306,055 votes cast making up 82.8% of the total votes cast.

* ### In Arapahoe County there were 24,801 votes cast making up 6.7% of the total votes cast.

* ### Denver County had the largest number of votes cast.

* ### Candidate Diana DeGette received 272,892 votes making up 73.8% of the total votes.

* ### Candidate Charles Casper Stockham received 85,213 votes making up 23% of the total votes.

* ### Candidate Raymon Anthony Doane received 11,606 votes making up 3.18% of the total votes.

* ### The winner of the election is Diana DeGette who received 272,892 votes making up 73.8% of the votes.

## Election Audit Summary
### In short, this python script is capable of handling the analysis for not only this election, but with few modifications, any election that might need this information found. If you wanted to look at similar data but for the whole of a country, it would be as simple as changing what data gets read from the csv file and changing what the summary text file has printed to it. You could even look at a set of states with the same level of detail for each state by adding another csv file to the resources and setting up another with open() statement to read the data from the new state and pull what is needed from the file.
