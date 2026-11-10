import streamlit as st
import joblib
import numpy as np
import pandas as pd

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Heart Disease AI Classifier",
    page_icon="❤️",
    layout="wide"
)

# ─────────────────────────────────────────────
# LOAD MODEL & SCALER
# ─────────────────────────────────────────────
model       = joblib.load("heart_disease_model.pkl")
scaler      = joblib.load("scaler.pkl")
feature_names = joblib.load("feature_names.pkl")

# ─────────────────────────────────────────────
# STYLING
# ─────────────────────────────────────────────
st.markdown("""
<style>
.stApp { background-color: #F8F9FA; }
.main-title { font-size: 38px; font-weight: bold; color: #C0392B; }
.subtitle   { font-size: 17px; color: #64748B; }
.result-positive { background:#FDECEA; padding:20px; border-radius:12px;
                   border-left:6px solid #E74C3C; text-align:center; }
.result-negative { background:#EAFAF1; padding:20px; border-radius:12px;
                   border-left:6px solid #2ECC71; text-align:center; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────
st.markdown('<div class="main-title">❤️ Heart Disease AI Classifier</div>',
            unsafe_allow_html=True)
st.markdown('<div class="subtitle">A Machine Learning System for Predicting Heart Disease Risk</div>',
            unsafe_allow_html=True)
st.divider()

# Info cards
c1, c2, c3 = st.columns(3)
with c1:
    st.info("🏥 **Dataset**\n\n1,000 patient records from hospital synthetic dataset")
with c2:
    st.success("🤖 **Algorithm**\n\nRandom Forest Classifier — ensemble learning")
with c3:
    st.warning("📊 **Features**\n\n10 medical + lifestyle risk factors")

st.write("")

# ─────────────────────────────────────────────
# INPUT FORM
# ─────────────────────────────────────────────
st.subheader("🩺 Enter Patient Medical Information")

col1, col2 = st.columns(2)

with col1:
    age              = st.number_input("Age (years)",          min_value=1,   max_value=120, value=50)
    sex              = st.selectbox("Sex",                     ["Male", "Female"])
    blood_pressure   = st.number_input("Blood Pressure (mmHg)", min_value=50, max_value=200, value=120)
    cholesterol      = st.number_input("Cholesterol (mg/dL)",  min_value=100, max_value=400, value=200)
    bmi              = st.number_input("BMI",                  min_value=10.0, max_value=60.0, value=25.0, step=0.1)

with col2:
    smoker            = st.selectbox("Smoker",                 ["No", "Yes"])
    diabetes          = st.selectbox("Diabetes",               ["No", "Yes"])
    physical_activity = st.number_input("Physical Activity (days/week)", min_value=0, max_value=7, value=3)
    family_history    = st.selectbox("Family History of Heart Disease", ["No", "Yes"])
    stress_level      = st.slider("Stress Level (1–10)",       min_value=1, max_value=10, value=5)

st.write("")

# ─────────────────────────────────────────────
# PREDICTION
# ─────────────────────────────────────────────
if st.button("🔍 Predict Heart Disease Risk", use_container_width=True):

    # Encode inputs to match training encoding
    sex_enc       = 1 if sex == "Male" else 0
    smoker_enc    = 1 if smoker == "Yes" else 0
    diabetes_enc  = 1 if diabetes == "Yes" else 0
    fam_enc       = 1 if family_history == "Yes" else 0

    raw = np.array([[age, sex_enc, blood_pressure, cholesterol, bmi,
                     smoker_enc, diabetes_enc, physical_activity,
                     fam_enc, stress_level]])

    scaled = scaler.transform(raw)
    prediction   = model.predict(scaled)[0]
    probabilities = model.predict_proba(scaled)[0]
    confidence   = probabilities[prediction] * 100

    st.divider()
    st.subheader("📋 Prediction Result")

    if prediction == 1:
        st.markdown(f"""
        <div class="result-positive">
            <h2 style="color:#C0392B">⚠️ HIGH RISK — HEART DISEASE DETECTED</h2>
            <p style="font-size:18px">Confidence: <strong>{confidence:.2f}%</strong></p>
            <p>Please consult a medical professional for a thorough assessment.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="result-negative">
            <h2 style="color:#1E8449">✅ LOW RISK — NO HEART DISEASE DETECTED</h2>
            <p style="font-size:18px">Confidence: <strong>{confidence:.2f}%</strong></p>
            <p>Maintain a healthy lifestyle to continue reducing your risk.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.subheader("📊 Risk Probability")
    prob_df = pd.DataFrame({
        "Outcome":     ["No Heart Disease", "Heart Disease"],
        "Probability (%)": [round(probabilities[0]*100, 2),
                            round(probabilities[1]*100, 2)]
    })
    st.bar_chart(prob_df.set_index("Outcome"))
    st.success("Analysis completed successfully!")

# ─────────────────────────────────────────────
# ABOUT
# ─────────────────────────────────────────────
st.divider()
with st.expander("ℹ️ About This System"):
    st.write("""
    This application uses a **Random Forest Classifier** trained on a synthetic hospital dataset
    of 1,000 patient records. It analyses 10 medical and lifestyle risk factors to predict
    whether a patient is at risk of heart disease.

    **Risk Factors Considered:**
    - Age, Sex, Blood Pressure, Cholesterol, BMI
    - Smoking Status, Diabetes, Physical Activity
    - Family History, Stress Level

    ⚠️ *This is an academic machine learning demonstration. It is NOT a substitute for
    professional medical advice, diagnosis, or treatment.*
    """)

st.caption("Heart Disease Classification Project | Machine Learning | Pentecost University")

