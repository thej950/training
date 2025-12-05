# write_students.py

# Open the file in write mode
file = open("student.txt", "w")

# Write 3 student names (one per line)
file.write("Rahul\n")
file.write("Priya\n")
file.write("Ankit\n")

# Close the file properly
file.close()

print("Student names written successfully to student.txt")
