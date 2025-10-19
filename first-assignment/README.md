## Ridge Regression + Active Learning — First Assignment

This folder contains a minimal, reproducible solution for the "Ridge Regression + Active Learning" assignment.

## Summary
- **Part 1:** Implement L2-regularized least squares (ridge regression) and compute
	\(w_{RR} = \arg\min_w \|y - Xw\|^2 + \lambda \|w\|^2\).
- **Part 2:** Implement a sequential active learning procedure that selects, from an
	unlabeled pool, the next points to measure by maximizing predictive variance;
	repeat for the first 10 selections.

## Files in this folder
- `samplesoln.ipynb` — Notebook with worked solutions for Part 1 and Part 2. The
	notebook has been updated to load the dataset files present in this repo.
- `run_assignment.py` — Minimal, standalone script that:
	- Loads `X_train-2.csv`, `y_train-1.csv`, and `X_test.csv`.
	- Computes closed-form ridge regression weights (Part 1).
	- Runs the active-learning loop and returns the first 10 selected measurement
		indices (1-based).
	- Prints a short summary of results.
- `X_train-2.csv`, `y_train-1.csv`, `X_test.csv` — Data files supplied with the
	assignment. (Do not commit private data if you plan to publish.)

## Reproducibility
- The notebook and `run_assignment.py` use fixed numeric values for key
	parameters (e.g., \(\lambda\) and \(\sigma^2\)) for deterministic outputs.
	Change them in the notebook or edit the `lam` / `sigma2` variables in
	`run_assignment.py` to experiment.

## How to run (Windows / PowerShell)
1. Create and activate a virtual environment (recommended) and install
	 dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r ..\requirements.txt
```

2. Run the solution script from this folder:

```powershell
python run_assignment.py
```

The script prints the ridge regression weights (truncated) and the first 10
selected pool indices (1-based).

## Notes and suggestions
- The active learning code in the notebook simulates measurements for pool
	points using the current posterior mean. If you have true labels for any
	pool points, update the code to use those instead of simulated labels.
- If you plan to publish on GitHub, add a license file and remove or ignore any
	private data files.

## Course & credit
- **Course:** "Machine Learning I" — Columbia University.
- **Course developer / tutor:** John Paisley, Associate Professor of Electrical
	Engineering.



