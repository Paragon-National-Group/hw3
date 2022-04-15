# hw3
This is the third programming assignment of the computer science track for Paragon National Group. The questions will cover the topics learned in the third lecture, which entailed file directories, pip / importing packages, dictionaries, sets, list functions (append, pop, reverse, filter, etc), iterating over a list, sorting a list, and breaking while/for loops.

Carefully read over the specifications of each function that is given in the header description.

Due Date: Apr 19th 2022 11:59pm

https://classroom.github.com/a/o8fuqp1F is the link for this assignment.

# Tasks
A skeleton is provided for each task, and your job is to fill it out. The parts where you need to fill it out is marked as "TODO".

**prime_pow**

This function takes two numbers and returns the first number to the power of the second number if they are relatively prime and will return only the first number if they are not relatively prime. You must use the math package for question. Think about what function in the package will help you determine that these two numbers are relatively prime.

**test_scores**

This function takes a list of test scores as an argument and returns a dictionary of the lowest score, highest score, and average in that order. The professor decides to apply a curve where all students get 10 more points. Use the map function to implement this. Also, using the sort function for the list is highly recommended.

**write_scores_file**

This function takes a filename as an argument and writes the list passed into the test_scores() function and the result for it on the next line in the provided file "test_scores_result.txt".  

The text file should look like this if you used ```test_scores([70, 74, 77, 78, 78, 79, 80])```:
```
[70, 74, 77, 78, 78, 79, 80]
Lowest: 80.0, Highest: 90.0, Average: 86.57
```

# Submitting the Code
To submit your code, simply run the following steps:
```
git add PNG-HW3.py
```
```
git commit -m 'Submitted hw3'
```
```
git push
```
After committing the latest changes to your Github repository, submit your code through Gradescope.
