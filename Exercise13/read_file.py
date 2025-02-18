# use the open function and the read method in order to open and read the file
slurping_pelican = open("pelican.txt").read()

# Print type of contents
print(type(slurping_pelican))

print("\nContent of pelican.txt:")
print(slurping_pelican)

# use readlines method to put the content of the file in a list
read_into_list = open("pelican.txt").readlines()
print("\nNumber of items within pelican.txt:", len(read_into_list))

# loop iterates through the content of the file and slice it to remove the empty new lines.
print("\nContent of pelican.txt:")
for content in read_into_list:
    print(content[:-1])

# # alt method
# print("\nContent of pelican.txt:")
# for line in slurping_pelican:
#     print(line.strip())