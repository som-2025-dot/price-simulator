import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd

# --- Load your data ---
# If you already saved your cleaned data as CSV, load it like this:
# df = pd.read_csv("cleaned_electronic_sales.csv")

# For now, you can re-train the model directly in this file:
df = pd.read_csv("Electronic_sales_Sep2023-Sep2024.csv")
df = df[df["Order Status"] == "Completed"]
df["Add-ons Purchased"] = df["Add-ons Purchased"].fillna("None")
df = df.dropna()
X = df[["Unit Price", "Age", "Gender", "Loyalty Member", "Product Type"]]
y = df["Quantity"]
X_encoded = pd.get_dummies(X, drop_first=True)

# Train the polynomial model
X_price = X_encoded[["Unit Price"]]
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X_price)
model = LinearRegression().fit(X_poly, y)

# Streamlit app
st.title("📊 Price Sensitivity Simulator")
st.markdown("Use the slider to test different prices and see predicted quantity and revenue.")

# Slider
price = st.slider("Set Unit Price (₹)", 10, 1000, 500)

# Predict
price_poly = poly.transform([[price]])
predicted_qty = model.predict(price_poly)[0]
revenue = predicted_qty * price

# Output
st.metric("📦 Predicted Quantity", f"{predicted_qty:.2f}")
st.metric("💰 Expected Revenue", f"₹{revenue:.2f}")
