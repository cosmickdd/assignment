# Solution for Module 3 Project

This Folder contains a solution for the Module 3 assignment from the "Welcome To Machine Learning I" course.

Files included:
- `solution.ipynb` — Jupyter notebook that reproduces the ridge regression closed-form solution and runs the active learning selection to pick the first 10 measurement indices from the test pool.
- `run_assignment.py` — A standalone script that computes ridge weights and the 10 active-learning indices (useful for quick runs outside the notebook).
- Data files: `X_train-2.csv`, `y_train-1.csv`, `X_test.csv` (already present in the workspace).

How to run
1. Make sure you have Python 3.8+ and `numpy` installed.
2. Run the notebook `solution.ipynb` in Jupyter, or run the script from the command line:

```powershell
python run_assignment.py
```

Notes
- The script uses deterministic lambda=5.0 and sigma^2=2.0 for reproducibility. Modify these values in the notebook or script if you need different settings.
- Selected indices are 1-based to match the original assignment conventions.
