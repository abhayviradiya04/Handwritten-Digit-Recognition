from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# 📌 Load Trained Model
model = tf.keras.models.load_model("digit_model_improved.h5")  # Use Improved Model

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    if "image" not in data:
        return jsonify({"error": "No image data received"}), 400

    try:
        # Convert received JSON array to NumPy array
        img = np.array(data["image"], dtype=np.float32)
        
        # Ensure proper shape (28,28) and invert colors
        img = 1 - img  # Invert (white digit on black background)
        img = img.reshape(1, 28, 28, 1)  # Reshape for CNN

        # Predict using the model
        prediction = model.predict(img)
        predicted_label = int(np.argmax(prediction))  # Convert NumPy int to Python int

        return jsonify({"prediction": predicted_label})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
