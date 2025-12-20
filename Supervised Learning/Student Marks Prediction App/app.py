from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load pre-trained model
try:
    model = joblib.load("model.pkl")
except Exception:
    model = None

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        try:
            study_hours = float(request.form["study_hours"]) 
        except (KeyError, ValueError):
            study_hours = None

        # Build a DataFrame with the exact feature names used during training
        # Notebook trained on: weekly_self_study_hours, attendance_percentage, class_participation
        if study_hours is not None and model is not None:
            features_df = pd.DataFrame({"weekly_self_study_hours": [study_hours]})
            prediction = model.predict(features_df)[0]
        else:
            prediction = None

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
