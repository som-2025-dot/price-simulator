
# 💰 Price Sensitivity Simulator

This is a Streamlit web app that helps simulate how changes in product price affect quantity sold and revenue — using real sales data and regression models.

🔗 **Live App**: [Click here to try it out](https://price-simulator-cd2j9rbda2nqkfq6xkgaf4.streamlit.app/)

---

## 📊 Features

- Upload historical sales data
- Fit a regression model (Linear / Polynomial)
- Choose a price using a slider
- Instantly get predicted quantity sold & expected revenue
- Visualize revenue curve to identify optimal price

---

## 🧠 Models Used

- Linear Regression  
- Polynomial Regression (degree = 2)

We simulate price sensitivity by modeling:
Quantity = f(Unit Price)
Revenue = Unit Price × Predicted Quantity


---

## 🖼 Sample Screenshot

![App Screenshot](https://your-screenshot-link.com) <!-- Replace with your own screenshot link -->

---

## 📁 Repo Structure

📁 price-simulator/
├── streamlit_app.py # Main Streamlit app
├── requirements.txt # Dependencies
└── Electronic_sales_Sep2023-Sep2024.csv # Input sales dataset


---

## 🚀 How to Run Locally

1. Clone the repo:
```bash
git clone https://github.com/som-2025-dot/price-simulator.git
cd price-simulator
Install dependencies:


pip install -r requirements.txt
Run the Streamlit app:

streamlit run streamlit_app.py
👨‍💻 Built With
Python 🐍

Streamlit ⚡

scikit-learn 🤖

pandas 📊
