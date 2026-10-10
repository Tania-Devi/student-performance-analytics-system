# Student Performance Analytics System

A beginner Python project that uses Pandas and NumPy to summarize marks and attendance for 20 students.

## What it does

- Reads student information from `students.csv` into a Pandas DataFrame.
- Calculates each student's total and average marks.
- Assigns grades and pass/fail results.
- Shows class and subject averages, highest and lowest averages, attendance, and the top 3 students.

## Rules used

- Each subject is marked out of 100.
- Grade: A = 90+, B = 75–89, C = 60–74, D = 40–59, F = below 40.
- A student passes only if they score at least 40 in every subject.
- Attendance is recorded as a percentage.

## Run the project

1. Install Python 3.
2. Open a terminal in this folder.
3. Install the libraries: `python -m pip install -r requirements.txt`
4. Run: `python main.py`

## Files

- `main.py` — program and reusable functions.
- `students.csv` — sample records for 20 students.
- `Project_Documentation.md` — full project report.
- `requirements.txt` — required Python libraries.

This project uses beginner concepts: variables, data types, functions, loops, Pandas, NumPy, and basic data analysis. It does not use machine learning.
