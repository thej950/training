# create_and_write_file.py

# Open the file in write mode
file = open("mydata.txt", "w")

# Write your name and age into the file
file.write("Name: Navathej\n")
file.write("Age: 25\n")

# Close the file properly
file.close()

print("Data written successfully to mydata.txt")
