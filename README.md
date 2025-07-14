# stock_market_crash_prediction
A machine learning app to predict stock market crashes using Random Forest and XGBoost.
# 📉 Stock Market Crash Prediction Dashboard

This project predicts the likelihood of stock market crashes using advanced machine learning models (✅ Random Forest and ✅ XGBoost). The dashboard is built with [Streamlit](https://streamlit.io/) and allows users to upload their own datasets for instant predictions.

---

## 🚀 Features
- 🔮 Predicts crash probabilities and binary outcomes (`Crash` or `No Crash`).
- 📊 Uses tuned and calibrated Random Forest and XGBoost models.
- 📥 Upload your own CSV file to get predictions.
- 📈 Download results directly from the app.
- ⚡ Fast and lightweight – runs locally or deploys to cloud easily.

---

## 📦 Models Used
- **Random Forest (Calibrated)**
  - Threshold: `0.40`
- **XGBoost (Calibrated)**
  - Threshold: `0.9987`
- Both models trained on **20 top features** selected from market and sentiment data.

---

## 📂 Project Structure
```bash
📁 stock_market_crash_prediction/
├── 📄 app.py # Streamlit app
├── 📄 requirements.txt # Required Python libraries
├── 📄 README.md # This file
├── 📁 models/
│ ├── calibrated_random_forest_model.pkl
│ ├── calibrated_xgboost_model.pkl
│ ├── optimal_thresholds.pkl
├── 📁 data/
│ ├── deployment_predictions.csv # Example dataset
│ ├── sample_input.csv # Lightweight sample file
└── 📁 notebooks/
├── modeling.ipynb # Training & tuning notebook
└── deployment.ipynb # Deployment predictions notebook


---

