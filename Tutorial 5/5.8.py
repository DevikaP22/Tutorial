import pandas as pd


df = pd.read_csv("auto.csv")

#Clean and update the CSV file
df = df.drop_duplicates()  # Remove duplicates
df = df.dropna()  # Remove rows with missing values
df.to_csv("auto_updated.csv", index=False)  # Save the updated CSV file

#Find the most expensive car company name
most_expensive_car = df.loc[df["price"].idxmax()]
print("Most expensive car company name:", most_expensive_car["company"])

#print all Toyota car details
toyota_cars = df[df["company"] == "toyota"]
print("Toyota car details:")
print(toyota_cars)

#Print total cars of all companies
total_cars = df["company"].value_counts()
print("Total cars of all companies:")
print(total_cars)

#Find the highest priced car of all companies
highest_priced_car = df.loc[df["price"].idxmax()]
print("Highest priced car of all companies:")
print(highest_priced_car)

#Find the average mileage of all companies
average_mileage = df["average-mileage"].mean()
print("Average mileage of all companies:", average_mileage)

#sort all cars by Price column
df_sorted = df.sort_values(by="price")
print("Cars sorted by Price column:")
print(df_sorted)
