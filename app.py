import streamlit as st
import joblib
import numpy as np

# Load model and scaler
rfc_model = joblib.load('rfc_model_diabetes.pkl')
sc = joblib.load('scaler.pkl')  # Replace with your actual scaler filename

# Configure page
st.set_page_config(page_title="🧬 Diabetes Predictor", page_icon="🩺", layout="centered")

# Add static background image with overlay and white font colors
st.markdown("""
    <style>
.stApp {
    position: relative;
    z-index: 1;
    min-height: 100vh;
    padding: 2rem 3rem;
    border-radius: 15px;
    color: white;
    background-image:
      linear-gradient(rgba(0, 0, 0, 0.55), rgba(0, 0, 0, 0.55)),
      url('https://d.newsweek.com/en/full/2472290/abstract-falling-drop-blood-sugar.jpg');
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
}

/* rest of your styles */
.title {
    text-align: center;
    font-size: 40px;
    color: white;
    font-weight: bold;
    margin-bottom: 10px;
    text-shadow: 1px 1px 6px rgba(0,0,0,0.9);
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: white;
    margin-bottom: 30px;
    text-shadow: 1px 1px 6px rgba(0,0,0,0.8);
}

/* other styles... */

</style>

""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title'>🧬 Diabetes Risk Predictor</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Enter patient details to predict diabetes risk</div>", unsafe_allow_html=True)

# Input Form
st.markdown("### 📋 Patient Information")
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Pregnancies (1–17)", min_value=1, max_value=17, step=1)
    glucose = st.number_input("Glucose Level (44–199 mg/dL)", min_value=44, max_value=199, step=1)
    blood_pressure = st.number_input("Blood Pressure (24–122 mmHg)", min_value=24, max_value=122, step=1)
    skin_thickness = st.number_input("Skin Thickness (7–99 mm)", min_value=7, max_value=99, step=1)

with col2:
    insulin = st.number_input("Insulin Level (14–846 µU/mL)", min_value=14, max_value=846, step=1)
    bmi = st.number_input("BMI (18.2–67.1)", min_value=18.2, max_value=67.1, step=0.1, format="%.1f")
    dpf = st.number_input("Diabetes Pedigree Function (0.078–2.42)", min_value=0.078, max_value=2.42, step=0.01, format="%.3f")
    age = st.number_input("Age (21–81 years)", min_value=21, max_value=81, step=1)

# Prediction
st.markdown("### 🧪 Prediction")
if st.button("🔍 Predict Diabetes Risk"):
    features = [pregnancies, glucose, blood_pressure, skin_thickness,
                insulin, bmi, dpf, age]

    if any(v == 0 for v in features):
        st.warning("⚠️ Please ensure all input values are within the valid range and non-zero.")
    else:
        scaled_input = sc.transform([features])
        prediction = rfc_model.predict(scaled_input)[0]
        probability = rfc_model.predict_proba(scaled_input)[0][1]

        if prediction == 1:
            st.markdown(f"""
            <div class="output-box-high">
                <h3>🩺 High Diabetes Risk</h3>
                <p style="font-size:18px;">The patient is <strong>likely</strong> to have Diabetes.</p>
                <p><strong>Confidence Score:</strong> {probability:.2%}</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="output-box-low">
                <h3>✅ Low Diabetes Risk</h3>
                <p style="font-size:18px;">The patient is <strong>unlikely</strong> to have Diabetes.</p>
                <p><strong>Confidence Score:</strong> {(1 - probability):.2%}</p>
            </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; font-size: 14px; color:#ddd;'>"
    "🧠 Built with ❤️ by <b>Smit Satani</b> | BTech AI & ML | Charusat University"
    "</div>",
    unsafe_allow_html=True
)
