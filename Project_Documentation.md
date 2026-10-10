# Student Performance Analytics System — Project Documentation

## 1. Project title

Student Performance Analytics System

## 2. Introduction

This project is a simple Python program for understanding student marks and attendance. It reads records from a CSV file, calculates useful results, and prints a report. It is designed for learning Python data analysis with NumPy and Pandas.

## 3. Problem statement

Checking marks for many students by hand takes time. This program organizes the records and calculates totals, averages, grades, results, subject performance, and attendance statistics automatically.

## 4. Project objectives

- Read a student dataset from a CSV file.
- Organize the data in a Pandas DataFrame.
- Use NumPy for numerical calculations.
- Use functions to keep the code reusable and clear.
- Use loops to process subjects and marks.
- Find student and class performance results.

## 5. Tools and concepts

- Python 3
- Pandas for reading and organizing CSV data
- NumPy for numerical calculations
- Variables, strings, numbers, lists, functions, conditions, and loops

## 6. Dataset description

The file `students.csv` contains 20 sample students. Each row has a student ID, name, department, marks in Maths, Science, English, and Computer, and attendance percentage. Each subject mark is out of 100.

## 7. Grading and pass/fail rules

The grade uses the student's average across four subjects:

| Average | Grade |
| --- | --- |
| 90 or more | A |
| 75 to below 90 | B |
| 60 to below 75 | C |
| 40 to below 60 | D |
| Below 40 | F |

A student passes when the mark in **every subject** is at least 40. If any one subject mark is below 40, the student fails. Attendance does not change the academic pass/fail result; it is reported separately.

## 8. Program workflow

1. `load_data()` reads `students.csv` with Pandas.
2. `add_student_results()` calculates totals, averages, grades, and pass/fail results.
3. A loop calculates and prints each subject average.
4. `show_report()` prints student results, class summary, attendance, and the top 3 performers.
5. `main()` starts the program.

## 9. Functions used

- `load_data()` — loads the CSV file into a DataFrame.
- `assign_grade(average)` — returns a grade for a student's average.
- `add_student_results(data)` — adds total, average, grade, and result columns.
- `show_report(data)` — prints the complete analysis.
- `main()` — connects the steps and runs the system.

## 10. NumPy and Pandas use

Pandas reads the CSV data and stores it in a DataFrame. It also calculates row totals, averages, and top performers. NumPy calculates the average for each subject and rounds student averages.

## 11. Outputs

When run, the program displays:

- Total, average, grade, and result for each student
- Class average and the highest and lowest student averages
- Numbers of students who passed and failed
- Average mark for each subject
- Average attendance and the number below 75% attendance
- The top 3 performers

## 12. How to run

Open a terminal in the project folder and run:

```text
python -m pip install -r requirements.txt
python main.py
```

## 13. Conclusion

The project demonstrates how Python, Pandas, and NumPy can turn a small student dataset into a clear performance report. It practices the class concepts of functions, loops, conditions, and data analysis without requiring machine learning.

## 14. Possible future improvements

- Let a user enter new student records.
- Save the calculated report to a new CSV file.
- Add simple charts for marks and attendance.
