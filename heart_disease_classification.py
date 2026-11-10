# ============================================================
# HEART DISEASE CLASSIFICATION USING MACHINE LEARNING
# Student: Philip Antwi | Pentecost University
# ============================================================

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")  # Non-interactive backend for saving plots
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import warnings
warnings.filterwarnings("ignore")

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    roc_auc_score,
    roc_curve,
)

# ─────────────────────────────────────────────
# 1. LOAD THE DATASET
# ─────────────────────────────────────────────

print("=" * 55)
print("  HEART DISEASE CLASSIFICATION — MACHINE LEARNING")
print("=" * 55)

DATA_PATH = "data/hospital_synthetic_dataset.xlsx"
df = pd.read_excel(DATA_PATH)

print("\n[1] Dataset Loaded Successfully!")
print(f"    Shape: {df.shape[0]} rows × {df.shape[1]} columns")
print(f"\n    Columns: {list(df.columns)}")

# ─────────────────────────────────────────────
# 2. EXPLORE THE DATASET
# ─────────────────────────────────────────────

print("\n[2] Dataset Overview:")
print(df.head())

print("\n    Data Types:")
print(df.dtypes)

print("\n    Missing Values:")
print(df.isnull().sum())

print("\n    Target Distribution (heart_disease):")
counts = df["heart_disease"].value_counts()
print(f"    No Heart Disease (0): {counts.get(0, 0)}")
print(f"    Heart Disease    (1): {counts.get(1, 0)}")

print("\n    Basic Statistics:")
print(df.describe())

# ─────────────────────────────────────────────
# 3. DATA PREPROCESSING
# ─────────────────────────────────────────────

print("\n[3] Preprocessing Data...")

# Encode categorical columns
le = LabelEncoder()
categorical_cols = ["sex", "smoker", "diabetes", "family_history"]

for col in categorical_cols:
    df[col] = le.fit_transform(df[col])
    print(f"    Encoded '{col}': {df[col].unique()}")

# Separate features and target
X = df.drop("heart_disease", axis=1)
y = df["heart_disease"]

print(f"\n    Features (X): {list(X.columns)}")
print(f"    Target   (y): heart_disease")

# Scale numerical features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

# Save the scaler for the web app
joblib.dump(scaler, "scaler.pkl")
joblib.dump(list(X.columns), "feature_names.pkl")
print("\n    Scaler saved as 'scaler.pkl'")

# ─────────────────────────────────────────────
# 4. TRAIN / TEST SPLIT
# ─────────────────────────────────────────────

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\n[4] Train-Test Split:")
print(f"    Training samples : {X_train.shape[0]}")
print(f"    Testing  samples : {X_test.shape[0]}")

# ─────────────────────────────────────────────
# 5. TRAIN MODELS
# ─────────────────────────────────────────────

print("\n[5] Training Models...")

# --- Logistic Regression ---
lr_model = LogisticRegression(max_iter=1000, random_state=42)
lr_model.fit(X_train, y_train)
lr_pred  = lr_model.predict(X_test)
lr_acc   = accuracy_score(y_test, lr_pred)
lr_auc   = roc_auc_score(y_test, lr_model.predict_proba(X_test)[:, 1])

print(f"\n    Logistic Regression:")
print(f"      Accuracy : {lr_acc * 100:.2f}%")
print(f"      ROC-AUC  : {lr_auc:.4f}")

# --- Random Forest ---
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred  = rf_model.predict(X_test)
rf_acc   = accuracy_score(y_test, rf_pred)
rf_auc   = roc_auc_score(y_test, rf_model.predict_proba(X_test)[:, 1])

print(f"\n    Random Forest:")
print(f"      Accuracy : {rf_acc * 100:.2f}%")
print(f"      ROC-AUC  : {rf_auc:.4f}")

# Pick best model
if rf_acc >= lr_acc:
    best_model = rf_model
    best_name  = "Random Forest"
    best_pred  = rf_pred
    best_acc   = rf_acc
else:
    best_model = lr_model
    best_name  = "Logistic Regression"
    best_pred  = lr_pred
    best_acc   = lr_acc

print(f"\n    ✔ Best Model Selected: {best_name} ({best_acc * 100:.2f}%)")

# ─────────────────────────────────────────────
# 6. SAVE THE BEST MODEL
# ─────────────────────────────────────────────

joblib.dump(best_model, "heart_disease_model.pkl")
print(f"\n[6] Best model saved as 'heart_disease_model.pkl'")

# ─────────────────────────────────────────────
# 7. EVALUATION
# ─────────────────────────────────────────────

print(f"\n[7] Evaluating Best Model ({best_name})...")

cm = confusion_matrix(y_test, best_pred)
print(f"\n    Confusion Matrix:")
print(cm)

report = classification_report(
    y_test, best_pred,
    target_names=["No Disease", "Heart Disease"]
)
print(f"\n    Classification Report:")
print(report)

# ─────────────────────────────────────────────
# 8. VISUALISATIONS
# ─────────────────────────────────────────────

print("\n[8] Generating and Saving Visualisations...")

# --- 8a. Confusion Matrix Heatmap ---
fig, ax = plt.subplots(figsize=(6, 5))
sns.heatmap(
    cm, annot=True, fmt="d", cmap="Blues",
    xticklabels=["No Disease", "Heart Disease"],
    yticklabels=["No Disease", "Heart Disease"],
    ax=ax
)
ax.set_title(f"Heart Disease Confusion Matrix\n({best_name})", fontsize=13)
ax.set_xlabel("Predicted Label")
ax.set_ylabel("Actual Label")
plt.tight_layout()
plt.savefig("confusion_matrix.png", dpi=300, bbox_inches="tight")
plt.close()
print("    Saved: confusion_matrix.png")

# --- 8b. ROC Curve ---
fig, ax = plt.subplots(figsize=(6, 5))
for model, name, color in [
    (lr_model, "Logistic Regression", "#1f77b4"),
    (rf_model, "Random Forest",       "#d62728"),
]:
    fpr, tpr, _ = roc_curve(y_test, model.predict_proba(X_test)[:, 1])
    auc_val = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
    ax.plot(fpr, tpr, label=f"{name} (AUC={auc_val:.3f})", color=color, lw=2)
ax.plot([0, 1], [0, 1], "k--", lw=1)
ax.set_xlabel("False Positive Rate")
ax.set_ylabel("True Positive Rate")
ax.set_title("ROC Curve — Heart Disease Classification")
ax.legend(loc="lower right")
plt.tight_layout()
plt.savefig("roc_curve.png", dpi=300, bbox_inches="tight")
plt.close()
print("    Saved: roc_curve.png")

# --- 8c. Feature Importance (Random Forest) ---
importances = pd.Series(
    rf_model.feature_importances_, index=X.columns
).sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(8, 5))
importances.plot(kind="bar", color="#17365D", ax=ax)
ax.set_title("Feature Importance — Random Forest")
ax.set_ylabel("Importance Score")
ax.set_xlabel("Feature")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("feature_importance.png", dpi=300, bbox_inches="tight")
plt.close()
print("    Saved: feature_importance.png")

# --- 8d. Target Distribution ---
fig, ax = plt.subplots(figsize=(5, 4))
target_counts = y.value_counts()
bars = ax.bar(
    ["No Disease", "Heart Disease"],
    target_counts.values,
    color=["#2ecc71", "#e74c3c"],
    edgecolor="white", width=0.5
)
for bar, val in zip(bars, target_counts.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
            str(val), ha="center", va="bottom", fontsize=11, fontweight="bold")
ax.set_title("Heart Disease — Class Distribution")
ax.set_ylabel("Number of Patients")
ax.set_ylim(0, max(target_counts.values) * 1.15)
plt.tight_layout()
plt.savefig("class_distribution.png", dpi=300, bbox_inches="tight")
plt.close()
print("    Saved: class_distribution.png")

# ─────────────────────────────────────────────
# 9. COMPARE ACTUAL vs PREDICTED (sample)
# ─────────────────────────────────────────────

print("\n[9] Sample Actual vs Predicted (first 10):")
print("-" * 40)
labels = {0: "No Disease", 1: "Heart Disease"}
for actual, predicted in list(zip(y_test, best_pred))[:10]:
    match = "✔" if actual == predicted else "✘"
    print(f"  Actual: {labels[actual]:<14} | Predicted: {labels[predicted]:<14} {match}")

print("\n" + "=" * 55)
print(f"  DONE — Best model: {best_name}")
print(f"  Test Accuracy: {best_acc * 100:.2f}%")
print("=" * 55)

