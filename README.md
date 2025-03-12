# 🖊️ Handwritten Digit Recognition ✨

![ML](https://img.shields.io/badge/Machine%20Learning-%E2%9C%85-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%E2%9C%85-orange)
![Flask API](https://img.shields.io/badge/Flask%20API-%E2%9C%85-red)
![Streamlit](https://img.shields.io/badge/Streamlit-%E2%9C%85-pink)

## 🎯 Project Overview
This project is a **Handwritten Digit Recognition System** that allows users to draw digits, characters, or symbols on a canvas, and the model predicts the output. If the input is unrecognized, it displays **"Sorry, I cannot predict."**

## 🚀 Tech Stack
- **Machine Learning:** TensorFlow, EMNIST Dataset
- **Backend:** Flask API (for model inference)
- **Frontend:** Streamlit (for UI and user input)


## 📌 Features
✔️ Recognizes **digits, characters, and symbols**
✔️ Uses **EMNIST Dataset** for training
✔️ Provides a **Flask API** for predictions
✔️ **Streamlit-based UI** for an interactive experience
✔️ Displays **"Cannot Predict"** if input is unknown

## 🛠️ Installation
### 🔧 Clone the Repository
```bash
git clone https://github.com/abhayviradiya04/Handwritten-Digit-Recognition.git
cd Handwritten-Digit-Recognition
```

### ⚙️ Install Dependencies
```bash
pip install -r requirements.txt
```

## 🌐 Start the Backend (Flask API)
```bash
python app.py
```
The Flask server will run on `http://127.0.0.1:5000/predict`.

## 🎨 Start the Frontend (Streamlit UI)
```bash
python -m streamlit run frontend.py
```
This will open the Streamlit UI in the browser.

## 📌 API Usage
Send a **POST request** to `/predict` with an image array:
```json
{
    "image": [[0, 0, ... , 255], [255, 255, ... , 0]]
}
```
Response:
```json
{
    "prediction": 3
}
```


## 💡 Future Enhancements
🔹 Improve character recognition accuracy
🔹 Add real-time webcam support
🔹 Deploy on cloud for public use

## 📜 License
This project is licensed under the **MIT License**.

🚀 **Happy Coding!** 😃

