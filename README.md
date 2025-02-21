# 🤖 Facial Emotion Recognition Using Deep Learning

## 📌 Project Description
This project implements an **😊 Emotion Recognition System** using **Deep Learning**. It provides a user-friendly interface for uploading 🎥 videos, detecting 👀 faces, and classifying 😊 emotions in real-time through a Flask-based web interface.

## 🌟 Features
- Detects human faces in a 🎥 video.
- Classifies emotions into **😡 Angry, 🤢 Disgusted, 😨 Fearful, 😃 Happy, 😐 Neutral, 😢 Sad, & 😲 Surprised**.
- Provides 📡 real-time streaming of detection results.
- Allows users to ⏸ **pause & ▶ resume** detection.

## 📚 Dataset & Training
- The **🗂 FER Dataset** (Facial Expression Recognition) was taken from Kaggle, containing `📂 train` and `📂 test` datasets.
- **Training**: The `📜 Emotion Recognition Training.ipynb` was used to train the 🧠 deep learning model, generating:
  - `📜 emotion_model.json` (🛠 model architecture)
  - `📜 emotion_model.weights.h5` (📊 trained weights)
- **Testing**: The `📜 Emotion Recognition Testing.ipynb` was used for detecting 😊 emotions from a video path or live webcam feed.

## 🛠 Tech Stack
- **🖥 Backend**: Flask (🐍 Python)
- **🎨 Frontend**: HTML, CSS, JavaScript
- **🤖 Deep Learning Framework**: TensorFlow, Keras
- **👀 Computer Vision**: OpenCV
- **📊 Dataset**: FER dataset from Kaggle

## 📂 Project Structure
```
Emotion_Recognition/
│── 📂 haarcascades/
│   ├── 📜 haarcascade_frontalface_default.xml
│
│── 📂 models/
│   ├── 📜 emotion_model.json
│   ├── 📜 emotion_model.weights.h5
│
│── 📂 static/css/
│   ├── 🎨 style.css
│
│── 📂 templates/
│   ├── 📝 index.html
│
│── 📂uploads/  # Directory for 📤 uploaded 🎥 videos
│── 🖥 app.py    # Main Flask 🖥 application
│── 📜 Emotion Recognition Training.ipynb  # Model training notebook
│── 📜 Emotion Recognition Testing.ipynb   # Testing notebook
│── 📜 README.md
│── 📜 requirements.txt
```

## 🔧 Installation & Setup
### 📌 Prerequisites
- **🐍 Python 3.10**

### 🚀 Running the Application
1. Clone this repository:
    ```sh
    git clone https://github.com/udaypachigolla999/Facial-Emotion-Recognition.git
    cd Facial-Emotion-Recognition
    ```
2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the Flask 🖥 server:
    ```sh
    python app.py
    ```
4. Open a 🌐 web browser and navigate to:
    ```
    http://127.0.0.1:5000/
    ```
5. 📤 Upload a video & start real-time facial emotion detection.

## 🎯 Usage
- Click **📤 Upload Video** and select a `.mp4` or `.avi` file.
- Click **Upload and Detect Emotions** to start processing.
- Click ⏸ **Pause** to stop detection temporarily.
- Click ▶ **Play** to resume detection.
- Alternatively, run `📜 Emotion Recognition Testing.ipynb` for video-based or webcam detection.

## 👥 Contributors
Feel free to 🖥 fork this repository and contribute to the project!

- [**Uday Pachigolla**](https://github.com/udaypachigolla999/)

## 📜 License
This project is licensed under the 📜 MIT License - see the 📜 [LICENSE](LICENSE) file for details.

