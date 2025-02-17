#opening and appending file
open_append = open("pelican.txt", "a")
#opening file with the open function and using two arguments the new file name and the a in a string which represents append
open_append.write("A wonderful bird is the pelican,\n")
#I've used the write method in order to add a new line
open_append.write("His bill hold more than his belican.\n")
lines = ["He can take in his beak,\n", "Enough food for a week,\n", "But I'm damned if I see how the helican.\n"]
open_append.writelines(lines)
#Why are the \n required
#They are required so a certain section of the sentence can be put on a new line. This makes easier to read.
print(open_append)
