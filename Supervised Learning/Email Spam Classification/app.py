import os
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

MODEL = None
VECTORIZER = None
MODEL_READY = False
LOAD_ERROR = None


def load_artifacts():
    model_path = os.getenv("MODEL_PATH", "spam_model.pkl")
    vectorizer_path = os.getenv("VECTORIZER_PATH", "tfidf_vectorizer.pkl")
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    return model, vectorizer


try:
    MODEL, VECTORIZER = load_artifacts()
    MODEL_READY = True
except Exception as e:
    LOAD_ERROR = str(e)
    MODEL_READY = False


@app.get("/health")
def health():
    return jsonify({
        "status": "ok",
        "model_loaded": MODEL_READY,
        "error": LOAD_ERROR if not MODEL_READY else None
    })


@app.get("/")
def index():
    return render_template(
        "index.html",
        model_loaded=MODEL_READY,
        load_error=LOAD_ERROR
    )


@app.post("/predict")
def predict():
    if not MODEL_READY:
        return jsonify({"error": "Model not loaded", "details": LOAD_ERROR}), 503

    payload = request.get_json(silent=True) or {}
    text = payload.get("text")

    if text is None:
        # try form field fallback
        text = request.form.get("text")

    if not text or not isinstance(text, str) or not text.strip():
        return jsonify({"error": "Missing or empty 'text' field"}), 400

    try:
        X = VECTORIZER.transform([text])
        y_pred = MODEL.predict(X)[0]
        label = "Spam" if int(y_pred) == 1 else "Not Spam"

        confidence = None
        if hasattr(MODEL, "predict_proba"):
            proba = MODEL.predict_proba(X)[0]
            confidence = float(max(proba))

        return jsonify({
            "text": text,
            "predicted_class": int(y_pred),
            "predicted_label": label,
            "confidence": confidence
        })
    except Exception as e:
        return jsonify({"error": "Prediction failed", "details": str(e)}), 500


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)
