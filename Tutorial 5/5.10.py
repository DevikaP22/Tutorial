import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = {
    "rollno": [1, 2, 3, 4, 5],
    "name": ["John", "Alice", "Bob", "Mary", "Tom"],
    "place": ["New York", "Los Angeles", "Chicago", "Houston", "Boston"],
    "mark": [85, 90, 78, 92, 88]
}
df = pd.DataFrame(data)
df.to_csv("stud.csv", index=False)
df = pd.read_csv("stud.csv")
print("File contents:")
print(df)
df.set_index("rollno", inplace=True)
print("\nFile contents after setting rollno as index:")
print(df)
print("\nName and mark:")
print(df[["name", "mark"]])
print("\nrollno, Name and mark in the order of name:")
print(df.sort_values(by="name"))
print("\nrollno, name, mark in the descending order of mark:")
print(df.sort_values(by="mark", ascending=False))
print("\nAverage mark:", df["mark"].mean())
print("Median mark:", df["mark"].median())
print("Mode mark:", df["mark"].mode().values[0])
print("\nMinimum mark:", df["mark"].min())
print("Maximum mark:", df["mark"].max())
print("\nVariance of marks:", df["mark"].var())
print("Standard deviation of marks:", df["mark"].std())
plt.hist(df["mark"], bins=5, edgecolor="black")
plt.xlabel("Mark")
plt.ylabel("Frequency")
plt.title("Histogram of Marks")
plt.show()
df.drop("place", axis=1, inplace=True)
print("\nFile contents after removing the place column:")
print(df)
