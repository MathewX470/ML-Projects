# Student Pass or Fail Classification

A simple logistic regression classifier that predicts whether a student will pass or fail based on two features: Study Hours and Previous Exam Score. The workflow lives in the Jupyter notebook and uses scikit-learn.

## Project Files
- data.csv: Sample dataset with features and labels.
- requirements.txt: Python dependencies for the notebook.
- student.ipynb: Main notebook with training, evaluation, and a sample prediction.

## Setup
1. Use Python 3.10+ (3.11 also works).
2. (Optional) Create a virtual environment:
   - Windows (PowerShell):
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
- Open student.ipynb and run cells in order to train and evaluate the model.
- Adjust the sample input (Study Hours, Previous Exam Score) in the last cell to test predictions.

## Notes
- Ensure data.csv is present in the project root.
- If you add more features, update the feature selection cell in the notebook accordingly.
