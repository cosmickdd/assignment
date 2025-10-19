# Solution for Module 3 Project

This Folder contains a solution for the Module 3 assignment from the "Welcome To Machine Learning I" course.

Files included:
# Solution for Module 3 Project — Ridge Regression & Active Learning

This folder contains a student-style solution for the Module 3 assignment from the
"Welcome to Machine Learning I" course.

Files included
- `solution.ipynb` — Jupyter notebook that reproduces the ridge-regression
	closed-form solution and runs the active learning selection to pick the first
	10 measurement indices from the test pool. The notebook is written and
	commented like a student submission (short explanations, results, and small
	conclusions).
- `run_assignment.py` — Standalone script that computes ridge weights and the
	10 active-learning indices (useful for quick command-line runs).
- Data files: `X_train-2.csv`, `y_train-1.csv`, `X_test.csv` (present in the
	workspace).

How to run
1. Ensure Python 3.8+ and `numpy` are installed.
2. From the folder run:

```powershell
python run_assignment.py
```

Notes
- The notebook and script use deterministic values (lambda=5.0 and sigma^2=2.0)
	for reproducibility. Modify these values in the notebook or script as needed.
- Selected indices are reported as 1-based indices to match the assignment
	convention.

Acknowledgements
- Course: " Machine Learning I" — Columbia University.
- Course developer / tutor: John Paisley.
