# Student Marks Prediction App

A simple Flask web app that predicts a student's total score based on weekly self‑study hours using a trained scikit‑learn model.

## Features
- Flask UI with modern styling
- Single‑feature regression (weekly self‑study hours)
- Model trained in Jupyter notebook and saved with `joblib`

## Project Structure
```
.
├─ app.py                   # Flask app (serves form + inference)
├─ templates/
│  └─ index.html            # App UI template
├─ data/
│  └─ data.csv              # Training data
├─ train_model.ipynb        # Notebook to train and save model
├─ requirements.txt         # Python dependencies
├─ student_score_model.pkl (or model.pkl)  # Saved model artifact
└─ .venv/                   # Virtual environment (optional)
```

## Setup
```powershell
# 1) Create and activate a virtual environment (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2) Install dependencies
pip install -r requirements.txt
```

## Train the Model
Open `train_model.ipynb` and run cells to:
- Load `data/data.csv`
- Train a regression model using `weekly_self_study_hours`
- Save the model with `joblib.dump(...)` (ensure the filename matches `app.py`)

## Run the App
```powershell
python app.py
```
Visit http://127.0.0.1:5000 and enter weekly self‑study hours.

## Notes
- Ensure the model’s expected feature names match the DataFrame used in `app.py` (`weekly_self_study_hours`).
- If you change the model filename (e.g., `model.pkl` vs `student_score_rf_model.pkl`), update the loader path in `app.py` accordingly.
- For production, disable `debug=True` and consider proper logging and error handling.

## License
This project is for educational purposes.