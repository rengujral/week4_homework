
with open ("pelican.txt", 'a') as file_handle:
    file_handle.write("A wonderful bird is the pelican\n")
    file_handle.write("His bill holds more than his belican\n")
    lines = ["He can take in his beak, \n", "Enough food for a week, \n", "But I'm damned if I see how the helican. \n"]
    file_handle.writelines(lines)