# 🧬 Diabetes Risk Prediction App

This project is a **Machine Learning powered web application** that predicts whether a person is at risk of diabetes based on several medical inputs. It uses **Random Forest Classifier** as the final model and is deployed using **Streamlit** for an interactive and responsive user experience.

---

## 🚀 Features

- 🔍 Predicts diabetes risk using medical features.
- 📊 Uses multiple ML models and selects the best one (RandomForestClassifier).
- 📈 Data preprocessed using:
  - **SMOTE** for oversampling the minority class.
  - **StandardScaler** for feature scaling.
  - **Median imputation** for missing/invalid (zero) values.
- 💡 Highlights high/low risk with intuitive UI design.
- 🌐 Clean Streamlit web UI with live predictions.

---

## 📁 Dataset Info

We use the **Pima Indians Diabetes dataset**, which includes:

- `Pregnancies`
- `Glucose`
- `BloodPressure`
- `SkinThickness`
- `Insulin`
- `BMI`
- `DiabetesPedigreeFunction`
- `Age`
- `Outcome` (0 = No Diabetes, 1 = Diabetes)

Invalid values like `0` (except for Pregnancies) are imputed using **median values**.

---

## 🧠 Machine Learning Models Used

| Model                   | Purpose                      |
|------------------------|------------------------------|
| Logistic Regression     | Baseline model               |
| Decision Tree Classifier| Tree-based learning          |
| GaussianNB              | Probabilistic approach       |
| Random Forest Classifier| ✅ **Best performer** with highest accuracy and recall |

> Final model selected: `RandomForestClassifier`  
> Accuracy: **0.792**  
> F1-score: **0.804**  
> Recall: **0.764**

---

## 🛠️ Tech Stack

- **Python**
- **scikit-learn**
- **pandas / numpy**
- **SMOTE (imblearn)**
- **Streamlit** for web UI
- **Joblib** for model persistence

---

## ⚙️ Installation & Running the App

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/diabetes-predictor.git
cd diabetes-predictor
```
## 2. Install Dependencies
Make sure you have Python 3.7+ installed. Then run:

pip install -r requirements.txt

## 3. Run the App

streamlit run app.py

📸 Sample Output
<p align="center"> <img src="screenshots/sample_output.png" width="600"/> </p>
---
## 🧪 Input Example for Prediction
- **Pregnancies: 3**
- **Glucose: 117**
- **BloodPressure: 72**
- **SkinThickness: 23**
- **Insulin: 30**
- **BMI: 32.0**
- **DiabetesPedigreeFunction: 0.372**
- **Age: 29**

## Output: ✅ Low Diabetes Risk
Confidence Score: 88.5%
---
## 📂 Project Structure

## diabetes-predictor/
│
├── app.py                # Streamlit app frontend
├── model_pipeline.pkl    # Final trained pipeline (scaler + model)
├── rfc_model_diabetes.pkl# Trained Random Forest model
├── requirements.txt      # All dependencies
└── README.md             # You're here!
