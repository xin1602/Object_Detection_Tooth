import cv2
from ultralytics import YOLO
import numpy as np

# 讀取圖片
image_path = 'F:\\Lab\\share\\dataset\\two_label_data_v1\\GRAY_AHE\\13.jpg'
image = cv2.imread(image_path)

# 初始化 YOLOv8 模型
model = YOLO('F:\\Lab\\share\\YOLO_segmentation\\seg_0312_tooth_data_v1_0308_GRAY_AHE_01\\train3\\weights\\best.pt')

# 執行預測
results = model(image)

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