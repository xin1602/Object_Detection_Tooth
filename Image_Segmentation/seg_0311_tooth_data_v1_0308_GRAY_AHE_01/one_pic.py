from ultralytics import YOLO
from PIL import Image

# Load the YOLOv8 model
model = YOLO("F:\\Lab\\share\\YOLO_segmentation\\seg_0311\\yolo\\best.pt")

# Perform inference on an image
results = model.predict("F:\\Lab\\share\\dataset\\two_label_data_v1\\GRAY_AHE\\12.jpg")

# results.show()

# # Extract bounding boxes, classes, names, and confidences
# boxes = results[0].boxes.xywh.tolist()
# classes = results[0].boxes.cls.tolist()
# names = results[0].names
# confidences = results[0].boxes.conf.tolist()


# # View results
# for r in results:
#     print(r.obb)

for r in results:
    n=1
    im_array = r.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    im.show()  # show image
    im.save('results.jpg')  # save image

# # Iterate through the results
# for box, cls, conf in zip(boxes, classes, confidences):
#     x1, y1, x2, y2 = box
#     confidence = conf
#     detected_class = cls
#     name = names[int(cls)]


# from ultralytics import YOLO

# # Load the YOLOv8 model
# model = YOLO('yolov8n-obb.pt')

# # Perform inference on an image
# results = model('https://ultralytics.com/images/bus.jpg')

# # Extract bounding boxes, classes, names, and confidences
# boxes = results[0].boxes.xyxy.tolist()
# classes = results[0].boxes.cls.tolist()
# names = results[0].names
# confidences = results[0].boxes.conf.tolist()

# # Iterate through the results
# for box, cls, conf in zip(boxes, classes, confidences):
#     x1, y1, x2, y2 = box
#     confidence = conf
#     detected_class = cls
#     name = names[int(cls)]
#     print(x1, y1, x2, y2)
#     print(confidence)
#     print(detected_class)
#     print(name)
