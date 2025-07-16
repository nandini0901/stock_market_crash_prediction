# stock_market_crash_prediction
A machine learning app to predict stock market crashes using Random Forest and XGBoost.
# 📉 Stock Market Crash Prediction Dashboard

This project predicts the likelihood of stock market crashes using advanced machine learning models (✅ Random Forest and ✅ XGBoost). The dashboard is built with [Streamlit](https://streamlit.io/) and allows users to upload their own datasets for instant predictions.

Live Dashboard here: https://stockmarketcrashprediction-mydashboard.streamlit.app/
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

✨ Screenshot
<img width="1822" height="812" alt="stock_project" src="https://github.com/user-attachments/assets/8ff6dfa4-75cf-4090-8a77-1bd9acedff37" />


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
│ ├── sample_input_file.csv # sample file
└── 📁 notebooks/
├── modeling.ipynb # Training & tuning notebook
└── deployment.ipynb # Deployment predictions notebook`


---

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nandini0901/stock_market_crash_prediction.git
   cd stock_market_crash_prediction
2.  **Install dependencies:**
   pip install -r requirements.txt
3.  **Run the app:**
   streamlit run app.py

📥 How to Use

- Launch the dashboard with streamlit run app.py.

- 📂 Upload your CSV file (without the target column).

- 📊 View predictions: Probabilities & Crash/No Crash outcomes.

- 💾 Download the results as a new CSV file.

⚡ Models Info

📚 Random Forest: Tuned with GridSearchCV and calibrated.

🚀 XGBoost: Tuned with GridSearchCV and calibrated.

🏁 Training Accuracy: ~100% (tested on unseen data).

🌐 Deployment Options

Deploy to Streamlit Cloud (recommended).

Or use Heroku, Docker, or AWS EC2.

🙋‍♀️ Contributing
Pull requests are welcome! For major changes, please open an issue first.

💡 Author
Made by @nandini0901-github



