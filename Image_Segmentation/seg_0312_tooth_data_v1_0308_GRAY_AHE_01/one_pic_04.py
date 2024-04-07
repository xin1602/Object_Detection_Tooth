import cv2
import math
from ultralytics import YOLO
import numpy as np

# 讀取圖片
image_path = 'F:\\Lab\\share\\dataset\\two_label_data_v1\\GRAY_AHE\\13.jpg'
image = cv2.imread(image_path)

# 初始化 YOLOv8 模型
model = YOLO("F:\\Lab\\share\\YOLO_segmentation\\seg_0312_tooth_data_v1_0308_GRAY_AHE_01\\train3\\weights\\best.pt")


# 執行預測
results = model(image)

# 獲取第一個結果
result = results[0]

# 獲取 OBB 信息
obb_info = result.obb

# 建立 mask_images 資料夾
import os
if not os.path.exists('F:\\Lab\\share\\YOLO_segmentation\\seg_0312_tooth_data_v1_0308_GRAY_AHE_01\\mask_images'):
    os.makedirs('F:\\Lab\\share\\YOLO_segmentation\\seg_0312_tooth_data_v1_0308_GRAY_AHE_01\\mask_images')

# 對每個邊界框進行處理
sorted_indices = sorted(range(len(obb_info.xyxyxyxy)), key=lambda i: obb_info.xyxyxyxy[i][0][0].item())  # 根據 orbit_center_x 排序的索引列表
for i, idx in enumerate(sorted_indices):
    # 獲取邊界框的四個角點座標
    pts = obb_info.xyxyxyxy[idx].numpy().reshape(-1, 2).astype(np.int32)
    # 計算邊界框的中心點座標
    center_x = int((pts[0][0] + pts[2][0]) / 2)
    center_y = int((pts[0][1] + pts[2][1]) / 2)
    # 計算邊界框的寬和高
    width = int(math.sqrt((pts[1][0] - pts[0][0])**2 + (pts[1][1] - pts[0][1])**2))
    height = int(math.sqrt((pts[2][0] - pts[1][0])**2 + (pts[2][1] - pts[1][1])**2))
    # 計算旋轉角度
    angle = math.atan2(pts[1][1] - pts[0][1], pts[1][0] - pts[0][0]) * 180 / math.pi
    # 獲取旋轉矩形的四個角點
    rect = ((center_x, center_y), (width, height), angle)
    box = cv2.boxPoints(rect)
    # 將角點轉換為整數類型
    box = np.int0(box)
    # 繪製遮罩
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    cv2.drawContours(mask, [box], 0, (255), -1)
    # 裁剪圖像
    masked_image = cv2.bitwise_and(image, image, mask=mask)
    # 保存遮罩圖像，使用原始圖片的檔名加上排序索引 i
    original_filename = os.path.splitext(os.path.basename(image_path))[0]
    cv2.imwrite(f'F:\\Lab\\share\\YOLO_segmentation\\seg_0312_tooth_data_v1_0308_GRAY_AHE_01\\mask_images\\{original_filename}_{i}.jpg', masked_image)







# import cv2
# import math
# from ultralytics import YOLO
# import numpy as np

# # 讀取圖片
# image_path = 'F:\\Lab\\share\\dataset\\multi_coco_json_1112_01\\test\\117_jpg.rf.bf2829db272438406ab3710bee89b31f.jpg'
# image = cv2.imread(image_path)

# # 初始化 YOLOv8 模型
# model = YOLO('F:\\Lab\\share\\YOLO_segmentation\\best.pt')

# # 執行預測
# results = model(image)

# # 獲取第一個結果
# result = results[0]

# # 獲取 OBB 信息
# obb_info = result.obb

# # 建立 mask_images 資料夾
# import os
# if not os.path.exists('mask_images'):
#     os.makedirs('mask_images')

# # 對每個邊界框進行處理
# for i in range(len(obb_info.xyxyxyxy)):
#     # 獲取邊界框的四個角點座標
#     pts = obb_info.xyxyxyxy[i].numpy().reshape(-1, 2).astype(np.int32)
    
#     # 計算邊界框的寬和高
#     width = np.linalg.norm(pts[1] - pts[0])
#     height = np.linalg.norm(pts[2] - pts[1])
    
#     # 計算等比例縮放後的寬和高
#     max_dim = max(width, height)
#     scale_factor = 640 / max_dim
#     new_width = int(width * scale_factor)
#     new_height = int(height * scale_factor)
    
#     # 獲取邊界框的中心點座標
#     center_x = int((pts[0][0] + pts[2][0]) / 2)
#     center_y = int((pts[0][1] + pts[2][1]) / 2)
    
#     # 計算新圖像的左上角座標
#     new_x = max(0, center_x - new_width // 2)
#     new_y = max(0, center_y - new_height // 2)
    
#     # 裁剪圖像
#     cropped_image = image[new_y:new_y+new_height, new_x:new_x+new_width]
    
#     # 將裁剪後的圖像等比例縮放至 640x640
#     resized_image = cv2.resize(cropped_image, (640, 640))
    
#     # 保存圖像
#     cv2.imwrite(f'mask_images/mask_{i}.jpg', resized_image)




# import cv2
# import math
# from ultralytics import YOLO
# import numpy as np

# # 讀取圖片
# image_path = 'F:\\Lab\\share\\dataset\\multi_coco_json_1112_01\\test\\117_jpg.rf.bf2829db272438406ab3710bee89b31f.jpg'
# image = cv2.imread(image_path)

# # 初始化 YOLOv8 模型
# model = YOLO('F:\\Lab\\share\\YOLO_segmentation\\best.pt')

# # 執行預測
# results = model(image)

# # 獲取第一個結果
# result = results[0]

# # 獲取 OBB 信息
# obb_info = result.obb

# # 建立 mask_images 資料夾
# import os
# if not os.path.exists('mask_images'):
#     os.makedirs('mask_images')

# # 對每個邊界框進行處理
# for i in range(len(obb_info.xyxyxyxy)):
#     # 獲取邊界框的四個角點座標
#     pts = obb_info.xyxyxyxy[i].numpy().reshape(-1, 2).astype(np.int32)
    
#     # 計算邊界框的中心點座標
#     center_x = int((pts[0][0] + pts[2][0]) / 2)
#     center_y = int((pts[0][1] + pts[2][1]) / 2)
    
#     # 計算邊界框的寬和高
#     width = int(np.linalg.norm(pts[1] - pts[0]))
#     height = int(np.linalg.norm(pts[2] - pts[1]))
    
#     # 計算放大比例
#     scale = min(640 / width, 640 / height)
    
#     # 計算新圖像的寬和高
#     new_width = int(width * scale)
#     new_height = int(height * scale)
    
#     # 創建一個黑色底的 640x640 圖像
#     new_image = np.zeros((640, 640, 3), dtype=np.uint8)
    
#     # 計算旋轉角度
#     angle = math.atan2(pts[1][1] - pts[0][1], pts[1][0] - pts[0][0]) * 180 / math.pi
    
#     # 獲取變換矩陣
#     M = cv2.getRotationMatrix2D((center_x, center_y), angle, scale)
#     # 將原始圖像進行放大和旋轉
#     resized_image = cv2.warpAffine(image, M, (new_width, new_height))
    
#     # 計算放置位置
#     x_offset = int((640 - new_width) / 2)
#     y_offset = int((640 - new_height) / 2)
    
#     # 在新圖像中心位置放置原始圖像
#     new_image[y_offset:y_offset+new_height, x_offset:x_offset+new_width] = resized_image
    
#     # 保存圖像
#     cv2.imwrite(f'mask_images/mask_{i}.jpg', new_image)




