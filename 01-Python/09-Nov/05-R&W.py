# read_students.py

# Open the file in read mode
file = open("student.txt", "r")

# Read all lines from the file
lines = file.readlines()

# Print each line on the screen
print("Student Names:\n")
for line in lines:
    print(line.strip())  # strip() removes newline characters

# Close the file properly
file.close()
