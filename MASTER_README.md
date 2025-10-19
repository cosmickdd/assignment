# Welcome To Machine Learning I — Course & Assignment Overview

Welcome to the repository containing solutions and supporting materials for the Module 3 assignment in the "Welcome To Machine Learning I" course.

About the course

Welcome to Machine Learning I course at Columbia University. We are thrilled to have you join us on this exciting journey and explore this topic together. This is a self-directed course and you will have access to a wealth of resources, including lectures, readings, and assessments. Please note that no faculty and course assistants are actively monitoring this course. We encourage you to take advantage of the forums and other resources to connect with fellow learners. Once again, we are thrilled to have you as part of the learning community and look forward to witnessing your growth and development in this field.

Course materials and references
- Course developer and instructor: John Paisley — Associate Professor of Electrical Engineering
- UCI Machine Learning Repository — http://archive.ics.uci.edu/ml/
- Lecture slides and module notes (refer to course platform for original slides referenced in the assignment)

Repository contents
- `solution.ipynb` — Notebook implementing closed-form ridge regression and an active learning selection strategy. Uses provided data files.
- `run_assignment.py` — Small, standalone script that runs the same computations without opening the notebook.
- `solution_README.md` — Notes about the solution and how to run it.
- `samplesoln.ipynb` — Starter/sample notebook included with the assignment (modified to load provided filenames).
- Data files: `X_train-2.csv`, `y_train-1.csv`, `X_test.csv`, and an additional folder `second-assignment` with its own data.

How to use this repo
1. Install dependencies (only numpy required for the scripts provided):

```powershell
python -m pip install --user numpy
```

2. Run the solution script:

```powershell
python run_assignment.py
```

3. Or open `solution.ipynb` with Jupyter Notebook / JupyterLab and run the cells.

Acknowledgements and references
- Course developed and materials provided by John Paisley (Columbia University).
- UCI Machine Learning Repository for datasets and examples.

License
- This repository contains educational code and example solutions for learning purposes. Reuse for coursework is permitted; for any public distribution, please attribute the original course and instructor.

If you'd like, I can also:
- Add a `.gitignore` and `requirements.txt`.
- Initialize a local git repository and prepare instructions for pushing to GitHub.
- Create a small license file (MIT/Apache) if you plan to publish this publicly.

Tell me which of those you'd like me to do next.