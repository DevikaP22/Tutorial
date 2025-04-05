
import pandas as pd
data = {
    'Name': ['John', 'Jane', 'Mike'],
    'Age': [28, 32, 36]
}
df = pd.DataFrame(data)
df.to_excel('data.xlsx', index=False)

print("Excel file created.")



