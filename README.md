# 🦟 Malaria Incidence Prediction in East Africa Using Machine Learning

## 📌 Project Overview

This project uses machine learning to predict malaria incidence in three East African countries — **Kenya, Uganda, and Tanzania** — based on environmental and historical data. The study compares three models: **Linear Regression**, **Decision Tree Regressor**, and **Random Forest Regressor** to determine which performs best in capturing and forecasting malaria trends.

The final goal is to assist public health officials with better forecasting tools and enable data-driven malaria control strategies.

---

## 🎯 Objectives

- Predict annual malaria incidence using weather and time-based features.
- Compare the performance of multiple machine learning models.
- Visualize and interpret model predictions versus actual reported cases.
- Recommend the best-performing model for real-world deployment.
- Optionally deploy the final model as a Streamlit web app.

---

## 🧠 Technologies & Tools

- **Python** (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Joblib)
- **Jupyter Notebook** (for data analysis and model training)
- **Streamlit** (for optional web app deployment)
- **Git & GitHub** (for version control and collaboration)

---

## 📊 Models Used

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

Performance was evaluated using:
- Mean Squared Error (MSE)
- R² Score
- Visual comparison of predicted vs actual malaria cases over time

---

## 📂 Project Structure

📦 malaria-prediction-east-africa-ml/
├── data/ # Raw and cleaned data files
├── notebooks/ # Jupyter notebooks for EDA and modeling
├── models/ # Saved .pkl models using joblib
├── app/ # Optional Streamlit app code
├── plots/ # Visualizations generated from analysis
├── README.md # Project documentation
└── requirements.txt # Python dependencies


---

## 📈 Visualizations

- Correlation heatmaps
- Boxplots and distribution plots
- Actual vs predicted malaria incidence line plots (per model)
- Model performance comparison bar charts

---

## 📌 Key Insights

- **Random Forest Regressor** had the best overall accuracy and trend-matching ability.
- Rainfall and temperature were the strongest predictors of malaria incidence.
- Uganda showed more seasonal malaria peaks than Kenya and Tanzania.

---

## ✅ Recommendation

Use the **Random Forest** model for deployment in East Africa to support real-time malaria monitoring and public health interventions.

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
[git clone https://github.com/oumaouma20/malaria-prediction-east-africa-ml.git)
cd malaria-prediction-east-africa-ml

2. Set Up the Environment
pip install -r requirements.txt

3. Run the Jupyter Notebook
jupyter notebook

4. (Optional) Launch the Web App
streamlit run app/app.py

📧 Contact
Author: Emmanuel Ouma
📩 Email: emmanuelouma2000@gmail.com
🌐 Portfolio: Data Analyst Portfolio
🔗 LinkedIn: LinkedIn Profile

