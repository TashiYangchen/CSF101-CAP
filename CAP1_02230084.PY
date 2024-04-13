##########################################################
#Tashi Yangchen
#1 Electrical
# 02230084
##########################################################
# REFERENCES
#https://github.com/golergka/advent-of-code-2022-with-chat-gpt/blob/master/day_2/README.md
################################
#SOLUTION
# Your Solution Score:49524
# 4
###############################
def read_input(enter_filename):
# The function read_input(enter_filename) reads a filename.
    total = []  # Initialize an empty list to store the scores
    with open(enter_filename, 'r') as f:
# It opens the file specified by enter_filename in read mode ('r') and uses the with statement to ensure 
# the file is properly closed after reading.
        for line in f: # Splitting each line into shape and score
            selected_shape, result_score = line.strip().split() 
            # A line indicates one line retrieved from the file, strip() deletes any beginning or trailing 
            # whitespace characters (such as spaces, tabs, or newlines) from the line, 
            # Split() divides the line into a list of strings, with whitespace as the default delimiter.
            total.append((selected_shape, result_score))
            #The code reads each line from the file, extracts the selected shape and result score, 
            #creates a single match tuple, and adds it to the total list.
    return total
# After reading all lines in the file, it returns the total list containing tuples of (selected_shape, result_score).
def calculate_score(matches_played):
#This function calculate_score takes a list of matches played (matches_played) as input.
    # A = Rock, B = Paper, C = Scissor
    selected_shape_values = {'A': 1, 'B': 2, 'C': 3}
    # X = lose, Y = Draw, Z = Win
    result_values = {'X': 0, 'Y': 3, 'Z': 6}
    score = 0  # Initialize a variable 'score' to keep track of the overall score, beginning at 0.
    for match in matches_played:
        selected_shape, result_score = match 
        #unpacks the tuple for each match into selected_shape and result_score fields.
        shape_value = selected_shape_values[selected_shape]
        result_value = result_values[result_score]
    # The function retrieves the numeric value of the selected shape and the score value based on
    # the result code from the corresponding dictionaries.
        if result_score == 'Y':
        #For a draw (Y), it adds the shape and outcome values to the overall score.
            score += shape_value + result_value
        elif result_score == 'Z':
        #For a win (Z), it adds a predefined value based on the form chosen.
            if shape_value == 1:
                score += 8
            elif shape_value == 2:
                score += 9
            elif shape_value == 3:
                score += 7       
        elif result_score == 'X':
        #For a loss (X), it adds a predefined value based on the shape chosen.
            if shape_value == 1:
                score += 3
            
            elif shape_value == 2:
                score += 1
                 
            elif shape_value == 3:
                score += 2
#Hence, based on the outcome score (Y, Z, or X), it calculates the match score and changes the overall score appropriately.                 
    print(f"The total_score is: {score}")
# This code reads data from a file containing match outcomes, calculates the scores using the criteria 
# specified, and outputs the total_score.
enter_filename = "CSF101-CAP/input_4_cap1.txt" # Bringing the input
calculate_score(read_input(enter_filename))
#Concise way to read match data from a file, calculate the total score based on that data, and display the result.