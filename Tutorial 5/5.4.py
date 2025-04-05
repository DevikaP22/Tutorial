import pandas as pd
data = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)

df.to_excel("output.xlsx", index=False)



