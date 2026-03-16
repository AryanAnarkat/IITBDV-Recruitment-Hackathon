# Cone Distance Estimation using YOLO
## Overview
This project detects traffic cones in an image and estimates their distance from the camera using a monocular vision approach. Object detection is performed using the YOLO model from the Ultralytics library, and the distance of each detected cone is calculated using geometric relationships from the pinhole camera model.
## Method

The YOLO model (best.pt) is used to perform inference on the input image. The model returns bounding boxes for detected cones in the format [x1, y1, x2, y2]. From these coordinates, the height of the bounding box in pixels is calculated as:
h = y2 − y1
This pixel height is then used to estimate the distance of the cone from the camera using the formula:
d = (H × f) / h
where H is the real-world height of the cone and f is the camera focal length.

## Results

For each detected cone, the program calculates the distance and displays it on the image. Bounding boxes are drawn around cones, and the estimated distance is annotated above each box. The annotated image is saved as output.jpg, and the distances of all detected cones are prin
