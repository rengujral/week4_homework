with open ("pelican.txt", 'r') as file_handle:
    file_content = file_handle.read()

print(type(file_content))

print("\nContent of pelican.txt:")
print(file_content)

with open("pelican.txt", "r") as file_handle:
    file_lines = file_handle.readlines()

print("Number of items within pelican.txt:", len(file_lines))

print("\nContent of pelican.txt:")
for line in file_lines:
    print(line.strip())