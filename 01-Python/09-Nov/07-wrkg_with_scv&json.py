# read_students_csv.py
import csv

# Open the CSV file in read mode
with open("students.csv", "r") as file:
    reader = csv.reader(file)

    # Display all records
    print("Student Records:\n")
    for row in reader:
        print(row)
