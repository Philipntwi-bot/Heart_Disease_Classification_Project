import json
import joblib
import numpy as np
import pandas as pd
from pathlib import Path
from http.server import BaseHTTPRequestHandler

# ── Load model, scaler and feature names at cold-start ──
BASE          = Path(__file__).resolve().parent.parent
model         = joblib.load(BASE / "heart_disease_model.pkl")
scaler        = joblib.load(BASE / "scaler.pkl")
FEATURE_NAMES = joblib.load(BASE / "feature_names.pkl")  # list of 10 column names


class handler(BaseHTTPRequestHandler):

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        try:
            length = int(self.headers.get("Content-Length", 0))
            data   = json.loads(self.rfile.read(length))

            # Encode categorical vars exactly as in training
            sex_enc = 1 if str(data.get("sex",  "Male")).lower() == "male" else 0
            smk_enc = 1 if str(data.get("smoker",  "No")).lower() == "yes" else 0
            dia_enc = 1 if str(data.get("diabetes", "No")).lower() == "yes" else 0
            fam_enc = 1 if str(data.get("family_history", "No")).lower() == "yes" else 0

            # Build a named DataFrame so sklearn won't warn about feature names
            row = {
                "age":               float(data["age"]),
                "sex":               sex_enc,
                "blood_pressure":    float(data["blood_pressure"]),
                "cholesterol":       float(data["cholesterol"]),
                "bmi":               float(data["bmi"]),
                "smoker":            smk_enc,
                "diabetes":          dia_enc,
                "physical_activity": float(data["physical_activity"]),
                "family_history":    fam_enc,
                "stress_level":      float(data["stress_level"]),
            }
            features = pd.DataFrame([row], columns=FEATURE_NAMES)

            scaled     = scaler.transform(features)
            prediction = int(model.predict(scaled)[0])
            proba      = model.predict_proba(scaled)[0]
            confidence = round(float(proba[prediction]) * 100, 2)

            response = {
                "prediction": prediction,
                "result":     "Heart Disease Detected" if prediction == 1 else "No Heart Disease",
                "confidence": confidence,
                "probabilities": {
                    "no_disease":    round(float(proba[0]) * 100, 2),
                    "heart_disease": round(float(proba[1]) * 100, 2),
                }
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        except Exception as err:
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(err)}).encode())

    def log_message(self, format, *args):
        pass   # silence server request logs
