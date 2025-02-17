# since there is no comma present, this is treated as a string
# len() counts and returns the number of characters in the string which is 5
tup = 'Hello'
print(len(tup))

# since there is a comma present, this is now treated as a tuple
# len () now counts and returns the number of elements in the tuple which is 1
tup = 'Hello',
print(len(tup))