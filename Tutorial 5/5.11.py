import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sales_data.csv")
toothpaste_sales = df["toothpaste"]
face_cream_sales = df["facecream"]
face_wash_sales = df["facewash"]
plt.figure(figsize=(10, 6))
plt.scatter(df["month_number"], toothpaste_sales, color='blue')
plt.xlabel("Month Number")
plt.ylabel("Toothpaste Sales")
plt.title("Toothpaste Sales Data")
plt.grid(True)
plt.show()
plt.figure(figsize=(10, 6))
plt.bar(df["month_number"], face_cream_sales, label="Face Cream", width=0.4, align='edge')
plt.bar(df["month_number"] - 0.4, face_wash_sales, label="Face Wash", width=0.4, align='edge')
plt.xlabel("Month Number")
plt.ylabel("Sales")
plt.title("Face Cream and Face Wash Sales Data")
plt.legend()
plt.grid(True)
plt.show()
total_face_cream_sales = face_cream_sales.sum()
total_face_wash_sales = face_wash_sales.sum()
total_toothpaste_sales = toothpaste_sales.sum()
plt.figure(figsize=(10, 6))
plt.pie(
    [total_face_cream_sales, total_face_wash_sales, total_toothpaste_sales],
    labels=["Face Cream", "Face Wash", "Toothpaste"],
    autopct='%1.1f%%',
    startangle=140
)
plt.title("Total Sales Data for Last Year")
plt.show()
