🚀 Features

Custom Dataset: Collected images via a web extension from Google Images.

Data Preprocessing:

Removed noisy/dodgy images.

Resized and cleaned image data.

Used TensorFlow’s DataLoader class for efficient batching.

Model Architecture:
model=Sequential()
model.add(Conv2D(16,(3,3),1,activation='relu',input_shape=(256,256,3)))
model.add(MaxPooling2D())
model.add(Conv2D(32,(3,3),1,activation='relu'))
model.add(MaxPooling2D())
model.add(Conv2D(16,(3,3),1,activation='relu'))
model.add(MaxPooling2D())
model.add(Flatten())
model.add(Dense(256,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

Convolutional Neural Network (CNN).

Trained on a binary classification task (Happy vs Sad).

Performance:

Testing Accuracy: 98%

Validation Accuracy: 96%

Performs well on unseen data.

Visualization:

Plotted accuracy and loss curves during training.

Displayed images using OpenCV, ImageShow, and Python’s os module.

Deployment:

Converted into a Streamlit demo app for real-time image classification.

🛠️ Tech Stack

Python

TensorFlow / Keras

OpenCV

ImageShow

Streamlit

📊 Model Performance
Metric	Accuracy
Training Accuracy	~98%
Validation Accuracy	~96%
Test Accuracy	~98%

📈 The model shows strong generalization and robustness on unseen data.

🖥️ Streamlit Demo

The project includes a Streamlit app that allows users to upload an image and get an instant prediction (Happy/Sad).

Run it locally:

streamlit run image_classifier.py

📂 Project Structure
├── notebooks           
├── image_classifier.py  
└── README.md            
📸 Example Outputs

Happy 🙂
Sad 🙁


📌 Future Improvements

Extend dataset with more diverse faces.

Add multi-class classification (e.g., Angry, Neutral, Excited).

Deploy app to Streamlit Cloud or Hugging Face Spaces for public use.

👨‍💻 Author

Developed by Irfan Khan.
A huge thanks to NicholasRenotte
And Chatgpt for helping me with the front end
