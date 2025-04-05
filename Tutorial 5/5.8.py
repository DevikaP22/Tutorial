import pandas as pd


df = pd.read_csv("auto.csv")


df = df.drop_duplicates()  
df = df.dropna()  
df.to_csv("auto_updated.csv", index=False)  
most_expensive_car = df.loc[df["price"].idxmax()]
print("Most expensive car company name:", most_expensive_car["company"])
toyota_cars = df[df["company"] == "toyota"]
print("Toyota car details:")
print(toyota_cars)
total_cars = df["company"].value_counts()
print("Total cars of all companies:")
print(total_cars)
highest_priced_car = df.loc[df["price"].idxmax()]
print("Highest priced car of all companies:")
print(highest_priced_car)
average_mileage = df["average-mileage"].mean()
print("Average mileage of all companies:", average_mileage)
df_sorted = df.sort_values(by="price")
print("Cars sorted by Price column:")
print(df_sorted)
