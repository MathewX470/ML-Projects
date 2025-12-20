# IMDB Rating Prediction

Predict IMDB ratings using a scikit-learn pipeline with feature engineering and one-hot encoding. The model trains on the included dataset and supports inference via a saved `.pkl` file.

## Project Structure
- `imdb.ipynb`: End-to-end notebook for loading data, preprocessing, training, evaluation, and saving the model.
- `imdb_top_1000.csv`: Dataset used for training and evaluation.
- `requirements.txt`: Python dependencies.
- `imdb_rating_predictor.pkl` (generated): Trained model pipeline saved by the notebook.

## Features
- Numeric: `Released_Year`, `Runtime` (minutes), `Meta_score`, `No_of_Votes`
- Categorical (one-hot encoded): `Genre`, `Certificate`, `Director`

## Setup
### 1) Create a virtual environment (Windows PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2) Install dependencies
```powershell
pip install -r requirements.txt
```

## Train & Evaluate
Open the notebook and run all cells:
- `imdb.ipynb`
This will:
- Load and clean the data
- One-hot encode categorical columns
- Train a `RandomForestRegressor`
- Print metrics (R² and MAE)
- Save the trained model to `imdb_rating_predictor.pkl`

## Quick Inference Example (after training)
```python
import joblib
import pandas as pd

model = joblib.load("imdb_rating_predictor.pkl")

sample_movie = pd.DataFrame({
    "Released_Year": [2022],
    "Runtime": [176],
    "Meta_score": [72],
    "No_of_Votes": [906000],
    "Genre": ["Action"],
    "Certificate": ["PG-13"],
    "Director": ["Christopher Nolan"],
})

pred = model.predict(sample_movie)[0]
print("Predicted IMDB Rating:", round(float(pred), 3))
```

## Notes
- The preprocessing pipeline uses `OneHotEncoder(handle_unknown='ignore')` for categorical columns to safely handle unseen categories at inference.
- Rows with missing values in selected columns are dropped by the notebook for simplicity.
- The dataset file is kept in the repository; model artifacts (`*.pkl`, `*.joblib`) are ignored by default via `.gitignore`.
