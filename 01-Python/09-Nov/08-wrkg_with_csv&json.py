# employee_json.py
import json

# Data to store
employee = {
    "name": "John",
    "id": 101,
    "skills": ["Python", "Flask"]
}

# Write data to JSON file
with open("employee.json", "w") as file:
    json.dump(employee, file, indent=4)

print("employee.json created successfully.\n")

# Read and print data from JSON file
with open("employee.json", "r") as file:
    data = json.load(file)

print("Employee Data:")
print(data)
