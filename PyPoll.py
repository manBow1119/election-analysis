#The data we need to retrieve 
#1. The total number of votes cast
#2. A complete list of candidateswho received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

#election_spreadsheet = open("Resources/election_results.csv","r")
import csv
import os

#Assign variable for the file to load and path
file_to_load = os.path.join("Resources","election_results.csv")
#Assign variable for file to write to
file_to_save = os.path.join('Analysis', 'elections_analysis.txt')

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #skip headers and print to verify
    headers = next(file_reader)
    print(headers)
    
    #Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)



#Using with statement to open file as text
# with open(file_to_save, "w") as txt_file:
#     #write some data to the file
#     txt_file.write("Counties in the Election\n")
#     txt_file.write("------------------------\n")
#     txt_file.write("Arapahoe\n")
#     txt_file.write("Denver\n")
#     txt_file.write("Jefferson")


