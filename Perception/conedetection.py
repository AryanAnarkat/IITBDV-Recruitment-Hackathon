from ultralytics import YOLO
import cv2
model=YOLO("best.pt")
image=cv2.imread("image.png")
image2=image.copy()
results=model(image)
cones=[]
for box in results[0].boxes:

    x1=int(box.xyxy[0][0])
    y1=int(box.xyxy[0][1])
    x2=int(box.xyxy[0][2])
    y2=int(box.xyxy[0][3])
    l=y2-y1
    cones.append(l)
    cv2.rectangle(image2, (x1, y1), (x2, y2), (108,108,0), 2)
    cv2.putText(image2, "d:"+str(int(30000/l)), (x1, y1-10),
            cv2.FONT_HERSHEY_COMPLEX,
            0.6, (0,255,0), 2)
cv2.imwrite("output.jpg", image2)
k=1
for i in cones:
   i=int(30000/i)
   print("Cone", k, "height:", i)
   k=k+1