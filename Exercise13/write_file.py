# the open function opens the specified .txt file
# 'a' (append mode) allows adding new content to the file without overwriting existing content
file_handle = open("pelican.txt", 'w')
#the second argument is the mode

# .write() method writes one string to the file
file_handle.write("A wonderful bird is the pelican\n")

file_handle.write("His bill holds more than his belican\n")

# Create a list of strings, with multiple lines of poem
# \n (new line) separates each string in the list
lines = ["He can take in his beak,\n", "Enough food for a week,\n", "But I'm damned if I see how the helican.\n"]
# .writelines method writes multiple lines from a list to the file
# .writelines assumes each line is a string
file_handle.writelines(lines)