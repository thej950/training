# read_mydata.py

# Open the file in read mode
file = open("mydata.txt", "r")

# Read the file contents
content = file.read()

# Print the contents on the screen
print("File Contents:\n")
print(content)

# Close the file
file.close()
