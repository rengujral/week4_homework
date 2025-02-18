# import the random module to generate randomised numbers
import random

# generate 6 unique numbers between 1-50
# a range of 1, 51 allows for a generation of number between 1-50, as the upper limit is exclusive
# .sample select unique values in the iterable (no duplication)
# 6 values are generated as k is 6
lotto_generator = random.sample(range(1, 51), 6)

###TO DO
### an example using random.randint
###Create an empty set at the start of the code
print(type)

# the sorted function allows for better readability and sorts them in ascending order
print("The lottery numbers are:", sorted(lotto_generator))