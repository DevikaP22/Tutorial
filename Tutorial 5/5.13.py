import pandas as pd


df = pd.read_csv("employee.csv")

# Print first 7 records from employees file
print("First 7 records:")
print(df.head(7))

# Print all employee names in alphabetical order
print("\nEmployee names in alphabetical order:")
print(df["name"].sort_values())

# Find the name of the employee with highest salary
max_salary_employee = df.loc[df["salary"].idxmax()]
print("\nEmployee with highest salary:")
print(max_salary_employee["name"])

# List the names of male employees
male_employees = df[df["gender"] == "Male"]
print("\nNames of male employees:")
print(male_employees["name"])

#. Display to which all teams employees belong
print("\nTeams employees belong to:")
print(df["team"].unique())
