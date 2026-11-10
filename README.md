# Heart Disease Classification Project

**Student:** Philip Antwi | **Programme:** BSc Information Technology | **Institution:** Pentecost University

## Overview

A machine learning web application that predicts the likelihood of heart disease based on 10 patient medical and lifestyle features. Built with **Python (scikit-learn)**, deployed on **Vercel** as a static HTML front-end + Python serverless API.

---

## Project Structure

```
Heart_Disease_Classification_Project/
├── data/
│   └── hospital_synthetic_dataset.xlsx   # Raw dataset (500 patients)
├── api/
│   ├── predict.py                        # Vercel Python serverless handler
│   └── requirements.txt                  # Python dependencies for API
├── heart_disease_classification.py       # ML training pipeline
├── heart_disease_model.pkl               # Trained Logistic Regression model
├── scaler.pkl                            # StandardScaler for feature normalisation
├── feature_names.pkl                     # Ordered list of feature column names
├── confusion_matrix.png                  # Evaluation – confusion matrix
├── roc_curve.png                         # Evaluation – ROC curve
├── feature_importance.png                # Feature importance chart
├── class_distribution.png               # Class distribution chart
├── index.html                            # Static front-end (Vercel served)
├── vercel.json                           # Vercel deployment config
├── requirements.txt                      # Top-level Python dependencies
└── README.md
```

---

## Dataset

- **Source:** Synthetic hospital dataset (`hospital_synthetic_dataset.xlsx`)
- **Records:** 500 patients × 11 columns
- **Target:** `heart_disease` (0 = No, 1 = Yes)
- **Features:** `age`, `sex`, `blood_pressure`, `cholesterol`, `bmi`, `smoker`, `diabetes`, `physical_activity`, `family_history`, `stress_level`

---

## Machine Learning Pipeline

1. **Load data** from Excel file using `pandas`
2. **Encode** categorical features (`sex`, `smoker`, `diabetes`, `family_history`) with `LabelEncoder`
3. **Scale** numerical features with `StandardScaler`
4. **Train** Logistic Regression and Random Forest classifiers
5. **Select** the best model by accuracy
6. **Evaluate** using accuracy, confusion matrix, ROC-AUC, and classification report
7. **Save** model, scaler, and feature names with `joblib`

### Results

| Model                | Accuracy | ROC-AUC |
|----------------------|----------|---------|
| Logistic Regression  | 56.00%   | 0.5054  |
| Random Forest        | 48.00%   | 0.5317  |
| **Selected**         | **Logistic Regression** | — |

---

## Running the Training Script

```bash
python heart_disease_classification.py
```

This generates `heart_disease_model.pkl`, `scaler.pkl`, `feature_names.pkl`, and the four PNG visualisations.

---

## Running the API Locally

```bash
# Install dependencies
pip install scikit-learn numpy pandas joblib

# Start a local server on port 3000
python -c "
from http.server import HTTPServer
from api.predict import handler
HTTPServer(('localhost', 3000), handler).serve_forever()
"
```

Then open `index.html` in a browser (or use Live Server extension in VS Code).

---

## Vercel Deployment

1. Push this folder to a GitHub repository.
2. Go to [vercel.com](https://vercel.com) → **New Project** → Import the GitHub repo.
3. Vercel reads `vercel.json` and automatically:
   - Deploys the Python API at `/api/predict`
   - Serves `index.html` at the root URL

---

## Live Application

> Will be available after Vercel deployment at: `https://heart-disease-classification-projec.vercel.app/`

---

## Disclaimer

This application is an **academic machine learning demonstration**. It is **not** a substitute for professional medical advice, diagnosis, or treatment.

