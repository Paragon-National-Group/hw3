# Paragon National Group Spring 2022
# Computer Science / Data Science Track
# HW 3

# Assigned: April 14, 2022
# Due: April 19, 2022 11:59pm

# This is the third programming assignment of the computer science track.
# For each function, a skeleton is provided, where your job is to fill the *TODO* out.
# The questions will cover the topics learned in the third lecture, which entailed
# file directories, pip / importing packages, dictionaries, sets, list functions 
# (append, pop, reverse, filter, etc), iterating over a list, sorting a list, and 
# breaking while/for loops.

# This function takes two numbers and returns the first number to the power of the
# second number if they are relatively prime and will return only the first number
# if they are not relatively prime. You must use the math package for question. 
# Think about what function in the package will help you determine that these two
# numbers are relatively prime.
# Ex) prime_pow(2, 3) -> 8
#     prime_pow(2, 4) -> 2
#     prime_pow(7, 2) -> 49
def prime_pow(n1, n2):
    #TODO
    return

# This function takes a list of test scores as an argument and returns a dictionary
# of the lowest score, highest score, and average in that order. The professor
# decides to apply a curve where all students get 10 more points. Use the map
# function to implement this. Also, using the sort function for the list is highly
# recommended.
# Ex) test_scores([70, 74, 77, 78, 78, 79, 80]) -> {"Lowest": 80.0, "Highest": 90.0, "Average": 86.57}
#     test_scores([78, 68, 65, 75, 73, 99, 92]) -> {"Lowest": 75.0, "Highest": 109.0, "Average": 88.57}
#     test_scores([54]) -> {"Lowest": 64.0, "Highest": 64.0, "Average": 64.0}
def test_scores(list):
    #TODO
    return

# This function takes a filename as an argument and writes the list passed into
# the test_scores() function and the result for it on the next line.
# Ex) write_scores_file("test_scores_results.txt")
#       -> [70, 74, 77, 78, 78, 79, 80]
#          Lowest: 80.0, Highest: 90.0, Average: 86.57
#     write_scores_file("test_scores_results.txt")
#       -> [78, 68, 65, 75, 73, 99, 92]
#          Lowest: 75.0, Highest: 109.0, Average: 88.57
#     write_scores_file("test_scores_results.txt")
#       -> [54]
#          Lowest: 64.0, Highest: 64.0, Average: 64.00
def write_scores_file(filename):
    #TODO
    return