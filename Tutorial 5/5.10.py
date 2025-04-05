import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#create the stud.csv file
data = {
    "rollno": [1, 2, 3, 4, 5],
    "name": ["John", "Alice", "Bob", "Mary", "Tom"],
    "place": ["New York", "Los Angeles", "Chicago", "Houston", "Boston"],
    "mark": [85, 90, 78, 92, 88]
}
df = pd.DataFrame(data)
df.to_csv("stud.csv", index=False)

#Read and display the file contents
df = pd.read_csv("stud.csv")
print("File contents:")
print(df)

#set rollno as index
df.set_index("rollno", inplace=True)
print("\nFile contents after setting rollno as index:")
print(df)

#display name and mark
print("\nName and mark:")
print(df[["name", "mark"]])

#rollno, Name and mark in the order of name
print("\nrollno, Name and mark in the order of name:")
print(df.sort_values(by="name"))

#Display the rollno, name, mark in the descending order of mark
print("\nrollno, name, mark in the descending order of mark:")
print(df.sort_values(by="mark", ascending=False))

#Find the average mark, median and mode
print("\nAverage mark:", df["mark"].mean())
print("Median mark:", df["mark"].median())
print("Mode mark:", df["mark"].mode().values[0])

#find minimum and maximum marks
print("\nMinimum mark:", df["mark"].min())
print("Maximum mark:", df["mark"].max())

#Variance and standard deviation of marks
print("\nVariance of marks:", df["mark"].var())
print("Standard deviation of marks:", df["mark"].std())

#Display the histogram of marks
plt.hist(df["mark"], bins=5, edgecolor="black")
plt.xlabel("Mark")
plt.ylabel("Frequency")
plt.title("Histogram of Marks")
plt.show()

#Remove the place column
df.drop("place", axis=1, inplace=True)
print("\nFile contents after removing the place column:")
print(df)
