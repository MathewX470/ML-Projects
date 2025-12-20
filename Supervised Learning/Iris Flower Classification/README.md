# Iris Flower Classification

A simple machine learning workflow using scikit-learn to classify iris species. Includes basic EDA with seaborn and a Logistic Regression model trained and evaluated in a Jupyter notebook.

## Project Structure
- `iris.ipynb`: Main notebook with EDA, training, evaluation, and test predictions
- `requirements.txt`: Python dependencies

## Quick Start

### 1) Create and activate a virtual environment (Windows PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2) Install dependencies
```powershell
pip install -r requirements.txt
```
Open `iris.ipynb` and run cells top-to-bottom.

## Notes
- The model is `LogisticRegression(max_iter=200)` trained on features from the Iris dataset.
- Predictions expect a DataFrame with columns matching `iris.feature_names`.
- Confusion matrix and pairplot visualizations use matplotlib/seaborn.

## Troubleshooting
- If you see a warning about "feature names", wrap your samples in a DataFrame:
```python
sample_df = pd.DataFrame([[6.1, 2.8, 4.7, 1.2]], columns=iris.feature_names)
model.predict(sample_df)
```