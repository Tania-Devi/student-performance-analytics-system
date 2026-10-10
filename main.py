"""Beginner-friendly Student Performance Analytics System."""

from pathlib import Path

import numpy as np
import pandas as pd


DATA_FILE = Path(__file__).parent / "students.csv"
SUBJECTS = ["Maths", "Science", "English", "Computer"]


def load_data(file_path=DATA_FILE):
    """Read student records from a CSV file into a Pandas DataFrame."""
    data = pd.read_csv(file_path)
    return data


def assign_grade(average):
    """Return a grade using the student's average marks."""
    if average >= 90:
        return "A"
    if average >= 75:
        return "B"
    if average >= 60:
        return "C"
    if average >= 40:
        return "D"
    return "F"


def add_student_results(data):
    """Calculate totals, averages, grades, and pass/fail results."""
    data = data.copy()
    data["Total"] = data[SUBJECTS].sum(axis=1)
    data["Average"] = np.round(data[SUBJECTS].mean(axis=1), 2)
    data["Grade"] = data["Average"].apply(assign_grade)

    # A student passes only when every subject mark is at least 40.
    data["Result"] = [
        "Pass" if all(mark >= 40 for mark in marks) else "Fail"
        for marks in data[SUBJECTS].itertuples(index=False, name=None)
    ]
    return data


def show_report(data):
    """Print student, class, subject, attendance, and top-student results."""
    data = add_student_results(data)

    print("\nSTUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 80)
    print(data[["Student_ID", "Name", "Department", "Total", "Average", "Grade", "Result"]].to_string(index=False))

    print("\nCLASS SUMMARY")
    print(f"Class average: {data['Average'].mean():.2f}")
    print(f"Highest student average: {data['Average'].max():.2f}")
    print(f"Lowest student average: {data['Average'].min():.2f}")
    print(f"Students passed: {(data['Result'] == 'Pass').sum()}")
    print(f"Students failed: {(data['Result'] == 'Fail').sum()}")

    print("\nSUBJECT-WISE AVERAGES")
    for subject in SUBJECTS:  # Loop through every subject.
        subject_average = np.mean(data[subject].to_numpy())
        print(f"{subject}: {subject_average:.2f}")

    print("\nATTENDANCE")
    print(f"Class attendance average: {data['Attendance'].mean():.2f}%")
    print(f"Students below 75% attendance: {(data['Attendance'] < 75).sum()}")

    print("\nTOP 3 PERFORMERS")
    top_students = data.nlargest(3, "Average")
    print(top_students[["Student_ID", "Name", "Average", "Grade"]].to_string(index=False))


def main():
    """Run the program."""
    students = load_data()
    show_report(students)


if __name__ == "__main__":
    main()
