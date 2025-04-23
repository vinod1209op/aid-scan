# 🛠 AID-SCAN: Full Deployment Guide

This guide contains everything you need to fully deploy the AID-SCAN project with CI/CD, Docker, and GitHub integration.

---

## 📁 1. Project Structure Overview

```
aid_scan_project/
├── .github/workflows/ci.yml       # GitHub Actions CI pipeline
├── alerts/                        # Alerting + SHAP
├── config/                        # Configuration files
├── dashboard/templates/           # Optional UI templates
├── data/                          # Raw, processed, labeled data
├── models/                        # ML models
├── notebooks/                     # Evaluation notebooks
├── pipelines/                     # Train, inference, retrain
├── preprocessing/                # Feature engineering
├── threat_intel/                 # Threat feeds
├── tests/                         # Unit tests
├── Dockerfile                     # Docker support
├── requirements.txt
└── README.md
```

---

## ✅ 2. Local Setup Instructions

### 🔧 Install dependencies
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 🧪 Run example
```bash
python preprocessing/log_parser.py
```

---

## 🐙 3. GitHub + CI/CD Setup

### 🐾 Initialize & push to GitHub
```bash
git init
git remote add origin https://github.com/YOUR_USERNAME/aid-scan.git
git add .
git commit -m "Initial commit"
git push -u origin main
```

### 🚦 GitHub Actions
Push will trigger `.github/workflows/ci.yml` to:
- Run lint checks
- Install dependencies
- Execute unit tests
- Build Docker image

View results in **GitHub > Actions**.

---

## 🐳 4. Docker Setup

### 🛠 Build locally
```bash
docker build -t aid-scan .
```

### ▶️ Run the container
```bash
docker run -it aid-scan
```

---

## ☁️ 5. Deploying to Cloud (Heroku Example)

### 🚀 Login & create project
```bash
heroku login
heroku create aid-scan-project
```

### 🔁 Add Docker support
```bash
heroku container:login
heroku container:push web -a aid-scan-project
heroku container:release web -a aid-scan-project
```

### 🌐 Open it
```bash
heroku open
```

---

## 🧪 6. Run Unit Tests
```bash
pytest tests/
```

---

## 📤 7. Alerting (Slack)

In `alerts/alert_manager.py`, replace webhook URL with your Slack webhook.

---

## 📈 8. SHAP Explainability

Run SHAP visualization:
```python
from alerts.shap_explainer import explain_prediction
explain_prediction(your_model, your_input_data)
```

---

🎉 Done! You're now fully deployed with CI, Docker, and SHAP explainability.

