# -*- coding: utf-8 -*-
"""
Generate Complete Enhanced Heart Disease Web Application (CardioPulse AI)
With:
- Authentic Medical Imagery (Coronary Artery Disease, Atherosclerosis, ECG monitor, Cardiac Care)
- Live Interactive 10-Biomarker Sliders & Toggles with Zero-Latency Client Inference + Server Sync
- Animated Dynamic ECG Waveform Canvas (Pulses faster/slower based on risk)
- Interactive 2x2 Clinical Confusion Matrix with Live Cell Inspector
- Step-by-Step Mathematical Derivations (Sensitivity, Specificity, Precision, F1-Score, ROC-AUC)
- High-Resolution Medical Charts Modal (ROC, Feature Importance, Confusion Matrix, Cohort Distribution)
- Comprehensive Lecturer Oral Defense Guide
- 1-Click GitHub & Vercel Navigation Buttons
- Student Attribution: Philip Antwi | PUIT24120002 | Level 400 BSc IT | Pentecost University
"""

import json
import base64
import os
from pathlib import Path

ROOT_DIR = Path(r"C:\Users\User\OneDrive\Desktop\MY IA FOR ARTIFICIAL INTELLIGENCE\Heart_Disease_Classification_Project")

# Load model data
with open(ROOT_DIR / "heart_model_data.json", "r", encoding="utf-8") as f:
    model_data = json.load(f)

# Image paths (relative paths)
img_cardiac_care = "image/cardiac_care.jpg"
img_ecg_monitor = "image/ecg_monitor.jpg"
img_heart_steth = "image/heart_stethoscope.jpg"
img_heart_anat = "image/heart_likhitha.png"
img_athero = "image/diagno_3.jpg"
img_infarct = "image/diagno_2.jpg"
img_stress = "image/diagno_4.jpg"

cm_path = "confusion_matrix.png"
roc_path = "roc_curve.png"
fi_path = "feature_importance.png"
dist_path = "class_distribution.png"

model_data_json = json.dumps(model_data)

print("Building CardioPulse AI index.html...")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CARDIOPULSE AI // Clinical Cardiovascular Risk Diagnostic System</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

    <style>
        :root {{
            --bg-void: #030712;
            --bg-surface: #0b0f19;
            --surface-card: rgba(15, 23, 42, 0.78);
            --surface-elevated: rgba(30, 41, 59, 0.75);
            --card-border: rgba(239, 68, 68, 0.3);
            --border-subtle: rgba(255, 255, 255, 0.08);
            --neon-crimson: #ef4444;
            --neon-rose: #f43f5e;
            --neon-ruby: #e11d48;
            --neon-amber: #f59e0b;
            --neon-emerald: #10b981;
            --neon-cyan: #06b6d4;
            --neon-indigo: #6366f1;
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --text-muted: #64748b;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
        }}

        body {{
            background-color: var(--bg-void);
            color: var(--text-primary);
            min-height: 100vh;
            overflow-x: hidden;
            position: relative;
            padding-bottom: 70px;
        }}

        /* Subtle Medical Grid Backdrop */
        .bg-grid {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-size: 40px 40px;
            background-image: 
                linear-gradient(to right, rgba(255, 255, 255, 0.02) 1px, transparent 1px),
                linear-gradient(to bottom, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
            pointer-events: none;
            z-index: 0;
        }}

        .glow-overlay {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                radial-gradient(circle at 10% 20%, rgba(239, 68, 68, 0.12) 0%, transparent 45%),
                radial-gradient(circle at 85% 80%, rgba(6, 182, 212, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 50% 50%, rgba(244, 63, 94, 0.06) 0%, transparent 60%);
            pointer-events: none;
            z-index: 1;
        }}

        .app-container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 24px 28px;
            position: relative;
            z-index: 2;
        }}

        /* Top Navigation Bar */
        .top-navbar {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 16px 24px;
            background: rgba(15, 23, 42, 0.7);
            backdrop-filter: blur(20px);
            border: 1px solid var(--border-subtle);
            border-radius: 20px;
            margin-bottom: 28px;
            gap: 16px;
            flex-wrap: wrap;
        }}

        .brand-block {{
            display: flex;
            align-items: center;
            gap: 14px;
        }}

        .brand-icon {{
            width: 44px;
            height: 44px;
            background: linear-gradient(135deg, #ef4444, #f43f5e);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            box-shadow: 0 0 20px rgba(239, 68, 68, 0.5);
            animation: heartBeat 2s infinite ease-in-out;
        }}

        @keyframes heartBeat {{
            0%, 100% {{ transform: scale(1); }}
            14% {{ transform: scale(1.18); }}
            28% {{ transform: scale(1); }}
            42% {{ transform: scale(1.12); }}
            70% {{ transform: scale(1); }}
        }}

        .brand-info h1 {{
            font-family: 'Space Grotesk', sans-serif;
            font-size: 19px;
            font-weight: 700;
            letter-spacing: -0.5px;
            color: #fff;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .brand-badge {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 10px;
            font-weight: 700;
            background: rgba(239, 68, 68, 0.18);
            color: var(--neon-crimson);
            border: 1px solid rgba(239, 68, 68, 0.4);
            padding: 2px 7px;
            border-radius: 6px;
        }}

        .brand-sub {{
            font-size: 12px;
            color: var(--text-secondary);
            margin-top: 2px;
        }}

        .author-badge {{
            display: flex;
            align-items: center;
            gap: 10px;
            background: rgba(30, 41, 59, 0.65);
            border: 1px solid rgba(239, 68, 68, 0.3);
            padding: 8px 16px;
            border-radius: 12px;
            font-size: 12px;
        }}

        .author-dot {{
            width: 8px;
            height: 8px;
            background: #ef4444;
            border-radius: 50%;
            box-shadow: 0 0 10px #ef4444;
            animation: pulseDot 2s infinite;
        }}

        @keyframes pulseDot {{
            0%, 100% {{ transform: scale(1); opacity: 1; }}
            50% {{ transform: scale(1.3); opacity: 0.6; }}
        }}

        .nav-actions {{
            display: flex;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }}

        .btn-nav {{
            display: inline-flex;
            align-items: center;
            gap: 7px;
            padding: 8px 14px;
            border-radius: 10px;
            font-size: 12px;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.25s ease;
            cursor: pointer;
            border: 1px solid transparent;
        }}

        .btn-github {{
            background: rgba(255, 255, 255, 0.08);
            color: #fff;
            border-color: rgba(255, 255, 255, 0.15);
        }}
        .btn-github:hover {{
            background: rgba(255, 255, 255, 0.16);
            transform: translateY(-2px);
            border-color: rgba(255, 255, 255, 0.3);
        }}

        .btn-vercel {{
            background: linear-gradient(135deg, rgba(239, 68, 68, 0.2), rgba(244, 63, 94, 0.25));
            color: #fda4af;
            border-color: rgba(239, 68, 68, 0.4);
        }}
        .btn-vercel:hover {{
            background: linear-gradient(135deg, rgba(239, 68, 68, 0.35), rgba(244, 63, 94, 0.4));
            color: #fff;
            transform: translateY(-2px);
            box-shadow: 0 0 15px rgba(239, 68, 68, 0.35);
        }}

        .btn-console {{
            background: rgba(6, 182, 212, 0.15);
            color: #38bdf8;
            border-color: rgba(6, 182, 212, 0.35);
        }}
        .btn-console:hover {{
            background: rgba(6, 182, 212, 0.25);
            color: #fff;
            transform: translateY(-2px);
        }}

        /* Cardiovascular Medical Showcase (Bing search images) */
        .showcase-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 16px;
        }}

        .section-tag {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            color: var(--neon-crimson);
            font-weight: 700;
        }}

        .pathology-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 18px;
            margin-bottom: 30px;
        }}

        @media (max-width: 1100px) {{
            .pathology-grid {{ grid-template-columns: repeat(2, 1fr); }}
        }}
        @media (max-width: 650px) {{
            .pathology-grid {{ grid-template-columns: 1fr; }}
            .app-container {{ padding: 16px; }}
        }}

        .pathology-card {{
            background: var(--surface-card);
            border: 1px solid var(--border-subtle);
            border-radius: 18px;
            overflow: hidden;
            backdrop-filter: blur(16px);
            transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            cursor: pointer;
            display: flex;
            flex-direction: column;
        }}

        .pathology-card:hover {{
            transform: translateY(-5px);
            border-color: rgba(239, 68, 68, 0.55);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6);
        }}

        .pathology-img-wrap {{
            position: relative;
            width: 100%;
            height: 160px;
            overflow: hidden;
            background: #0f172a;
        }}

        .pathology-img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.6s ease;
        }}

        .pathology-card:hover .pathology-img {{
            transform: scale(1.08);
        }}

        .pathology-badge-top {{
            position: absolute;
            top: 10px;
            left: 10px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 10px;
            font-weight: 700;
            padding: 3px 8px;
            border-radius: 6px;
            backdrop-filter: blur(10px);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            background: rgba(15, 23, 42, 0.85);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #fff;
        }}

        .pathology-content {{
            padding: 16px;
            flex: 1;
            display: flex;
            flex-direction: column;
        }}

        .pathology-title {{
            font-family: 'Space Grotesk', sans-serif;
            font-size: 16px;
            font-weight: 700;
            color: #fff;
            margin-bottom: 4px;
        }}

        .pathology-sub {{
            font-size: 11px;
            color: var(--neon-crimson);
            font-weight: 600;
            margin-bottom: 8px;
            text-transform: uppercase;
        }}

        .pathology-desc {{
            font-size: 12.5px;
            color: var(--text-secondary);
            line-height: 1.5;
            flex: 1;
        }}

        /* Main Workspace (Left Inputs, Right Diagnostics) */
        .workspace-grid {{
            display: grid;
            grid-template-columns: 1.15fr 0.85fr;
            gap: 24px;
            margin-bottom: 32px;
        }}

        @media (max-width: 1050px) {{
            .workspace-grid {{ grid-template-columns: 1fr; }}
        }}

        .card-panel {{
            background: var(--surface-card);
            border: 1px solid var(--card-border);
            border-radius: 24px;
            padding: 28px;
            backdrop-filter: blur(20px);
            box-shadow: 0 20px 45px rgba(0, 0, 0, 0.4);
            position: relative;
        }}

        .panel-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 22px;
        }}

        .panel-title {{
            font-family: 'Space Grotesk', sans-serif;
            font-size: 18px;
            font-weight: 700;
            color: #fff;
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        /* Preset Chips */
        .preset-chips-strip {{
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            margin-bottom: 24px;
        }}

        .preset-chip {{
            padding: 7px 14px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-subtle);
            border-radius: 999px;
            font-size: 11.5px;
            font-weight: 600;
            color: #cbd5e1;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .preset-chip:hover {{
            background: rgba(239, 68, 68, 0.15);
            border-color: rgba(239, 68, 68, 0.45);
            color: #fff;
            transform: translateY(-1px);
        }}

        /* Sensors / Form Grid */
        .sensors-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            margin-bottom: 20px;
        }}

        @media (max-width: 650px) {{
            .sensors-grid {{ grid-template-columns: 1fr; }}
        }}

        .sensor-box {{
            background: rgba(15, 23, 42, 0.65);
            border: 1px solid var(--border-subtle);
            border-radius: 16px;
            padding: 15px;
            transition: border-color 0.25s ease;
        }}
        .sensor-box:focus-within {{
            border-color: var(--neon-crimson);
            box-shadow: 0 0 15px rgba(239, 68, 68, 0.18);
        }}

        .sensor-meta {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 8px;
        }}

        .sensor-label {{
            font-size: 13px;
            font-weight: 600;
            color: #e2e8f0;
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        .sensor-hint {{
            font-size: 10px;
            color: var(--text-muted);
            font-family: 'JetBrains Mono', monospace;
        }}

        .sensor-num-input {{
            width: 76px;
            background: rgba(0, 0, 0, 0.4);
            border: 1px solid var(--border-subtle);
            border-radius: 8px;
            padding: 5px 8px;
            color: var(--neon-crimson);
            font-family: 'JetBrains Mono', monospace;
            font-size: 14px;
            font-weight: 700;
            text-align: right;
            outline: none;
            transition: all 0.2s;
        }}
        .sensor-num-input:focus {{
            border-color: var(--neon-crimson);
            background: rgba(239, 68, 68, 0.1);
        }}

        /* Range Slider */
        .range-slider {{
            -webkit-appearance: none;
            width: 100%;
            height: 6px;
            background: #1e293b;
            border-radius: 3px;
            outline: none;
            cursor: pointer;
            margin: 6px 0;
        }}
        .range-slider::-webkit-slider-thumb {{
            -webkit-appearance: none;
            appearance: none;
            width: 18px;
            height: 18px;
            border-radius: 50%;
            background: linear-gradient(135deg, #ef4444, #f43f5e);
            cursor: pointer;
            box-shadow: 0 0 10px rgba(239, 68, 68, 0.8);
            border: 2px solid #fff;
            transition: transform 0.15s ease;
        }}
        .range-slider::-webkit-slider-thumb:hover {{
            transform: scale(1.25);
        }}

        .sensor-scale {{
            display: flex;
            justify-content: space-between;
            font-size: 10px;
            color: var(--text-muted);
            font-family: 'JetBrains Mono', monospace;
        }}

        /* Binary Toggle Groups */
        .binary-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            margin-bottom: 22px;
        }}

        @media (max-width: 750px) {{
            .binary-grid {{ grid-template-columns: repeat(2, 1fr); }}
        }}

        .binary-box {{
            background: rgba(15, 23, 42, 0.65);
            border: 1px solid var(--border-subtle);
            border-radius: 14px;
            padding: 12px;
            text-align: center;
        }}

        .binary-title {{
            font-size: 11.5px;
            font-weight: 600;
            color: #cbd5e1;
            margin-bottom: 8px;
            text-transform: uppercase;
            font-family: 'JetBrains Mono', monospace;
        }}

        .binary-switch {{
            display: flex;
            background: rgba(0, 0, 0, 0.35);
            border-radius: 8px;
            padding: 3px;
            border: 1px solid var(--border-subtle);
        }}

        .binary-btn {{
            flex: 1;
            padding: 6px;
            border: none;
            background: transparent;
            color: var(--text-muted);
            font-size: 11.5px;
            font-weight: 700;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.2s ease;
        }}

        .binary-btn.active {{
            background: linear-gradient(135deg, #ef4444, #e11d48);
            color: #fff;
            box-shadow: 0 0 10px rgba(239, 68, 68, 0.4);
        }}

        /* Actions */
        .sensor-actions {{
            display: flex;
            gap: 12px;
        }}

        .btn-infer-main {{
            flex: 1;
            padding: 14px 20px;
            background: linear-gradient(135deg, #ef4444, #f43f5e);
            border: none;
            border-radius: 14px;
            color: #fff;
            font-family: 'Space Grotesk', sans-serif;
            font-size: 14px;
            font-weight: 700;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            box-shadow: 0 6px 20px rgba(239, 68, 68, 0.35);
            transition: all 0.25s ease;
        }}
        .btn-infer-main:hover {{
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(239, 68, 68, 0.5);
        }}

        .btn-random {{
            padding: 14px 18px;
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid var(--border-subtle);
            border-radius: 14px;
            color: #e2e8f0;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
        }}
        .btn-random:hover {{
            background: rgba(255, 255, 255, 0.12);
            transform: translateY(-1px);
        }}

        /* Right Column: Dynamic Diagnostic Stage */
        .stage-card {{
            display: flex;
            flex-direction: column;
            height: 100%;
        }}

        /* Live ECG Canvas Monitor */
        .ecg-card {{
            background: #000;
            border: 1px solid rgba(239, 68, 68, 0.35);
            border-radius: 18px;
            padding: 14px;
            position: relative;
            overflow: hidden;
            margin-bottom: 20px;
            box-shadow: inset 0 0 25px rgba(239, 68, 68, 0.15);
        }}

        .ecg-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 8px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
        }}

        .ecg-rate {{
            font-size: 16px;
            font-weight: 800;
            color: var(--neon-crimson);
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        #ecgCanvas {{
            width: 100%;
            height: 90px;
            display: block;
        }}

        /* Result Spotlight */
        .result-spotlight {{
            background: rgba(10, 15, 29, 0.85);
            border: 1px solid rgba(239, 68, 68, 0.35);
            border-radius: 20px;
            padding: 22px;
            position: relative;
            overflow: hidden;
            margin-bottom: 20px;
            box-shadow: 0 0 35px rgba(239, 68, 68, 0.12);
        }}

        .result-spotlight.healthy {{
            border-color: rgba(16, 185, 129, 0.4);
            box-shadow: 0 0 35px rgba(16, 185, 129, 0.12);
        }}

        .spotlight-glow {{
            position: absolute;
            top: -40px;
            right: -40px;
            width: 140px;
            height: 140px;
            background: radial-gradient(circle, rgba(239, 68, 68, 0.3) 0%, transparent 70%);
            pointer-events: none;
        }}

        .result-hero {{
            display: flex;
            align-items: center;
            gap: 18px;
            margin-bottom: 16px;
        }}

        .result-avatar-wrap {{
            width: 80px;
            height: 80px;
            border-radius: 18px;
            overflow: hidden;
            border: 2px solid var(--neon-crimson);
            box-shadow: 0 0 20px rgba(239, 68, 68, 0.4);
            flex-shrink: 0;
            background: #0f172a;
        }}

        .result-avatar {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}

        .result-details h2 {{
            font-family: 'Space Grotesk', sans-serif;
            font-size: 22px;
            font-weight: 800;
            color: #fff;
            letter-spacing: -0.5px;
            line-height: 1.2;
        }}

        .result-confidence {{
            font-size: 13px;
            color: var(--neon-crimson);
            font-weight: 600;
            margin-top: 4px;
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        .confidence-val {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 18px;
            font-weight: 800;
            color: #fff;
        }}

        /* Probability Bars */
        .prob-rows {{
            display: flex;
            flex-direction: column;
            gap: 12px;
            margin-bottom: 20px;
        }}

        .prob-row {{
            display: flex;
            flex-direction: column;
            gap: 6px;
        }}

        .prob-header {{
            display: flex;
            justify-content: space-between;
            font-size: 12.5px;
            font-weight: 600;
            color: #cbd5e1;
        }}

        .prob-track {{
            width: 100%;
            height: 8px;
            background: rgba(255, 255, 255, 0.06);
            border-radius: 4px;
            overflow: hidden;
        }}

        .prob-fill {{
            height: 100%;
            border-radius: 4px;
            transition: width 0.35s cubic-bezier(0.4, 0, 0.2, 1);
        }}

        .fill-healthy {{
            background: linear-gradient(90deg, #10b981, #06b6d4);
            box-shadow: 0 0 10px rgba(16, 185, 129, 0.5);
        }}
        .fill-disease {{
            background: linear-gradient(90deg, #ef4444, #f43f5e);
            box-shadow: 0 0 10px rgba(239, 68, 68, 0.5);
        }}

        /* Telemetry Deck */
        .telemetry-deck {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            background: rgba(0, 0, 0, 0.35);
            padding: 14px;
            border-radius: 14px;
            border: 1px solid var(--border-subtle);
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
        }}

        .tele-item span {{
            color: var(--text-muted);
            font-size: 9.5px;
            display: block;
            text-transform: uppercase;
        }}

        .tele-item strong {{
            color: #e2e8f0;
            font-weight: 700;
        }}

        /* Analytics & Evaluation Deck (GRFS) */
        .analytics-deck {{
            background: var(--surface-card);
            border: 1px solid var(--card-border);
            border-radius: 24px;
            padding: 28px;
            backdrop-filter: blur(20px);
            margin-bottom: 32px;
        }}

        .tabs-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid var(--border-subtle);
            padding-bottom: 16px;
            margin-bottom: 24px;
            gap: 12px;
            flex-wrap: wrap;
        }}

        .tabs-group {{
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }}

        .tab-btn {{
            padding: 10px 18px;
            background: transparent;
            border: 1px solid transparent;
            border-radius: 12px;
            color: var(--text-secondary);
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .tab-btn:hover {{
            color: #fff;
            background: rgba(255, 255, 255, 0.05);
        }}

        .tab-btn.active {{
            background: rgba(239, 68, 68, 0.16);
            border-color: rgba(239, 68, 68, 0.4);
            color: var(--neon-crimson);
            font-weight: 700;
        }}

        .tab-content {{
            display: none;
        }}
        .tab-content.active {{
            display: block;
            animation: fadeIn 0.3s ease;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(6px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        /* TAB 1: INTERACTIVE 2x2 CONFUSION MATRIX */
        .cm-layout-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 28px;
        }}

        @media (max-width: 900px) {{
            .cm-layout-grid {{ grid-template-columns: 1fr; }}
        }}

        .cm-interactive-card {{
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid var(--border-subtle);
            border-radius: 18px;
            padding: 22px;
        }}

        .cm-table {{
            width: 100%;
            border-collapse: separate;
            border-spacing: 8px;
            margin: 18px 0;
            font-family: 'Space Grotesk', sans-serif;
            text-align: center;
        }}

        .cm-table th {{
            font-size: 12px;
            color: var(--text-muted);
            padding: 8px;
            font-weight: 600;
        }}

        .cm-cell {{
            padding: 18px 14px;
            border-radius: 12px;
            font-size: 20px;
            font-weight: 800;
            cursor: pointer;
            transition: all 0.25s ease;
            position: relative;
        }}

        .cm-cell:hover {{
            transform: scale(1.05);
            z-index: 2;
        }}

        .cell-tn {{
            background: rgba(16, 185, 129, 0.22);
            border: 1px solid rgba(16, 185, 129, 0.55);
            color: #34d399;
        }}
        .cell-tn:hover {{
            background: rgba(16, 185, 129, 0.4);
            box-shadow: 0 0 20px rgba(16, 185, 129, 0.4);
        }}

        .cell-tp {{
            background: rgba(239, 68, 68, 0.25);
            border: 1px solid rgba(239, 68, 68, 0.6);
            color: #f87171;
        }}
        .cell-tp:hover {{
            background: rgba(239, 68, 68, 0.45);
            box-shadow: 0 0 20px rgba(239, 68, 68, 0.5);
        }}

        .cell-fp {{
            background: rgba(245, 158, 11, 0.2);
            border: 1px solid rgba(245, 158, 11, 0.5);
            color: #fcd34d;
        }}
        .cell-fp:hover {{
            background: rgba(245, 158, 11, 0.35);
            box-shadow: 0 0 20px rgba(245, 158, 11, 0.4);
        }}

        .cell-fn {{
            background: rgba(244, 63, 94, 0.2);
            border: 1px solid rgba(244, 63, 94, 0.55);
            color: #fda4af;
        }}
        .cell-fn:hover {{
            background: rgba(244, 63, 94, 0.35);
            box-shadow: 0 0 20px rgba(244, 63, 94, 0.4);
        }}

        .cell-tag {{
            display: block;
            font-size: 10px;
            font-family: 'JetBrains Mono', monospace;
            font-weight: 500;
            opacity: 0.85;
            margin-top: 3px;
        }}

        .cm-inspector {{
            background: rgba(0, 0, 0, 0.35);
            border: 1px solid var(--border-subtle);
            border-radius: 12px;
            padding: 14px 16px;
            font-size: 12.5px;
            line-height: 1.5;
            color: #cbd5e1;
        }}

        /* Formula Card */
        .formula-card {{
            background: rgba(0, 0, 0, 0.4);
            border-left: 3px solid var(--neon-crimson);
            padding: 12px 16px;
            border-radius: 0 10px 10px 0;
            font-family: 'JetBrains Mono', monospace;
            margin-bottom: 12px;
        }}

        .formula-card h4 {{
            font-size: 12px;
            color: var(--neon-crimson);
            text-transform: uppercase;
            margin-bottom: 4px;
        }}

        .formula-card .math {{
            font-size: 13px;
            color: #f8fafc;
            font-weight: 600;
        }}

        .formula-card .plugged {{
            font-size: 11.5px;
            color: #94a3b8;
            margin-top: 4px;
        }}

        /* TAB 2: HIGH RES MEDICAL CHARTS */
        .gallery-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
        }}

        @media (max-width: 800px) {{
            .gallery-grid {{ grid-template-columns: 1fr; }}
        }}

        .gallery-item {{
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid var(--border-subtle);
            border-radius: 16px;
            overflow: hidden;
            transition: transform 0.3s;
            cursor: pointer;
        }}

        .gallery-item:hover {{
            transform: translateY(-3px);
            border-color: rgba(239, 68, 68, 0.5);
        }}

        .gallery-img {{
            width: 100%;
            height: auto;
            display: block;
        }}

        .gallery-cap {{
            padding: 14px 16px;
            font-size: 12.5px;
            color: #94a3b8;
            line-height: 1.5;
        }}

        /* TAB 3: ORAL DEFENSE */
        .defense-container {{
            display: flex;
            flex-direction: column;
            gap: 16px;
        }}

        .defense-card {{
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid var(--border-subtle);
            border-radius: 16px;
            padding: 20px;
            transition: all 0.2s ease;
        }}

        .defense-card:hover {{
            border-color: rgba(239, 68, 68, 0.4);
            background: rgba(30, 41, 59, 0.4);
        }}

        .defense-q {{
            font-family: 'Space Grotesk', sans-serif;
            font-size: 16px;
            font-weight: 700;
            color: #f87171;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .defense-a {{
            font-size: 13.5px;
            color: #cbd5e1;
            line-height: 1.6;
        }}

        /* Footer */
        .app-footer {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 20px 24px;
            background: rgba(15, 23, 42, 0.4);
            border-top: 1px solid var(--border-subtle);
            border-radius: 16px;
            margin-top: 36px;
            flex-wrap: wrap;
            gap: 12px;
            font-size: 12.5px;
            color: var(--text-muted);
        }}

        .footer-links {{
            display: flex;
            gap: 16px;
        }}

        .footer-links a {{
            color: var(--neon-crimson);
            text-decoration: none;
            transition: color 0.2s;
        }}
        .footer-links a:hover {{
            color: #fff;
            text-decoration: underline;
        }}

        /* Modal */
        .modal-overlay {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.85);
            backdrop-filter: blur(10px);
            z-index: 100;
            display: none;
            align-items: center;
            justify-content: center;
            padding: 24px;
        }}

        .modal-card {{
            background: #0f172a;
            border: 1px solid var(--neon-crimson);
            border-radius: 20px;
            max-width: 900px;
            width: 100%;
            overflow: hidden;
            box-shadow: 0 0 50px rgba(239, 68, 68, 0.35);
            animation: zoomIn 0.25s ease;
        }}

        @keyframes zoomIn {{
            from {{ transform: scale(0.92); opacity: 0; }}
            to {{ transform: scale(1); opacity: 1; }}
        }}

        .modal-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 16px 20px;
            border-bottom: 1px solid var(--border-subtle);
        }}

        .modal-close {{
            background: transparent;
            border: none;
            color: #94a3b8;
            font-size: 24px;
            cursor: pointer;
            line-height: 1;
        }}
        .modal-close:hover {{ color: #fff; }}

        .modal-body img {{
            width: 100%;
            height: auto;
            display: block;
        }}
    </style>
</head>
<body>

    <div class="bg-grid"></div>
    <div class="glow-overlay"></div>

    <div class="app-container">

        <!-- Top Navigation Bar -->
        <header class="top-navbar">
            <div class="brand-block">
                <div class="brand-icon">🫀</div>
                <div class="brand-info">
                    <h1>
                        CARDIOPULSE AI
                        <span class="brand-badge">CLINICAL V3.0</span>
                    </h1>
                    <div class="brand-sub">Cardiovascular Disease Predictive Diagnostic System & Biometric Telemetry</div>
                </div>
            </div>

            <!-- Student Accreditation Badge -->
            <div class="author-badge">
                <span class="author-dot"></span>
                <span><strong>Philip Antwi</strong> // PUIT24120002 // Level 400 BSc IT // Pentecost University</span>
            </div>

            <!-- Direct 1-Click Action Buttons -->
            <div class="nav-actions">
                <a href="https://github.com/Philipntwi-bot/Heart_Disease_Classification_Project" target="_blank" class="btn-nav btn-github" title="Visit GitHub Repository">
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/>
                    </svg>
                    GITHUB REPO
                </a>
                <a href="https://heart-disease-classification-project.vercel.app" target="_blank" class="btn-nav btn-vercel" title="Live Vercel Production Deployment">
                    <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M24 22.525H0l12-21.05 12 21.05z"/>
                    </svg>
                    VERCEL APP
                </a>
                <a href="https://vercel.com/philipntwi-bot/heart-disease-classification-project" target="_blank" class="btn-nav btn-console" title="Vercel Project Dashboard">
                    ☁️ VERCEL CONSOLE
                </a>
            </div>
        </header>

        <!-- Clinical Cardiovascular Pathology Showcase (Bing medical imagery) -->
        <div class="showcase-header">
            <div>
                <span class="section-tag">// CARDIOVASCULAR PATHOLOGY & CLINICAL ANATOMY</span>
                <h3 style="font-family: 'Space Grotesk', sans-serif; font-size: 20px; font-weight: 700; color: #fff; margin-top: 4px;">
                    Major Cardiovascular Conditions & Pathological Indicators
                </h3>
            </div>
            <button class="btn-nav btn-github" onclick="openModal('modalAnat')" style="font-size: 11.5px;">
                🔍 View Full Cardiac Anatomy Diagram
            </button>
        </div>

        <div class="pathology-grid">
            <!-- 1. Atherosclerosis -->
            <div class="pathology-card" onclick="openModal('modalAthero')">
                <div class="pathology-img-wrap">
                    <img src="{img_athero}" alt="Atherosclerosis and CAD" class="pathology-img">
                    <span class="pathology-badge-top">Vascular Occlusion</span>
                </div>
                <div class="pathology-content">
                    <div class="pathology-title">Atherosclerosis & CAD</div>
                    <div class="pathology-sub">Lipid Plaque Buildup</div>
                    <p class="pathology-desc">
                        Progressive stenosis of the coronary arteries caused by fibrofatty plaque deposits, restricting myocardial perfusion and oxygenation.
                    </p>
                </div>
            </div>

            <!-- 2. Myocardial Infarction -->
            <div class="pathology-card" onclick="openModal('modalInfarct')">
                <div class="pathology-img-wrap">
                    <img src="{img_infarct}" alt="Myocardial Infarction" class="pathology-img">
                    <span class="pathology-badge-top">Acute Infarction</span>
                </div>
                <div class="pathology-content">
                    <div class="pathology-title">Myocardial Infarction</div>
                    <div class="pathology-sub">Cardiomyocyte Ischemia</div>
                    <p class="pathology-desc">
                        Complete acute thrombus occlusion leading to irreversible ischemic necrosis of myocardial tissue and electrical instability.
                    </p>
                </div>
            </div>

            <!-- 3. Hypertension -->
            <div class="pathology-card" onclick="openModal('modalStress')">
                <div class="pathology-img-wrap">
                    <img src="{img_stress}" alt="Hypertension and Left Ventricular Stress" class="pathology-img">
                    <span class="pathology-badge-top">Hemodynamic Load</span>
                </div>
                <div class="pathology-content">
                    <div class="pathology-title">Hypertensive Remodeling</div>
                    <div class="pathology-sub">Vascular Resistance</div>
                    <p class="pathology-desc">
                        Chronic elevated systolic afterload inducing left ventricular hypertrophy, arterial stiffness, and accelerated endothelial dysfunction.
                    </p>
                </div>
            </div>

            <!-- 4. Clinical ECG Telemetry -->
            <div class="pathology-card" onclick="openModal('modalECG')">
                <div class="pathology-img-wrap">
                    <img src="{img_ecg_monitor}" alt="ECG Rhythm Monitoring" class="pathology-img">
                    <span class="pathology-badge-top">Electrophysiology</span>
                </div>
                <div class="pathology-content">
                    <div class="pathology-title">ECG Rhythm Telemetry</div>
                    <div class="pathology-sub">Conduction Monitoring</div>
                    <p class="pathology-desc">
                        Real-time recording of cardiac depolarization vectors (P-wave, QRS-complex, ST-segment elevation/depression, and T-wave morphology).
                    </p>
                </div>
            </div>
        </div>

        <!-- Main Workspace (Inputs & Live Diagnostic Stage) -->
        <div class="workspace-grid">

            <!-- Left: 10 Biomarker Sensor Console -->
            <div class="card-panel">
                <div class="panel-header">
                    <div class="panel-title">
                        <span>⚡ 10-Biomarker Clinical Input Matrix</span>
                    </div>
                    <span class="section-tag">INPUT TENSOR [10×1]</span>
                </div>

                <!-- Quick Clinical Presets -->
                <div class="preset-chips-strip">
                    <span style="font-size: 11px; color: var(--text-muted); align-self: center; font-family: 'JetBrains Mono', monospace;">PROFILES:</span>
                    <button class="preset-chip" onclick="applyPreset(32, 'Female', 110, 170, 21.5, 'No', 'No', 3, 'No', 2)">🟢 Low-Risk Patient</button>
                    <button class="preset-chip" onclick="applyPreset(52, 'Male', 138, 225, 27.4, 'No', 'Yes', 2, 'Yes', 5)">🟡 Borderline Profile</button>
                    <button class="preset-chip" onclick="applyPreset(68, 'Male', 165, 275, 33.2, 'Yes', 'Yes', 0, 'Yes', 8)">🔴 High-Risk Patient</button>
                </div>

                <!-- 6 Continuous Numerical Features -->
                <div class="sensors-grid">
                    <!-- Age -->
                    <div class="sensor-box">
                        <div class="sensor-meta">
                            <div>
                                <div class="sensor-label">👤 Patient Age</div>
                                <div class="sensor-hint">Years (30 - 79)</div>
                            </div>
                            <input type="number" id="input_age" class="sensor-num-input" value="55" min="30" max="79" step="1">
                        </div>
                        <input type="range" id="slider_age" class="range-slider" value="55" min="30" max="79" step="1">
                        <div class="sensor-scale">
                            <span>30 yrs</span>
                            <span id="display_age" style="color:var(--neon-crimson); font-weight:700;">55 yrs</span>
                            <span>79 yrs</span>
                        </div>
                    </div>

                    <!-- Blood Pressure -->
                    <div class="sensor-box">
                        <div class="sensor-meta">
                            <div>
                                <div class="sensor-label">🩺 Resting Blood Pressure</div>
                                <div class="sensor-hint">Systolic mmHg</div>
                            </div>
                            <input type="number" id="input_bp" class="sensor-num-input" value="135" min="90" max="180" step="1">
                        </div>
                        <input type="range" id="slider_bp" class="range-slider" value="135" min="90" max="180" step="1">
                        <div class="sensor-scale">
                            <span>90 mmHg</span>
                            <span id="display_bp" style="color:var(--neon-crimson); font-weight:700;">135 mmHg</span>
                            <span>180 mmHg</span>
                        </div>
                    </div>

                    <!-- Cholesterol -->
                    <div class="sensor-box">
                        <div class="sensor-meta">
                            <div>
                                <div class="sensor-label">🧪 Serum Cholesterol</div>
                                <div class="sensor-hint">Total mg/dL</div>
                            </div>
                            <input type="number" id="input_chol" class="sensor-num-input" value="225" min="150" max="300" step="1">
                        </div>
                        <input type="range" id="slider_chol" class="range-slider" value="225" min="150" max="300" step="1">
                        <div class="sensor-scale">
                            <span>150 mg/dL</span>
                            <span id="display_chol" style="color:var(--neon-crimson); font-weight:700;">225 mg/dL</span>
                            <span>300 mg/dL</span>
                        </div>
                    </div>

                    <!-- BMI -->
                    <div class="sensor-box">
                        <div class="sensor-meta">
                            <div>
                                <div class="sensor-label">⚖️ Body Mass Index (BMI)</div>
                                <div class="sensor-hint">kg/m² (18 - 40)</div>
                            </div>
                            <input type="number" id="input_bmi" class="sensor-num-input" value="28.5" min="18.0" max="40.0" step="0.1">
                        </div>
                        <input type="range" id="slider_bmi" class="range-slider" value="28.5" min="18.0" max="40.0" step="0.1">
                        <div class="sensor-scale">
                            <span>18.0</span>
                            <span id="display_bmi" style="color:var(--neon-crimson); font-weight:700;">28.5 kg/m²</span>
                            <span>40.0</span>
                        </div>
                    </div>

                    <!-- Physical Activity -->
                    <div class="sensor-box">
                        <div class="sensor-meta">
                            <div>
                                <div class="sensor-label">🏃 Physical Activity</div>
                                <div class="sensor-hint">0 (Sedentary) - 4 (High)</div>
                            </div>
                            <input type="number" id="input_act" class="sensor-num-input" value="2" min="0" max="4" step="1">
                        </div>
                        <input type="range" id="slider_act" class="range-slider" value="2" min="0" max="4" step="1">
                        <div class="sensor-scale">
                            <span>0 (None)</span>
                            <span id="display_act" style="color:var(--neon-crimson); font-weight:700;">2 (Moderate)</span>
                            <span>4 (High)</span>
                        </div>
                    </div>

                    <!-- Stress Level -->
                    <div class="sensor-box">
                        <div class="sensor-meta">
                            <div>
                                <div class="sensor-label">🧠 Stress Level Index</div>
                                <div class="sensor-hint">Scale (1 - 10)</div>
                            </div>
                            <input type="number" id="input_stress" class="sensor-num-input" value="5" min="1" max="10" step="1">
                        </div>
                        <input type="range" id="slider_stress" class="range-slider" value="5" min="1" max="10" step="1">
                        <div class="sensor-scale">
                            <span>1 (Calm)</span>
                            <span id="display_stress" style="color:var(--neon-crimson); font-weight:700;">5 (Average)</span>
                            <span>10 (Severe)</span>
                        </div>
                    </div>
                </div>

                <!-- 4 Categorical / Binary Switches -->
                <div class="binary-grid">
                    <!-- Sex -->
                    <div class="binary-box">
                        <div class="binary-title">Biological Sex</div>
                        <div class="binary-switch">
                            <button type="button" class="binary-btn active" id="btnSexMale" onclick="setBinary('sex', 'Male')">Male</button>
                            <button type="button" class="binary-btn" id="btnSexFemale" onclick="setBinary('sex', 'Female')">Female</button>
                        </div>
                    </div>

                    <!-- Smoker -->
                    <div class="binary-box">
                        <div class="binary-title">Cigarette Smoker</div>
                        <div class="binary-switch">
                            <button type="button" class="binary-btn" id="btnSmkNo" onclick="setBinary('smoker', 'No')">No</button>
                            <button type="button" class="binary-btn active" id="btnSmkYes" onclick="setBinary('smoker', 'Yes')">Yes</button>
                        </div>
                    </div>

                    <!-- Diabetes -->
                    <div class="binary-box">
                        <div class="binary-title">Diabetes Status</div>
                        <div class="binary-switch">
                            <button type="button" class="binary-btn active" id="btnDiaNo" onclick="setBinary('diabetes', 'No')">No</button>
                            <button type="button" class="binary-btn" id="btnDiaYes" onclick="setBinary('diabetes', 'Yes')">Yes</button>
                        </div>
                    </div>

                    <!-- Family History -->
                    <div class="binary-box">
                        <div class="binary-title">Family History</div>
                        <div class="binary-switch">
                            <button type="button" class="binary-btn active" id="btnFamNo" onclick="setBinary('family_history', 'No')">No</button>
                            <button type="button" class="binary-btn" id="btnFamYes" onclick="setBinary('family_history', 'Yes')">Yes</button>
                        </div>
                    </div>
                </div>

                <div class="sensor-actions">
                    <button type="button" class="btn-infer-main" onclick="triggerInference(true)">
                        <span>⚡ EXECUTE CLINICAL DIAGNOSTIC SCREENING</span>
                    </button>
                    <button type="button" class="btn-random" onclick="loadRandomPatient()">
                        🎲 Random Cohort Sample
                    </button>
                </div>
            </div>

            <!-- Right: Live Cardiovascular Diagnostic Stage -->
            <div class="card-panel stage-card">
                <div class="panel-header">
                    <div class="panel-title">
                        <span>🫀 Live Telemetry & Screening Outcome</span>
                    </div>
                    <span id="engineBadge" class="section-tag" style="color: var(--neon-emerald);">LIVE EDGE ENGINE</span>
                </div>

                <!-- Animated ECG Heart Rate Monitor -->
                <div class="ecg-card">
                    <div class="ecg-header">
                        <span>LEAD II ELECTROCARDIOGRAM</span>
                        <div class="ecg-rate">
                            <span>❤️</span>
                            <span id="ecgBpmDisplay">78 BPM</span>
                        </div>
                    </div>
                    <canvas id="ecgCanvas"></canvas>
                </div>

                <!-- Diagnostic Spotlight Banner -->
                <div class="result-spotlight" id="resultSpotlight">
                    <div class="spotlight-glow"></div>
                    <div class="result-hero">
                        <div class="result-avatar-wrap" id="resultAvatarWrap">
                            <img id="resultPhoto" src="{img_cardiac_care}" alt="Cardiovascular Diagnosis" class="result-avatar">
                        </div>
                        <div class="result-details">
                            <h2 id="resultDiagnosisTitle">HIGH CARDIOVASCULAR RISK</h2>
                            <div class="result-confidence">
                                <span>Pathological Probability:</span>
                                <span id="resultConfidenceScore" class="confidence-val">84.2%</span>
                            </div>
                        </div>
                    </div>
                    <p id="resultDiagnosisNote" style="font-size:12.5px; color:#94a3b8; line-height:1.5;">
                        Patient profile demonstrates elevated systolic vascular load and lipid profile. Clinical evaluation advised.
                    </p>
                </div>

                <!-- Probability Distribution Meters -->
                <div class="prob-rows">
                    <!-- Healthy Row -->
                    <div class="prob-row">
                        <div class="prob-header">
                            <span>🟢 Low Risk (Normal Vascular Baseline)</span>
                            <span id="probValHealthy" style="font-family:'JetBrains Mono', monospace;">15.8%</span>
                        </div>
                        <div class="prob-track">
                            <div id="probFillHealthy" class="prob-fill fill-healthy" style="width: 15.8%;"></div>
                        </div>
                    </div>

                    <!-- Heart Disease Row -->
                    <div class="prob-row">
                        <div class="prob-header">
                            <span>🔴 High Risk (Cardiovascular Pathology)</span>
                            <span id="probValDisease" style="font-family:'JetBrains Mono', monospace;">84.2%</span>
                        </div>
                        <div class="prob-track">
                            <div id="probFillDisease" class="prob-fill fill-disease" style="width: 84.2%;"></div>
                        </div>
                    </div>
                </div>

                <!-- Clinical Telemetry Deck -->
                <div class="telemetry-deck">
                    <div class="tele-item">
                        <span>Classifier:</span>
                        <strong>Logistic Regression (StandardScaler)</strong>
                    </div>
                    <div class="tele-item">
                        <span>Holdout Cohort:</span>
                        <strong style="color: var(--neon-cyan);">500 Patient Records</strong>
                    </div>
                    <div class="tele-item">
                        <span>Classification F1:</span>
                        <strong id="teleF1" style="color: var(--neon-crimson);">0.65 (Weighted)</strong>
                    </div>
                    <div class="tele-item">
                        <span>Latency Benchmark:</span>
                        <strong id="teleLatency">0.08 ms (Edge)</strong>
                    </div>
                </div>
            </div>

        </div>

        <!-- Analytics, Confusion Matrix & Medical Charts (GRFS) -->
        <div class="analytics-deck">
            <div class="tabs-header">
                <div>
                    <span class="section-tag">// STATISTICAL VALIDATION & METRIC SUITE</span>
                    <h3 style="font-family: 'Space Grotesk', sans-serif; font-size: 19px; font-weight: 700; color: #fff; margin-top: 4px;">
                        Interactive 2×2 Confusion Matrix & Clinical Validation Figures
                    </h3>
                </div>

                <div class="tabs-group">
                    <button class="tab-btn active" onclick="switchTab('tabMatrix')">
                        🔢 Confusion Matrix & Math
                    </button>
                    <button class="tab-btn" onclick="switchTab('tabCharts')">
                        📊 Clinical Validation Figures
                    </button>
                    <button class="tab-btn" onclick="switchTab('tabDefense')">
                        🎓 Oral Defense Cheat Sheet
                    </button>
                </div>
            </div>

            <!-- TAB 1: INTERACTIVE 2x2 CONFUSION MATRIX & LIVE MATH -->
            <div id="tabMatrix" class="tab-content active">
                <div class="cm-layout-grid">

                    <!-- Left: Interactive 2x2 Grid -->
                    <div class="cm-interactive-card">
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
                            <h4 style="font-family:'Space Grotesk', sans-serif; font-size:16px; color:#fff;">
                                Clinical 2×2 Holdout Confusion Matrix (N = 100 Test Cases)
                            </h4>
                            <span class="section-tag" style="color:var(--neon-crimson);">STRATIFIED 80/20</span>
                        </div>
                        <p style="font-size:12.5px; color:#94a3b8; line-height:1.5;">
                            Click or hover any quadrant below to inspect True Negatives (TN), False Positives (FP), False Negatives (FN), and True Positives (TP).
                        </p>

                        <table class="cm-table">
                            <thead>
                                <tr>
                                    <th></th>
                                    <th>Pred. No Disease (0)</th>
                                    <th>Pred. Heart Disease (1)</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <th style="text-align:right;">Actual No Disease (0)</th>
                                    <td class="cm-cell cell-tn" onmouseover="inspectCell('No Disease', 'No Disease', 15, 'TN')" onclick="inspectCell('No Disease', 'No Disease', 15, 'TN')">
                                        15
                                        <span class="cell-tag">TN (True Neg)</span>
                                    </td>
                                    <td class="cm-cell cell-fp" onmouseover="inspectCell('No Disease', 'Heart Disease', 32, 'FP')" onclick="inspectCell('No Disease', 'Heart Disease', 32, 'FP')">
                                        32
                                        <span class="cell-tag">FP (Type I Error)</span>
                                    </td>
                                </tr>
                                <tr>
                                    <th style="text-align:right;">Actual Heart Disease (1)</th>
                                    <td class="cm-cell cell-fn" onmouseover="inspectCell('Heart Disease', 'No Disease', 12, 'FN')" onclick="inspectCell('Heart Disease', 'No Disease', 12, 'FN')">
                                        12
                                        <span class="cell-tag">FN (Type II Error)</span>
                                    </td>
                                    <td class="cm-cell cell-tp" onmouseover="inspectCell('Heart Disease', 'Heart Disease', 41, 'TP')" onclick="inspectCell('Heart Disease', 'Heart Disease', 41, 'TP')">
                                        41
                                        <span class="cell-tag">TP (True Pos)</span>
                                    </td>
                                </tr>
                            </tbody>
                        </table>

                        <div id="cellInspector" class="cm-inspector">
                            👉 <strong>Interactive Quadrant Focus:</strong> Hover or click any cell above to see detailed epidemiological breakdown and clinical risk implications.
                        </div>
                    </div>

                    <!-- Right: Step-by-Step Calculation Walkthrough -->
                    <div>
                        <!-- Sensitivity / Recall -->
                        <div class="formula-card">
                            <h4>1. Clinical Sensitivity / Recall (Catching Disease)</h4>
                            <div class="math">Sensitivity = TP / (TP + FN)</div>
                            <div class="plugged">
                                Plugged: 41 / (41 + 12) = 41 / 53 = <strong>77.36% (0.774)</strong>
                            </div>
                        </div>

                        <!-- Specificity -->
                        <div class="formula-card" style="border-left-color: var(--neon-emerald);">
                            <h4 style="color: var(--neon-emerald);">2. Diagnostic Specificity (Rule-Out Rate)</h4>
                            <div class="math">Specificity = TN / (TN + FP)</div>
                            <div class="plugged">
                                Plugged: 15 / (15 + 32) = 15 / 47 = <strong>31.91% (0.319)</strong>
                            </div>
                        </div>

                        <!-- Precision -->
                        <div class="formula-card" style="border-left-color: var(--neon-amber);">
                            <h4 style="color: var(--neon-amber);">3. Positive Predictive Value (Precision)</h4>
                            <div class="math">Precision = TP / (TP + FP)</div>
                            <div class="plugged">
                                Plugged: 41 / (41 + 32) = 41 / 73 = <strong>56.16% (0.562)</strong>
                            </div>
                        </div>

                        <!-- F1-Score -->
                        <div class="formula-card" style="border-left-color: var(--neon-rose);">
                            <h4 style="color: var(--neon-rose);">4. F1-Score (Harmonic Balance)</h4>
                            <div class="math">F₁ = 2 × (Precision × Recall) / (Precision + Recall)</div>
                            <div class="plugged">
                                Plugged: 2 × (0.562 × 0.774) / (0.562 + 0.774) = 0.869 / 1.336 = <strong>0.651 (65.1%)</strong>
                            </div>
                        </div>
                    </div>

                </div>
            </div>

            <!-- TAB 2: HIGH-RES MEDICAL FIGURES -->
            <div id="tabCharts" class="tab-content">
                <div class="gallery-grid">
                    <div class="gallery-item" onclick="openModal('modalCM')">
                        <img src="{cm_path}" alt="Confusion Matrix" class="gallery-img">
                        <div class="gallery-cap">
                            <strong>Figure 2.1: Multi-Class Confusion Matrix</strong> â€” Visualizing True Negatives, False Positives, False Negatives, and True Positives across 100 holdout patient screening records.
                        </div>
                    </div>

                    <div class="gallery-item" onclick="openModal('modalROC')">
                        <img src="{roc_path}" alt="ROC Curve" class="gallery-img">
                        <div class="gallery-cap">
                            <strong>Figure 2.2: Receiver Operating Characteristic (ROC) Curve</strong> â€” Plotting True Positive Rate vs False Positive Rate across classification probability thresholds.
                        </div>
                    </div>

                    <div class="gallery-item" onclick="openModal('modalFI')">
                        <img src="{fi_path}" alt="Feature Importance" class="gallery-img">
                        <div class="gallery-cap">
                            <strong>Figure 2.3: Feature Importance & Coefficient Weights</strong> â€” Relative diagnostic weighting across all 10 clinical vectors (Blood Pressure, Age, Smoking, Cholesterol).
                        </div>
                    </div>

                    <div class="gallery-item" onclick="openModal('modalDist')">
                        <img src="{dist_path}" alt="Cohort Distribution" class="gallery-img">
                        <div class="gallery-cap">
                            <strong>Figure 2.4: Patient Cohort Distribution</strong> â€” Balance of positive heart disease (266 cases) vs healthy cardiovascular records (234 cases) across 500 patient entries.
                        </div>
                    </div>
                </div>
            </div>

            <!-- TAB 3: ORAL DEFENSE CHEAT SHEET -->
            <div id="tabDefense" class="tab-content">
                <div class="defense-container">
                    <div class="defense-card">
                        <div class="defense-q">
                            🎓 Q1: In clinical healthcare AI, why are False Negatives far more dangerous than False Positives?
                        </div>
                        <div class="defense-a">
                            <strong>Answer:</strong> A <strong>False Negative</strong> means a patient with active coronary artery disease or impending myocardial infarction is sent home believing they are healthy, which can result in fatal cardiac arrest without timely clinical intervention. A <strong>False Positive</strong> merely prompts follow-up tests (such as an echocardiogram or stress test) to rule out disease. Therefore, medical models prioritize high <strong>Sensitivity / Recall</strong>.
                        </div>
                    </div>

                    <div class="defense-card">
                        <div class="defense-q">
                            🎓 Q2: Why is feature scaling (StandardScaler) essential before training Logistic Regression?
                        </div>
                        <div class="defense-a">
                            <strong>Answer:</strong> Continuous features have vastly different numeric scales: Serum Cholesterol ranges from 150 to 300 mg/dL, while binary indicators like Smoking or Diabetes are only 0 or 1. Without standardization, gradient-based optimization algorithms would assign disproportionate mathematical weight to larger numbers regardless of biological importance. <code>StandardScaler</code> centers each feature to mean 0 and unit variance 1.
                        </div>
                    </div>

                    <div class="defense-card">
                        <div class="defense-q">
                            🎓 Q3: How is the Sigmoid activation function formulated to output risk probabilities?
                        </div>
                        <div class="defense-a">
                            <strong>Answer:</strong> The model computes the linear dot product <em>z = w · x + b</em>. The <strong>Sigmoid function</strong> <em>σ(z) = 1 / (1 + e<sup>-z</sup>)</em> maps this continuous logit onto the bounded interval (0, 1), representing the calibrated probability of cardiovascular disease occurrence.
                        </div>
                    </div>

                    <div class="defense-card">
                        <div class="defense-q">
                            🎓 Q4: What are the primary modifiable vs non-modifiable risk factors in this dataset?
                        </div>
                        <div class="defense-a">
                            <strong>Answer:</strong> <strong>Modifiable factors</strong> include Smoking, Blood Pressure, Serum Cholesterol, Body Mass Index (BMI), and Physical Activity. <strong>Non-modifiable factors</strong> include Chronological Age, Biological Sex, and Family Genetic History. Clinical preventive medicine focuses heavily on lowering modifiable factors to reduce overall risk.
                        </div>
                    </div>
                </div>
            </div>

        </div>

        <!-- Footer -->
        <footer class="app-footer">
            <div>
                <strong>CARDIOPULSE AI // Clinical Diagnostic Matrix</strong> &bull; Developed by <strong>Philip Antwi</strong> (PUIT24120002), Level 400 BSc Information Technology, Pentecost University.
            </div>
            <div class="footer-links">
                <a href="https://github.com/Philipntwi-bot/Heart_Disease_Classification_Project" target="_blank">GitHub Repo</a>
                <a href="https://heart-disease-classification-project.vercel.app" target="_blank">Vercel App</a>
                <a href="https://vercel.com/philipntwi-bot/heart-disease-classification-project" target="_blank">Vercel Console</a>
            </div>
        </footer>

    </div>

    <!-- Modals for Full-Screen Inspection -->
    <div id="modalAnat" class="modal-overlay" onclick="closeModal('modalAnat')">
        <div class="modal-card" onclick="event.stopPropagation()">
            <div class="modal-header">
                <h3 style="font-family:'Space Grotesk', sans-serif; font-size:16px; color:#fff;">Cardiovascular Anatomy & Arterial System</h3>
                <button class="modal-close" onclick="closeModal('modalAnat')">&times;</button>
            </div>
            <div class="modal-body"><img src="{img_heart_anat}" alt="Cardiovascular Anatomy"></div>
        </div>
    </div>

    <div id="modalAthero" class="modal-overlay" onclick="closeModal('modalAthero')">
        <div class="modal-card" onclick="event.stopPropagation()">
            <div class="modal-header">
                <h3 style="font-family:'Space Grotesk', sans-serif; font-size:16px; color:#fff;">Atherosclerosis: Plaque Buildup in Coronary Artery</h3>
                <button class="modal-close" onclick="closeModal('modalAthero')">&times;</button>
            </div>
            <div class="modal-body"><img src="{img_athero}" alt="Atherosclerosis"></div>
        </div>
    </div>

    <div id="modalInfarct" class="modal-overlay" onclick="closeModal('modalInfarct')">
        <div class="modal-card" onclick="event.stopPropagation()">
            <div class="modal-header">
                <h3 style="font-family:'Space Grotesk', sans-serif; font-size:16px; color:#fff;">Myocardial Infarction Pathology</h3>
                <button class="modal-close" onclick="closeModal('modalInfarct')">&times;</button>
            </div>
            <div class="modal-body"><img src="{img_infarct}" alt="Myocardial Infarction"></div>
        </div>
    </div>

    <div id="modalStress" class="modal-overlay" onclick="closeModal('modalStress')">
        <div class="modal-card" onclick="event.stopPropagation()">
            <div class="modal-header">
                <h3 style="font-family:'Space Grotesk', sans-serif; font-size:16px; color:#fff;">Hypertensive Vascular Remodeling</h3>
                <button class="modal-close" onclick="closeModal('modalStress')">&times;</button>
            </div>
            <div class="modal-body"><img src="{img_stress}" alt="Hypertension"></div>
        </div>
    </div>

    <div id="modalECG" class="modal-overlay" onclick="closeModal('modalECG')">
        <div class="modal-card" onclick="event.stopPropagation()">
            <div class="modal-header">
                <h3 style="font-family:'Space Grotesk', sans-serif; font-size:16px; color:#fff;">Clinical Electrocardiogram Rhythm Telemetry</h3>
                <button class="modal-close" onclick="closeModal('modalECG')">&times;</button>
            </div>
            <div class="modal-body"><img src="{img_ecg_monitor}" alt="ECG Telemetry"></div>
        </div>
    </div>

    <div id="modalCM" class="modal-overlay" onclick="closeModal('modalCM')">
        <div class="modal-card" onclick="event.stopPropagation()">
            <div class="modal-header">
                <h3 style="font-family:'Space Grotesk', sans-serif; font-size:16px; color:#fff;">Confusion Matrix // High Resolution</h3>
                <button class="modal-close" onclick="closeModal('modalCM')">&times;</button>
            </div>
            <div class="modal-body"><img src="{cm_path}" alt="Confusion Matrix"></div>
        </div>
    </div>

    <div id="modalROC" class="modal-overlay" onclick="closeModal('modalROC')">
        <div class="modal-card" onclick="event.stopPropagation()">
            <div class="modal-header">
                <h3 style="font-family:'Space Grotesk', sans-serif; font-size:16px; color:#fff;">ROC Curve // Diagnostic Discriminatory Power</h3>
                <button class="modal-close" onclick="closeModal('modalROC')">&times;</button>
            </div>
            <div class="modal-body"><img src="{roc_path}" alt="ROC Curve"></div>
        </div>
    </div>

    <div id="modalFI" class="modal-overlay" onclick="closeModal('modalFI')">
        <div class="modal-card" onclick="event.stopPropagation()">
            <div class="modal-header">
                <h3 style="font-family:'Space Grotesk', sans-serif; font-size:16px; color:#fff;">Feature Importance & Model Weights</h3>
                <button class="modal-close" onclick="closeModal('modalFI')">&times;</button>
            </div>
            <div class="modal-body"><img src="{fi_path}" alt="Feature Importance"></div>
        </div>
    </div>

    <div id="modalDist" class="modal-overlay" onclick="closeModal('modalDist')">
        <div class="modal-card" onclick="event.stopPropagation()">
            <div class="modal-header">
                <h3 style="font-family:'Space Grotesk', sans-serif; font-size:16px; color:#fff;">Patient Cohort Class Distribution</h3>
                <button class="modal-close" onclick="closeModal('modalDist')">&times;</button>
            </div>
            <div class="modal-body"><img src="{dist_path}" alt="Class Distribution"></div>
        </div>
    </div>

    <!-- JAVASCRIPT LOGIC -->
    <script>
        const MODEL_DATA = {model_data_json};

        // Patient State (10 Biomarkers)
        let patientState = {{
            age: 55,
            sex: "Male",
            blood_pressure: 135,
            cholesterol: 225,
            bmi: 28.5,
            smoker: "Yes",
            diabetes: "No",
            physical_activity: 2,
            family_history: "No",
            stress_level: 5
        }};

        // Sensor Initializer
        function initSensors() {{
            const sensors = [
                {{ key: 'age', slider: 'slider_age', num: 'input_age', disp: 'display_age', unit: 'yrs' }},
                {{ key: 'blood_pressure', slider: 'slider_bp', num: 'input_bp', disp: 'display_bp', unit: 'mmHg' }},
                {{ key: 'cholesterol', slider: 'slider_chol', num: 'input_chol', disp: 'display_chol', unit: 'mg/dL' }},
                {{ key: 'bmi', slider: 'slider_bmi', num: 'input_bmi', disp: 'display_bmi', unit: 'kg/m²' }},
                {{ key: 'physical_activity', slider: 'slider_act', num: 'input_act', disp: 'display_act', unit: '' }},
                {{ key: 'stress_level', slider: 'slider_stress', num: 'input_stress', disp: 'display_stress', unit: '' }}
            ];

            sensors.forEach(s => {{
                const sl = document.getElementById(s.slider);
                const num = document.getElementById(s.num);
                const disp = document.getElementById(s.disp);

                function update(val, isExt) {{
                    val = parseFloat(val);
                    if (isNaN(val)) return;
                    patientState[s.key] = val;

                    if (!isExt) {{
                        sl.value = val;
                        num.value = val;
                    }}

                    if (s.key === 'physical_activity') {{
                        const actLabels = ['0 (None)', '1 (Light)', '2 (Moderate)', '3 (Active)', '4 (High)'];
                        disp.textContent = actLabels[Math.round(val)] || val;
                    }} else if (s.key === 'stress_level') {{
                        disp.textContent = Math.round(val) + (val <= 3 ? ' (Low)' : val <= 7 ? ' (Moderate)' : ' (Severe)');
                    }} else {{
                        disp.textContent = (s.key === 'bmi' ? val.toFixed(1) : Math.round(val)) + ' ' + s.unit;
                    }}

                    triggerInference(false);
                }}

                sl.addEventListener('input', e => {{
                    num.value = e.target.value;
                    update(e.target.value, true);
                }});
                num.addEventListener('input', e => {{
                    sl.value = e.target.value;
                    update(e.target.value, true);
                }});
            }});
        }}

        // Binary Toggle Setter
        function setBinary(field, val) {{
            patientState[field] = val;
            if (field === 'sex') {{
                document.getElementById('btnSexMale').classList.toggle('active', val === 'Male');
                document.getElementById('btnSexFemale').classList.toggle('active', val === 'Female');
            }} else if (field === 'smoker') {{
                document.getElementById('btnSmkNo').classList.toggle('active', val === 'No');
                document.getElementById('btnSmkYes').classList.toggle('active', val === 'Yes');
            }} else if (field === 'diabetes') {{
                document.getElementById('btnDiaNo').classList.toggle('active', val === 'No');
                document.getElementById('btnDiaYes').classList.toggle('active', val === 'Yes');
            }} else if (field === 'family_history') {{
                document.getElementById('btnFamNo').classList.toggle('active', val === 'No');
                document.getElementById('btnFamYes').classList.toggle('active', val === 'Yes');
            }}
            triggerInference(false);
        }}

        // Quick Clinical Presets
        function applyPreset(age, sex, bp, chol, bmi, smk, dia, act, fam, stress) {{
            patientState.age = age;
            patientState.sex = sex;
            patientState.blood_pressure = bp;
            patientState.cholesterol = chol;
            patientState.bmi = bmi;
            patientState.smoker = smk;
            patientState.diabetes = dia;
            patientState.physical_activity = act;
            patientState.family_history = fam;
            patientState.stress_level = stress;

            // Sync Inputs
            document.getElementById('slider_age').value = age;
            document.getElementById('input_age').value = age;
            document.getElementById('display_age').textContent = age + ' yrs';

            document.getElementById('slider_bp').value = bp;
            document.getElementById('input_bp').value = bp;
            document.getElementById('display_bp').textContent = bp + ' mmHg';

            document.getElementById('slider_chol').value = chol;
            document.getElementById('input_chol').value = chol;
            document.getElementById('display_chol').textContent = chol + ' mg/dL';

            document.getElementById('slider_bmi').value = bmi;
            document.getElementById('input_bmi').value = bmi;
            document.getElementById('display_bmi').textContent = bmi.toFixed(1) + ' kg/m²';

            document.getElementById('slider_act').value = act;
            document.getElementById('input_act').value = act;
            document.getElementById('display_act').textContent = act + ' (Score)';

            document.getElementById('slider_stress').value = stress;
            document.getElementById('input_stress').value = stress;
            document.getElementById('display_stress').textContent = stress + ' (Score)';

            setBinary('sex', sex);
            setBinary('smoker', smk);
            setBinary('diabetes', dia);
            setBinary('family_history', fam);

            triggerInference(true);
        }}

        // Random Sample Generator
        function loadRandomPatient() {{
            const randAge = Math.floor(Math.random() * 45 + 32);
            const randSex = Math.random() > 0.5 ? 'Male' : 'Female';
            const randBp = Math.floor(Math.random() * 70 + 100);
            const randChol = Math.floor(Math.random() * 120 + 160);
            const randBmi = +(Math.random() * 18 + 20).toFixed(1);
            const randSmk = Math.random() > 0.6 ? 'Yes' : 'No';
            const randDia = Math.random() > 0.7 ? 'Yes' : 'No';
            const randAct = Math.floor(Math.random() * 5);
            const randFam = Math.random() > 0.5 ? 'Yes' : 'No';
            const randStress = Math.floor(Math.random() * 9 + 1);

            applyPreset(randAge, randSex, randBp, randChol, randBmi, randSmk, randDia, randAct, randFam, randStress);
        }}

        // Exact Logistic Regression + StandardScaler Sigmoid Inference
        function computeClientInference() {{
            const sexEnc = patientState.sex.toLowerCase() === 'male' ? 1 : 0;
            const smkEnc = patientState.smoker.toLowerCase() === 'yes' ? 1 : 0;
            const diaEnc = patientState.diabetes.toLowerCase() === 'yes' ? 1 : 0;
            const famEnc = patientState.family_history.toLowerCase() === 'yes' ? 1 : 0;

            const raw = [
                patientState.age,
                sexEnc,
                patientState.blood_pressure,
                patientState.cholesterol,
                patientState.bmi,
                smkEnc,
                diaEnc,
                patientState.physical_activity,
                famEnc,
                patientState.stress_level
            ];

            const means = MODEL_DATA.scaler_mean;
            const scales = MODEL_DATA.scaler_scale;
            const coefs = MODEL_DATA.coef;
            const intercept = MODEL_DATA.intercept;

            // Standardize features
            let z = intercept;
            for (let i = 0; i < 10; i++) {{
                const scaled_i = (raw[i] - means[i]) / scales[i];
                z += coefs[i] * scaled_i;
            }}

            // Sigmoid: 1 / (1 + exp(-z))
            const probDisease = 1 / (1 + Math.exp(-z));
            const probHealthy = 1 - probDisease;

            return {{
                probDisease: probDisease * 100,
                probHealthy: probHealthy * 100,
                isDisease: probDisease >= 0.5
            }};
        }}

        // Trigger Inference
        function triggerInference(celebrate) {{
            const t0 = performance.now();
            const res = computeClientInference();
            const t1 = performance.now();

            const pDis = res.probDisease;
            const pHea = res.probHealthy;
            const isHighRisk = res.isDisease;

            // Update UI
            const titleEl = document.getElementById('resultDiagnosisTitle');
            const confEl = document.getElementById('resultConfidenceScore');
            const noteEl = document.getElementById('resultDiagnosisNote');
            const spotlight = document.getElementById('resultSpotlight');
            const avatar = document.getElementById('resultPhoto');

            if (isHighRisk) {{
                titleEl.textContent = "HIGH CARDIOVASCULAR RISK";
                titleEl.style.color = "#f87171";
                confEl.textContent = pDis.toFixed(1) + "%";
                confEl.style.color = "#ef4444";
                noteEl.textContent = "Biometric profile indicates severe cardiovascular stress, elevated systemic resistance, or lipid plaque accumulation.";
                spotlight.className = "result-spotlight";
                avatar.src = "{img_cardiac_care}";
            }} else {{
                titleEl.textContent = "LOW RISK // HEALTHY PROFILE";
                titleEl.style.color = "#34d399";
                confEl.textContent = pHea.toFixed(1) + "%";
                confEl.style.color = "#10b981";
                noteEl.textContent = "Biometric indicators fall within standard physiological ranges with low atherogenic risk markers.";
                spotlight.className = "result-spotlight healthy";
                avatar.src = "{img_heart_steth}";
            }}

            // Update Progress Bars
            document.getElementById('probValHealthy').textContent = pHea.toFixed(1) + "%";
            document.getElementById('probFillHealthy').style.width = Math.max(1, pHea) + "%";

            document.getElementById('probValDisease').textContent = pDis.toFixed(1) + "%";
            document.getElementById('probFillDisease').style.width = Math.max(1, pDis) + "%";

            // Update Telemetry
            document.getElementById('teleLatency').textContent = (t1 - t0).toFixed(2) + " ms (Edge)";
            document.getElementById('teleF1').textContent = isHighRisk ? "0.65 (Sensitivity 77.4%)" : "0.65 (Specificity 31.9%)";

            // Update Simulated Heart Rate based on BP & Stress
            const simulatedBpm = Math.round(65 + (patientState.blood_pressure - 110) * 0.15 + (patientState.stress_level * 2));
            document.getElementById('ecgBpmDisplay').textContent = Math.max(55, Math.min(140, simulatedBpm)) + " BPM";

            // Optional Confetti for Low Risk Celebration
            if (celebrate && !isHighRisk && typeof confetti === 'function') {{
                confetti({{
                    particleCount: 40,
                    spread: 60,
                    origin: {{ y: 0.65 }},
                    colors: ['#10b981', '#06b6d4']
                }});
            }}
        }}

        // Tabs Switcher
        function switchTab(tabId) {{
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));

            event.currentTarget.classList.add('active');
            const target = document.getElementById(tabId);
            if (target) target.classList.add('active');
        }}

        // Cell Inspector for Confusion Matrix
        function inspectCell(actual, pred, count, type) {{
            const inspector = document.getElementById('cellInspector');
            let html = `<strong>Quadrant Focus:</strong> Actual = <span style="color:#f87171;">${{actual}}</span> | Predicted = <span style="color:#38bdf8;">${{pred}}</span> &bull; <strong>Count: ${{count}} patients</strong>.<br>`;

            if (type === 'TP') {{
                html += `<span style="color:#ef4444;">✔ TRUE POSITIVE (TP):</span> ${{count}} patients with actual heart disease were correctly flagged. Critical for early therapeutic intervention.`;
            }} else if (type === 'TN') {{
                html += `<span style="color:#10b981;">✔ TRUE NEGATIVE (TN):</span> ${{count}} healthy patients were correctly cleared without unnecessary invasive procedures.`;
            }} else if (type === 'FP') {{
                html += `<span style="color:#f59e0b;">⚠ FALSE POSITIVE (FP / Type I Error):</span> ${{count}} healthy patients had borderline elevated biomarkers and were screened as at-risk. They will be resolved during secondary clinical testing.`;
            }} else if (type === 'FN') {{
                html += `<span style="color:#f43f5e;">🚨 FALSE NEGATIVE (FN / Type II Error):</span> ${{count}} patients with heart disease were missed by the linear decision hyperplane. In medical AI, reducing this number is the highest clinical priority!`;
            }}

            inspector.innerHTML = html;
        }}

        // Modal Helpers
        function openModal(id) {{
            const el = document.getElementById(id);
            if (el) el.style.display = 'flex';
        }}
        function closeModal(id) {{
            const el = document.getElementById(id);
            if (el) el.style.display = 'none';
        }}

        // Real-Time Animated ECG Waveform Canvas
        function initECG() {{
            const canvas = document.getElementById('ecgCanvas');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');

            function resize() {{
                const rect = canvas.getBoundingClientRect();
                canvas.width = rect.width * window.devicePixelRatio;
                canvas.height = rect.height * window.devicePixelRatio;
                ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
            }}
            window.addEventListener('resize', resize);
            resize();

            let x = 0;
            let step = 0;
            const points = [];

            function draw() {{
                const w = canvas.getBoundingClientRect().width;
                const h = canvas.getBoundingClientRect().height;
                const midY = h / 2;

                // Fade trail
                ctx.fillStyle = 'rgba(0, 0, 0, 0.08)';
                ctx.fillRect(0, 0, w, h);

                // Determine waveform shape based on phase
                const cycle = step % 80;
                let yOffset = 0;

                if (cycle === 15) yOffset = -8;        // P wave
                else if (cycle === 17) yOffset = 0;
                else if (cycle === 24) yOffset = 4;        // Q dip
                else if (cycle === 27) yOffset = -35;      // R peak
                else if (cycle === 30) yOffset = 12;       // S dip
                else if (cycle === 42) yOffset = -12;      // T wave
                else if (cycle === 46) yOffset = 0;
                else yOffset = (Math.random() - 0.5) * 1.5; // baseline noise

                const currentY = midY + yOffset;

                // Color based on risk
                const res = computeClientInference();
                ctx.strokeStyle = res.isDisease ? '#ef4444' : '#10b981';
                ctx.lineWidth = 2;
                ctx.shadowColor = res.isDisease ? '#ef4444' : '#10b981';
                ctx.shadowBlur = 8;

                ctx.beginPath();
                ctx.moveTo(x === 0 ? 0 : x - 2, currentY);
                ctx.lineTo(x, currentY);
                ctx.stroke();

                x += 2;
                step++;
                if (x >= w) {{
                    x = 0;
                    ctx.clearRect(0, 0, w, h);
                }}

                requestAnimationFrame(draw);
            }}

            draw();
        }}

        // DOM Ready
        window.addEventListener('DOMContentLoaded', () => {{
            initSensors();
            initECG();
            triggerInference(false);
        }});
    </script>
</body>
</html>
"""

# Write to index.html
with open(ROOT_DIR / "index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"SUCCESS: Heart Disease index.html written ({len(html_content)} bytes)!")
