import os
import csv

#initialising the variables
total_votes_casted = 0
candidates_list = []
vote_count = []
candidate_vote_percentage = []

#locating the csvfile to collect the data
csvpath = os.path.join(".", "Resources", "election_data.csv")

#opening the csv file in read mode
with open(csvpath, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

    #looping through rows
    for row in csv_reader:
        #calculating the total votes
        total_votes_casted += 1
    #Finding the candidate names using conditional statement and adding them to the candidates_list
    #counting the votes for each candidate using index numbers
        candidate = str(row[2])
        if candidate not in candidates_list:
            candidates_list.append(candidate)
            index = candidates_list.index(candidate)
            vote_count.append(1)
        else:
            index = candidates_list.index(candidate)
            vote_count[index] += 1

    #finding the winner using vote count and index
        winner = max(vote_count)
        index = vote_count.index(winner)
        winner_candidate = candidates_list[index]
                
    #printing the output
    print("Election Results")
    print("------------------------")
    print(f"Total Votes:{total_votes_casted}")
    print("------------------------")
    
    #calculating the vote percentage and printing the percentage using enumerate function to iterate using the index and candidates
    
    for index, candidate in enumerate(candidates_list):
    
        vote_percentage = (vote_count[index]/total_votes_casted)*100
        candidate_vote_percentage.append(vote_percentage)

        print(f"{candidate}: {vote_percentage:.3f}%  ({vote_count[index]} votes)")

    #printing the winner    
    print(f"Winner: {winner_candidate}")

#creating a new textfile
output_path = os.path.join(".", "Analysis", "output.txt")

#opening the textfile in write mode to print the result
with open(output_path, "w") as textfile:
    row1 = textfile.write("Election Results\n")
    row2 = textfile.write("------------------\n")
    row3 = textfile.write(f"Total Votes:{total_votes_casted}\n")
    row4 = textfile.write("------------------\n")
    #using for loop with enumerate function again to write the vote_count for each candidate
    for index, candidate in enumerate(candidates_list):
        row5 = textfile.write(f"{candidate}: {vote_percentage:.3f}%  ({vote_count[index]} votes)\n")
    row6 = textfile.write(" \n")
    row7 = textfile.write(f"Winner: {winner_candidate}\n")
    



        
        
    
    
    
  
