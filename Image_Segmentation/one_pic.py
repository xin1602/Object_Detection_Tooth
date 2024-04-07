from ultralytics import YOLO
from PIL import Image

# Load the YOLOv8 model
model = YOLO("F:\\Lab\\share\\YOLO_segmentation\\best.pt")

# Perform inference on an image
results = model.predict('F:\\Lab\\share\\dataset\\multi_coco_json_1112_01\\test\\117_jpg.rf.bf2829db272438406ab3710bee89b31f.jpg')

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
