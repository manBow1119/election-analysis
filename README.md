# Election Enalysis

## Project Overview
An analysis of raw popular vote data for a local congressional election in Colorado. 
Total votes were calculated, as were the total number of votes and percentage of votes for each candidate who received votes. The winner was determined by these calculated percentages.

## Technologies/Resources
- Data Source: election_results.csv
- Software: Python 3.10, Visual Studio Code 1.61

## Summary
### The analysis of the election shows that:
- There were 369,711 total votes cast in the election
- Denver County was the largest reporting county with 82.8% of total votes cast
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
### The candidate results were
  - Charles Casper Stockham received 23.0% of the vote with 85,213 votes.
  - Diana DeGette received 73.8% of the vote with 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote with 11,606 votes.
  
### The winner of the election was:
  - Diana DeGette received 73.8% of the vote with 272,892 votes.
  

   
## Extended Analysis
The initial election analysis algorithm was modified to include metrics on county data, demonstrating its flexibility and ability to be reused for other election analyses.
  
##  Summary
The script used to analyze this data can be generalized to practically any other election. With a simple modification of the data file name, voting data from other congressional elections can be analyzed. The script's flexibility also permits analysis of all the state voter and county data for full state elections like senatorial elections. The script can also be modified to further analyze candidate performance in each county by simply totalling candidate votes and finding the proportion of total county votes. Finally, the algorithm can be further modified to additionally include analysis of state data for larger elections on the scale of a presidential race.
