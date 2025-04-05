import pandas as pd


df = pd.read_csv("employee.csv")
print("First 7 records:")
print(df.head(7))
print("\nEmployee names in alphabetical order:")
print(df["name"].sort_values())
max_salary_employee = df.loc[df["salary"].idxmax()]
print("\nEmployee with highest salary:")
print(max_salary_employee["name"])
male_employees = df[df["gender"] == "Male"]
print("\nNames of male employees:")
print(male_employees["name"])
print("\nTeams employees belong to:")
print(df["team"].unique())
