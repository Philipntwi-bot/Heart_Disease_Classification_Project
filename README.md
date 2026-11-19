# 🫀 CARDIOPULSE AI // Clinical Cardiovascular Disease Diagnostic System

**Student:** Philip Antwi  
**Student ID:** PUIT24120002  
**Level:** 400  
**Programme:** BSc Information Technology  
**Institution:** Pentecost University, Accra, Ghana  
**Live Production Web App:** [https://heart-disease-classification-project.vercel.app](https://heart-disease-classification-project.vercel.app)  
**☁️ Vercel Console:** [https://vercel.com/philipntwi-bot/heart-disease-classification-project](https://vercel.com/philipntwi-bot/heart-disease-classification-project)  
**🐙 GitHub Repository:** [https://github.com/Philipntwi-bot/Heart_Disease_Classification_Project](https://github.com/Philipntwi-bot/Heart_Disease_Classification_Project)  
**⚡ VS Code in Browser:** [https://github.dev/Philipntwi-bot/Heart_Disease_Classification_Project](https://github.dev/Philipntwi-bot/Heart_Disease_Classification_Project)  

---

## 📌 Executive Summary

**CARDIOPULSE AI** is an advanced clinical cardiovascular risk screening platform developed as part of academic artificial intelligence research at Pentecost University. The system deploys a **Regularized Logistic Regression** classifier coupled with **StandardScaler** multi-variate feature normalization to predict the presence of cardiovascular pathology across a 500-patient clinical hospital cohort.

The production web interface features a bioluminescent crimson & cyan medical glassmorphism design, real-time Lead II Electrocardiogram (ECG) rhythm telemetry, authentic clinical pathology photography (Coronary Artery Disease, Atherosclerosis, Myocardial Infarction), an interactive 2×2 confusion matrix with epidemiological metric calculations, and an oral defense cheat sheet for academic Viva Voce examination.

---

## 🔬 Clinical Biomarkers & Features (10-Vector Input)

The classification matrix accepts 10 standardized physiological, hemodynamic, metabolic, lifestyle, and hereditary indicators:

| # | Clinical Biomarker | Measurement Unit | Normal Physiological Range | Cohort Mean ± Std |
|---|---|---|---|---|
| 1 | **Age** | Years | 30 – 79 years | 54.86 ± 14.32 |
| 2 | **Biological Sex** | Binary | Female (0) / Male (1) | 53.2% Male / 46.8% Female |
| 3 | **Resting Blood Pressure** | mmHg (Systolic) | 90 – 180 mmHg | 132.87 ± 26.42 |
| 4 | **Serum Cholesterol** | mg/dL | 150 – 300 mg/dL | 221.50 ± 43.86 |
| 5 | **Body Mass Index (BMI)** | kg/m² | 18.0 – 40.0 kg/m² | 29.02 ± 6.40 |
| 6 | **Cigarette Smoker** | Binary | No (0) / Yes (1) | 53.2% Smokers |
| 7 | **Diabetes Mellitus** | Binary | No (0) / Yes (1) | 47.4% Diabetic |
| 8 | **Physical Activity** | Ordinal Scale (0 - 4) | 0 (Sedentary) to 4 (High) | 2.05 ± 1.42 |
| 9 | **Family History of CAD** | Binary | No (0) / Yes (1) | 47.8% Positive Family History |
| 10 | **Stress Level Index** | Scale (1 - 10) | 1 (Low) to 10 (Critical) | 4.88 ± 2.60 |

---

## 📊 Model Evaluation & Statistical Metrics

Evaluated on an 80/20 stratified holdout test partition ($N = 100$ patient records):

### 1. Multi-Variate Confusion Matrix (Holdout N = 100)

| Actual \ Predicted | Predicted No Disease (0) | Predicted Heart Disease (1) |
|---|---|---|
| **Actual No Disease (0)** | **15 (True Negative - TN)** | 32 (False Positive - Type I Error) |
| **Actual Heart Disease (1)** | 12 (False Negative - Type II Error) | **41 (True Positive - TP)** |

### 2. Epidemiological Metric Derivations

* **Diagnostic Sensitivity (Recall):** $\text{Recall} = \frac{TP}{TP + FN} = \frac{41}{41 + 12} = \mathbf{77.36\%}$ *(Catches over 77% of pathological cases)*
* **Diagnostic Specificity:** $\text{Specificity} = \frac{TN}{TN + FP} = \frac{15}{15 + 32} = \mathbf{31.91\%}$
* **Positive Predictive Value (Precision):** $\text{Precision} = \frac{TP}{TP + FP} = \frac{41}{41 + 32} = \mathbf{56.16\%}$
* **Harmonic Mean (F1-Score):** $F_1 = 2 \times \frac{0.562 \times 0.774}{0.562 + 0.774} = \mathbf{0.651 \ (65.1\%)}$
* **Mathematical Sigmoid Activation:**  
  $$P(y = 1 \mid \mathbf{x}) = \frac{1}{1 + e^{-(\mathbf{w}^\top \mathbf{x}_{\text{scaled}} + b)}}$$

---

## 🌟 Interactive Key Features

1. **Authentic Cardiovascular Pathology Showcase:**
   - Curated medical photography illustrating **Atherosclerosis** (coronary lumen narrowing & plaque), **Myocardial Infarction** (ischemic tissue necrosis), **Hypertensive Remodeling**, and **Clinical ECG Telemetry**.
   - Interactive zoom modals for anatomical examination.

2. **Real-Time Dynamic ECG Waveform Canvas:**
   - Real-time animated Lead II electrocardiogram (P, QRS, T waves) that dynamically accelerates/decelerates based on the patient's blood pressure, stress level, and calculated cardiovascular risk.
   - Trace color dynamically transitions from **Emerald Green** (Low Risk) to **Crimson Red** (High Risk).

3. **Instant `<0.1 ms` Client-Side + Serverless Inference:**
   - Zero-latency standardized vector calculations executed directly in JavaScript with background fallback to Vercel Python API (`/api/predict`).
   - Quick-load profiles: *Low-Risk Patient*, *Borderline Profile*, *High-Risk Patient*, and *Random Cohort Sample*.

4. **Interactive 2×2 Confusion Matrix Grid:**
   - Clickable quadrants explaining True Negatives, False Positives, False Negatives, and True Positives with clinical risk implications.

5. **Lecturer Oral Defense Cheat Sheet:**
   - Comprehensive answers covering False Negatives in medicine, StandardScaler normalization rationale, and Sigmoid logit derivations.

---

## 🚀 Running Locally

```bash
git clone https://github.com/Philipntwi-bot/Heart_Disease_Classification_Project.git
cd Heart_Disease_Classification_Project
python -m http.server 8000
```
Open `http://localhost:8000` in your web browser.

---

## 📜 Verification & Academic Attribution

- **Student:** Philip Antwi
- **Student ID:** PUIT24120002
- **Programme:** BSc Information Technology (Level 400)
- **Institution:** Pentecost University, Accra, Ghana
- **Course:** Artificial Intelligence & Machine Learning
