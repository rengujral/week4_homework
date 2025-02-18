slurping_pelican = open("pelican.txt").read()
#I've used the open function and the read method in order to open and read the file as requested
print(type(slurping_pelican))
#I've printed type of contents that will be return
print(slurping_pelican)
# Q4: what type of data type is this
#The data type is a string
read_into_list = open("pelican.txt").readlines()
print(len(read_into_list))
#I've used the readiness method to put the content of the file in a list
for content in read_into_list:
    print(content[:-1])
#I've iterated through the content of the file and have sliced it to remove the empty new lines.
