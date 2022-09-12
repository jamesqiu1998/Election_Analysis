# The data we need to retrieve
# 1. The total numbers of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of election based on popular vote.

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize the vote counter
total_vote= 0

# Candidate options
candidate_options = []

# declare empty dictionary
candidate_votes= {}

#Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage  = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
   
    # Print each row in the CSV file
    for row in file_reader:

        # Add to the total vote count
        total_vote +=1

        # Print the candidates name from each row
        candidate_name = row[2]
        if candidate_name not in candidate_options:
        # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

            # Add each vote to the candidate_votes dictionary after scnaner through the excel sheet
        candidate_votes[candidate_name] +=1


# Savr the result to our text file
with open(file_to_save,"w") as txt_file:
    election_result = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_vote:,}\n"
        f"-------------------------\n"
    )

    print (election_result, end = "")
  

    txt_file.write(election_result)

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_vote) * 100
        candidate_result = (
            f"{candidate_name} : {vote_percentage:.1f} % ({votes:,})\n")
        print(candidate_result)
        txt_file.write(candidate_result)

        if (votes > winning_count) and (vote_percentage > winning_percentage) :
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate=candidate_name

    winning_candidate_summary = (
        f"-----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------\n"
    )    




    print(winning_candidate_summary)

# Save the winning candidate's result to the text file
    txt_file.write(winning_candidate_summary)
