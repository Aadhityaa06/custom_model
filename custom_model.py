# Importing the modules
import os
import time
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model, load_model
import numpy as np
import tensorflow as tf
import tensorflow.keras
from PIL import Image, ImageOps
import argparse
import io
import picamera

# Set classes names
classes_names = ['animals', 'other', 'person']  # You can change classes

# Load model
model_path = 'animall_person_other_v2_fine_tuned.h5'  # You can change name and path for model
model = load_model(model_path)

# Start capturing the image from the PiCamera
with picamera.PiCamera(resolution=(640, 480), framerate=30) as camera:
    try:
        stream = io.BytesIO()
        for _ in camera.capture_continuous(
                stream, format='jpeg', use_video_port=True):
            stream.seek(0)

            # Change image size from 299, 299 to any size
            img = Image.open(stream).convert('RGB').resize((299, 299), Image.ANTIALIAS)

            # Start time
            start_time = time.time()

            # Predict class from video stream
            x = image.img_to_array(img)
            x /= 255
            x = np.expand_dims(x, axis=0)
            prediction = model.predict(x)
            classes = np.argmax(prediction, axis=1)

            # Calculate elapsed time and clear the stream
            elapsed_ms = (time.time() - start_time) * 1000
            stream.seek(0)
            stream.truncate()

            # Print the predicted class and elapsed time
            print("Elapsed time: {} ms, Predicted class number: {}, Predicted class name: {}".format(
                elapsed_ms, classes[0], classes_names[classes[0]]
            ))

    finally:
        camera.stop_preview()
