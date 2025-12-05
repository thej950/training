# create_students_csv.py
import csv

# Open the CSV file in write mode
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write the header
    writer.writerow(["Name", "Age", "Marks"])

    # Write student records
    writer.writerow(["Rahul", 20, 85])
    writer.writerow(["Priya", 21, 90])
    writer.writerow(["Ankit", 19, 88])

print("students.csv created successfully with 3 records.")
