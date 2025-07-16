import streamlit as st
import pandas as pd
import numpy as np
import joblib

# 🎨 Streamlit page configuration
st.set_page_config(
    page_title="📉 Stock Market Crash Prediction",
    layout="wide",
    page_icon="📊",
)

# 🏷️ App title
st.title("📉 Stock Market Crash Prediction Dashboard")
st.markdown(
    """
This app uses **Calibrated Random Forest** and **XGBoost** models to predict the likelihood of a stock market crash (is_crash=1).
Upload your data matching the sample format to get predictions.
"""
)

# 📦 Load calibrated models and thresholds
try:
    rf_model = joblib.load('D:/stock_market_crash_prediction/notebooks/calibrated_random_forest_model.pkl')
    xgb_model = joblib.load('D:/stock_market_crash_prediction/notebooks/calibrated_xgboost_model.pkl')
    thresholds = joblib.load('D:/stock_market_crash_prediction/notebooks/optimal_thresholds.pkl')
    rf_threshold = thresholds['rf']
    xgb_threshold = thresholds['xgb']

    st.success(f"✅ Models and thresholds loaded! (RF: {rf_threshold:.2f}, XGB: {xgb_threshold:.4f})")
except Exception as e:
    st.error(f"❌ Error loading models or thresholds: {e}")
    st.stop()

# 📥 Upload CSV file
uploaded_file = st.file_uploader("📤 Upload your CSV file (no target column required)", type=["csv"])

# 📥 Sample CSV download
with open("D:/stock_market_crash_prediction/merged_top_features(no_target).csv", "rb") as f:
    st.download_button(
        label="📥 Download Sample Input File",
        data=f,
        file_name="sample_input.csv",
        mime="text/csv"
    )

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)
        st.success(f"✅ File uploaded successfully! Shape: {data.shape}")

        # Drop target column if user accidentally included it
        if 'is_crash' in data.columns:
            data = data.drop(columns=['is_crash'])
            st.warning("⚠️ Dropped 'is_crash' column from input data.")

        # 🚀 Make predictions
        st.info("🔮 Making predictions...")
        rf_probs = rf_model.predict_proba(data)[:, 1]
        xgb_probs = xgb_model.predict_proba(data)[:, 1]

        rf_preds = (rf_probs >= rf_threshold).astype(int)
        xgb_preds = (xgb_probs >= xgb_threshold).astype(int)

        # 📊 Add predictions to dataframe
        results = data.copy()
        results['RF_Crash_Probability'] = rf_probs.round(4)
        results['RF_Crash_Prediction'] = rf_preds
        results['XGB_Crash_Probability'] = xgb_probs.round(4)
        results['XGB_Crash_Prediction'] = xgb_preds

        st.success("✅ Predictions completed!")

        # 📋 Show a preview of results
        st.dataframe(results.head(10))

        # 📥 Download predictions
        csv = results.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Predictions as CSV",
            data=csv,
            file_name='predictions_output.csv',
            mime='text/csv'
        )

    except Exception as e:
        st.error(f"❌ Error processing file: {e}")

else:
    st.info("📂 Please upload a CSV file to start predictions.")

# Footer
st.markdown("---")
st.markdown("© 2025 Stock Crash Predictor | Built with ❤️ using Streamlit")
