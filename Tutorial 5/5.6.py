import csv
data = [
    ["SN", "Name", "Country", "Contribution", "Year"],
    ["1", "Linus Torvalds", "Finland", "Linux Kernel", "1991"],
    ["2", "Tim Berners-Lee", "England", "World Wide Web", "1990"],
    ["3", "Guido van Rossum", "Netherlands", "Python", "1991"]
]
with open("contributors.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

print("Data written to contributors.csv")

