# Ridge Regression + Active Learning Assignment

This repository contains a minimal solution for a ridge-regression and active-learning assignment.

Files:
- `samplesoln.ipynb` - Notebook with solutions for Part 1 (ridge regression) and Part 2 (active learning). Updated to load the provided CSVs.
- `run_assignment.py` - Standalone script to compute ridge regression weights and select the first 10 active-learning indices from the test pool.
- `X_train-2.csv`, `y_train-1.csv`, `X_test.csv` - Data files (provided by the assignment).

How to run

1. Make sure you have Python 3.8+ and numpy installed.
2. From the project root run:

```powershell
python run_assignment.py
```

This will print the ridge regression weights and the first 10 selected measurement indices (1-based).

License: put your preferred license here before publishing.
