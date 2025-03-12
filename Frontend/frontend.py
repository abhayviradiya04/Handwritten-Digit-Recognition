import streamlit as st
import requests
import numpy as np
import cv2
from streamlit_drawable_canvas import st_canvas

# 📌 Page Configuration
st.set_page_config(page_title="Handwritten Digit Recognition", layout="centered")

# 📌 Custom Styling
st.markdown("""
    <style>
        .stButton>button { width: 100%; padding: 10px; font-size: 20px; }
        .prediction-box { font-size: 22px; font-weight: bold; color: #2E8B57; text-align: center; padding-top: 10px; }
    </style>
""", unsafe_allow_html=True)

# 📌 Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🖊 Handwritten Digit Recognition</h1>", unsafe_allow_html=True)

# 📌 Centered Canvas
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    canvas_result = st_canvas(
        fill_color="black",
        stroke_width=10,
        stroke_color="white",
        background_color="black",
        height=280, width=280,
        drawing_mode="freedraw",
        key="canvas",
    )

# 📌 Centered Predict Button
_, btn_col, _ = st.columns([1, 2, 1])
with btn_col:
    predict_btn = st.button("🔍 Predict", use_container_width=True)

# 📌 Process Image and Send to Backend
if predict_btn:
    if canvas_result.image_data is not None:
        img = canvas_result.image_data[:, :, :3]  # Extract RGB
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # Convert to Grayscale
        _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)  # Invert and binarize
        img = cv2.resize(img, (28, 28))  # Resize to 28x28
        img = img / 255.0  # Normalize
        img = img.reshape(28, 28).tolist()  # Convert to list for JSON

        # Send Image to Backend API
        response = requests.post("http://127.0.0.1:5000/predict", json={"image": img})

        if response.status_code == 200:
            predicted_digit = response.json()['prediction']
            st.success("✅ Prediction Successful!")

            # 📌 Show Prediction
            st.markdown(f"<div class='prediction-box'>🔢 Predicted Digit: <b>{predicted_digit}</b></div>", unsafe_allow_html=True)
        else:
            st.error("⚠️ Error in Prediction! Please try again.")
