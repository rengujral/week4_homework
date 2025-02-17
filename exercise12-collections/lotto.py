from random import randrange

# help("random")
#used the help function to find out which function to use. I must first import random. I would also like to use randrange to generate a
#new number from the range 1 to 50

count = 0
#I use the variable count and assign it to 0 as a counter.
new_list = []
#I use new_list as a variable that store an empty list, so I have a place to store the 6 numbers that is trying to be generated.
while count < 6:
    num = randrange(1, 51)
#I assign the random number that will be generated from the randrange function of arguments 1 and 51 to a variable num
    new_list.append(num)
#I then add the number to the empty list, new_list is storing.
    count += 1
#I increment the count so the while loop eventually meets the condition of 6 and breaks.
print(new_list)
#I then print the list.


#Experimenting - How I would convert the list to a dictionary.
new_dict = {}
for num in new_list:
    index_num = new_list.index(num)
    new_dict[index_num + 1] = num
print(new_dict)


