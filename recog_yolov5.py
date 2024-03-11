import cv2
import torch
import pandas as pd
import matplotlib.pyplot as plt

# Load the YOLOv8 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5m', pretrained=True)

# Define the video capture object
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Inference on a single image
    results = model(frame)

    # Render the results on the frame
    frame_with_results = results.render()[0]

    # Display the frame with results
    cv2.imshow('YOLOv8', frame_with_results)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the window
cap.release()
cv2.destroyAllWindows()