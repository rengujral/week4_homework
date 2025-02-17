# QUESTION 3
# Import the random module so we can use its functions
import random

# Pick 6 random numbers between 1 and 50, without repeating any
# random.sample() does this and puts them in a list
numbers = random.sample(range(1, 51), 6)

# Print the list of 6 numbers
print("Your lottery numbers are:", numbers)