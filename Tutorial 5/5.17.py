mport pandas as pd
df = pd.read_csv("student.csv")
average_cgpa = df["CGPA"].mean()
print(" Average CGPA of Students:", round(average_cgpa, 2))
high_cgpa_students = df[df["CGPA"] > 9]
print("\n Students with CGPA > 9:\n", high_cgpa_students)
cse_high_cgpa = df[(df["Branch"] == "CSE") & (df["CGPA"] > 9)]
print("\n CSE Students with CGPA > 9:\n", cse_high_cgpa)
max_cgpa_student = df[df["CGPA"] == df["CGPA"].max()]
print("\n Student with Maximum CGPA:\n", max_cgpa_student)
branch_avg_cgpa = df.groupby("Branch")["CGPA"].mean()
print("\n Average CGPA of Each Branch:\n", branch_avg_cgpa)

