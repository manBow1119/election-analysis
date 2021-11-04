#The data we need to retrieve 
#1. The total number of votes cast
#2. A complete list of candidateswho received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

#Add dependencies
import csv
import os

#Assign variable for the file to load and path
file_to_load = os.path.join("Resources","election_results.csv")
#Assign variable for file to write to
file_to_save = os.path.join('Analysis', 'elections_analysis.txt')

#initialize accumulator variable
total_votes = 0

#candidates list
candidate_options = []

#candidates: votes hash
candidate_votes = {}

#winner details
winning_candidate = ""
winning_count = 0 
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #skip headers 
    headers = next(file_reader)
    
    #Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        #check list of candidates and add new names
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #create key for hash table and starting vote count at 0
            candidate_votes[candidate_name] = 0
        #track total votes for each candidate
        candidate_votes[candidate_name] += 1

#Saving results to text file
#Using with statement to open file as text
with open(file_to_save, "w") as txt_file:
    #write some data to the file
    election_results = (
        f"\nElection Results\n"
        f"----------------------\n"
        f"Total Votes: {total_votes: ,}\n"
        f"----------------------\n"
    )
    print(election_results, end="")
    #save final vote count to text file
    txt_file.write(election_results)
            
    #Determine percentage of total votes for each candidate
    for candidate_name in candidate_votes:
        #get votes for each candidate
        votes = candidate_votes[candidate_name]
        #calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        #print each candidates stats
        candidate_results = (f"{candidate_name} : {vote_percentage:.1f}% ({votes: ,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
    

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #update winning details
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate =  candidate_name
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count: ,}\n"
        f"Winning Percentage: {winning_percentage:.1f}\n"
        f"--------------------------\n")
    txt_file.write(winning_candidate_summary)






