# Student Marks Prediction

A simple linear regression project to predict students' grades from study time (hours/day). Built with pandas, numpy, matplotlib, and scikit-learn.

## Dataset
- File: `data.csv`
- Required columns: `study_time_hours`, `grade`

## Notebook
- File: `student_grade_prediction.ipynb`
- Steps:
  - Data loading and validation
  - Exploratory scatter plot
  - Train/test split (random_state=42)
  - Model training (LinearRegression)
  - Evaluation: MAE and R²
  - Visualizations: regression prediction line and residuals histogram
  - Single prediction demo (final cell)

## Quick Start
1. Install dependencies:
```bash
pip install notebook pandas numpy matplotlib scikit-learn
```

## Notes
- Ensure `data.csv` contains no missing values in the required columns; the notebook drops rows with missing `study_time_hours` or `grade`.
- The prediction line overlays the fitted linear model over the scatter plot for interpretability.
 - Single-value prediction uses a DataFrame with the same feature name (`study_time_hours`) as training to avoid scikit-learn feature-name warnings.
