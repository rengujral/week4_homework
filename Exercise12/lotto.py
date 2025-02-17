# import the random module to generate randomised numbers
import random

# generate 6 unique numbers between 1-50
# a range of 1, 51 allows for a generation of number between 1-50, as the upper limit is exclusive
#
lotto_generator = random.sample(range(1, 51), 6)

# the sorted function allows for better readibility and sorts them in ascending order
print("The lottery numbers are:", sorted(lotto_generator))