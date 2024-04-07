import cv2
from ultralytics import YOLO
import numpy as np

# 讀取圖片
image_path = 'F:\\Lab\\share\\dataset\\multi_coco_json_1112_01\\test\\117_jpg.rf.bf2829db272438406ab3710bee89b31f.jpg'
image = cv2.imread(image_path)

# 初始化 YOLOv8 模型
model = YOLO('F:\\Lab\\share\\YOLO_segmentation\\best.pt')

# 執行預測
results = model(image)

# # 提取預測結果中的旋轉矩形的信息
# obb_info = results.obb[0].cpu().numpy()  # 將 OBB 結果轉換為 NumPy 格式

# # 打印每個旋轉矩形的信息
# for obb in obb_info:
#     # 獲取旋轉矩形的坐標、角度和其他相關信息
#     x, y, w, h, angle, confidence, class_id = obb
#     class_name = model.names[int(class_id)]  # 獲取類別名稱

#     print(f"Bounding Box: ({x}, {y}), Width: {w}, Height: {h}, Angle: {angle}, Confidence: {confidence}, Class: {class_name}")

# # 獲取 xyxy 格式的邊界框信息
# xyxy_boxes = results.xyxy.cpu().numpy()

# # 打印每個邊界框的信息
# for box in xyxy_boxes:
#     x_min, y_min, x_max, y_max = box[:4]
#     print(f"Bounding Box: ({x_min}, {y_min}, {x_max}, {y_max})")


# 獲取第一個結果
result = results[0]

# 確認結果的類型
print(type(result))

# 根據結果的類型，獲取相應的屬性
if isinstance(result, dict):
    obb_info = result['obb']
else:
    obb_info = result.obb

# 打印結果
print(obb_info)