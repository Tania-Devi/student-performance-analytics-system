import pandas as pd
import numpy as np

# Load student data
df = pd.read_csv("students.csv")

# Calculate total and average marks
subjects = ["Python", "Maths", "Science"]
df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1).round(2)

# Assign grades
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"

df["Grade"] = df["Average"].apply(calculate_grade)

# Display results
print("\n===== STUDENT PERFORMANCE ANALYTICS =====")
print(df.to_string(index=False))

print("\n===== CLASS SUMMARY =====")
print("Total students:", len(df))
print("Class average:", round(np.mean(df["Average"]), 2))
print("Highest average:", df["Average"].max())
print("Lowest average:", df["Average"].min())

# Find top performer
top_student = df.loc[df["Average"].idxmax()]
print("\nTop performer:", top_student["Name"])
print("Top performer's average:", top_student["Average"])

# Save analysed data
df.to_csv("student_analysis.csv", index=False)
print("\nAnalysis saved to student_analysis.csv")