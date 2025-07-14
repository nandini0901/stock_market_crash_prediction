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

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nandini0901/stock_market_crash_prediction.git
   cd stock_market_crash_prediction
2.  **Install dependencies:**
   pip install -r requirements.txt
3. **Run the app:**
   streamlit run app.py

**📥 How to Use**
Launch the dashboard with streamlit run app.py.

1.  📂 Upload your CSV file (without the target column).

2.  📊 View predictions: Probabilities & Crash/No Crash outcomes.

3.  💾 Download the results as a new CSV file.

**⚡ Models Info**
📚 Random Forest: Tuned with GridSearchCV and calibrated.

🚀 XGBoost: Tuned with GridSearchCV and calibrated.

🏁 Training Accuracy: ~100% (tested on unseen data).

**🌐 Deployment Options**
Deploy to Streamlit Cloud (recommended).

Or use Heroku, Docker, or AWS EC2.

**✨ Screenshots**
<img width="1822" height="812" alt="stock_project" src="https://github.com/user-attachments/assets/fe86d92e-559c-43ba-9e26-b0d6052c8dd1" />


**🙋‍♀️ Contributing**
Pull requests are welcome! For major changes, please open an issue first.

**📜 License**
This project is licensed under the MIT License - see the LICENSE file for details.

💡 Author
Made with ❤️ by Nandini Agrawal



