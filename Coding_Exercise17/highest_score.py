# Coding Exercise No.17
# Highest Score

user_input = input("Enter the scores of students, separated by spaces: ")
score_strings = user_input.split()

# Convert each item in the list from string to integer
# We'll use a loop to do this manually
student_scores = []
for s in score_strings:
    student_scores.append(int(s))  # convert and add to the list

# Assume the first score is the highest to start comparison
highest_score = student_scores[0]

# Loop through each score to find the highest
for score in student_scores:
    if score > highest_score:
        highest_score = score  # Update highest_score if a larger one is found

# After checking all, print the highest score
print("The highest score in the class is:", highest_score)
