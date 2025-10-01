import numpy as np
import streamlit as st
from PIL import Image
import tensorflow as tf

model = tf.keras.models.load_model(r"C:\Users\Homii\OneDrive\Desktop\new_onr\image_classifier.keras")

# Define class names (binary case)
class_names = ["happy", "sad"]

# Streamlit app UI
st.title("😊😢 Emotion Classifier")
st.write("Upload an image and let the model decide if it's happy or sad!")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg","bmp"])

if uploaded_file is not None:
    # Open and display the image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess the image (adjust size to your training size, e.g., 128x128)
    img = image.resize((256,256))
    img_array = np.array(img) / 255.0   # normalize if trained that way
    img_array = np.expand_dims(img_array, axis=0)  # add batch dimension

    # Make prediction
    prediction = model.predict(img_array)[0][0]  # sigmoid gives a single value
    if prediction>0.5:
        st.write("### 😢 Prediction: **sad**")
    else:
        st.write("### 😊 Prediction: **happy**")

