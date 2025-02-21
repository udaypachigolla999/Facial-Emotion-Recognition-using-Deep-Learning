# app.py

import threading
from flask import Flask, render_template, Response
from flask import request, redirect, url_for
from werkzeug.utils import secure_filename
import cv2
import os
import numpy as np
from keras.models import model_from_json

app = Flask(__name__)


emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}




script_dir = os.path.dirname(os.path.abspath(__file__))

# Update the constants at the beginning of your app.py
UPLOAD_FOLDER = os.path.join(script_dir, 'uploads')
ALLOWED_EXTENSIONS = {'mp4', 'avi'}

# Add this configuration after creating the Flask app
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Specify the file path relative to the script directory
json_file_path = os.path.join(script_dir, "models/emotion_model.json")

# Open the file
with open(json_file_path, 'r') as json_file:
    loaded_model_json = json_file.read()

emotion_model = model_from_json(loaded_model_json)

weights_file_path = os.path.join(script_dir, "models/emotion_model.weights.h5")
emotion_model.load_weights(weights_file_path)












print("Loaded emotion model from disk")



video_uploaded = False
cap = None
detection_paused = threading.Event()
previous_detection_state = False

@app.route('/')
def index():
    return render_template('index.html')

def gen():
    global cap, video_uploaded
    detection_paused.clear()
    while True:
        print("hii")
        if video_uploaded:
            while detection_paused.is_set():
                # If detection is paused, wait until it's resumed
                pass
            ret, frame = cap.read()
            frame = cv2.resize(frame, (1280, 720))
            if not ret:
                break
            
            #Face detection

            face_cascade_path = os.path.join(script_dir, 'haarcascades', 'haarcascade_frontalface_default.xml')
            face_detector = cv2.CascadeClassifier(face_cascade_path)

            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            num_faces = face_detector.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

            for (x, y, w, h) in num_faces:
                cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (0, 255, 0), 4)
                roi_gray_frame = gray_frame[y:y + h, x:x + w]
                cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (48, 48)), -1), 0)

                # Emotion prediction
                emotion_prediction = emotion_model.predict(cropped_img)
                maxindex = int(np.argmax(emotion_prediction))
                emotion_label = emotion_dict[maxindex]
                












                # Display emotion label
                cv2.putText(frame, f'Emotion: {emotion_label}', (x+5, y-60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            
            


            _, jpeg = cv2.imencode('.jpg', frame)
            frame = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        
        else:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + b'' + b'\r\n\r\n')


@app.route('/upload_video', methods=['POST'])
def upload_video():
    global video_uploaded, cap, detection_paused, previous_detection_state
    print('uploadoneeeeeeeeeeeeeeeeeeeeeee')
    if 'video' in request.files:
        video_file = request.files['video']
        
        # Check if the file has an allowed extension
        if '.' in video_file.filename and \
                video_file.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
            # Ensure the 'uploads' directory exists
            os.makedirs(UPLOAD_FOLDER, exist_ok=True)

            
            # Save the video file to a secure location
            video_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(video_file.filename))
            video_file.save(video_path)
            video_uploaded = True
            previous_detection_state = detection_paused.is_set()
            detection_paused.clear()
            # Update the video feed source
            if cap is not None:
                cap.release()
            cap = cv2.VideoCapture(video_path)

            if previous_detection_state:
                detection_paused.set()

    return redirect(url_for('index'))

@app.route('/video_feed')
def video_feed():
    if video_uploaded:
        return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        # If no video has been uploaded, return an empty response
        return '', 204

@app.route('/pause_detection', methods=['GET', 'POST'])
def pause_detection():
    global detection_paused
    detection_paused.set()
    return 'Detection paused', 200

@app.route('/resume_detection', methods=['GET', 'POST'])
def resume_detection():
    global detection_paused
    detection_paused.clear()
    return 'Detection resumed', 200


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
